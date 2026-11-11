// Converte src/*.md (Markdown + LaTeX) em PDF, com as fórmulas compostas em KaTeX.
const fs = require('fs'), path = require('path');
const katex = require('katex');
require('katex/contrib/mhchem');
const md = require('markdown-it')({ html: true, typographer: false });
const { chromium } = require('playwright');

const SRC = __dirname, OUT = path.join(__dirname, '..', 'pdf'), HTML = path.join(__dirname, 'html');
fs.mkdirSync(OUT, { recursive: true }); fs.mkdirSync(HTML, { recursive: true });
const katexCss = 'file://' + require.resolve('katex/dist/katex.min.css');
const css = fs.readFileSync(path.join(SRC, 'style.css'), 'utf8');

function tex(src, display) {
  // vírgula decimal sem espaço: 0,86 -> 0{,}86
  src = src.replace(/(\d),(?=\d)/g, '$1{,}');
  return katex.renderToString(src, { displayMode: display, throwOnError: true, strict: false, trust: true });
}

function render(file) {
  let text = fs.readFileSync(file, 'utf8');
  const meta = {};
  text = text.replace(/^---\n([\s\S]*?)\n---\n/, (_, y) => {
    y.split('\n').forEach(l => { const i = l.indexOf(':'); if (i > 0) meta[l.slice(0, i).trim()] = l.slice(i + 1).trim(); });
    return '';
  });
  text = text.replace(/\{\{code:([\w.-]+)\}\}/g, (_, n) =>
    '```c\n' + fs.readFileSync(path.join(SRC, '..', 'codigo-C', n), 'utf8').trimEnd() + '\n```');
  text = text.replace(/\{\{fig:([\w-]+)\}\}/g, (_, n) =>
    '<div class="fig">' + fs.readFileSync(path.join(SRC, 'figs', n + '.svg'), 'utf8').replace(/\n\s*/g, ' ') + '</div>');
  const store = [];
  const keep = html => { store.push(html); return 'ZZMATH' + (store.length - 1) + 'ZZ'; };
  const code = [];
  text = text.replace(/```[\s\S]*?```/g, m => { code.push(m); return 'ZZCODE' + (code.length - 1) + 'ZZ'; });
  text = text.replace(/\$\$([\s\S]+?)\$\$/g, (_, s) => {
    try { return '\n\n' + keep('<div class="eq">' + tex(s.trim(), true) + '</div>') + '\n\n'; }
    catch (e) { throw new Error(path.basename(file) + ': ' + e.message + '\n' + s); }
  });
  text = text.replace(/\$([^\$\n]+?)\$/g, (_, s) => {
    try { return keep(tex(s, false)); }
    catch (e) { throw new Error(path.basename(file) + ': ' + e.message + '\n' + s); }
  });
  text = text.replace(/ZZCODE(\d+)ZZ/g, (_, i) => code[+i]);
  let body = md.render(text);
  body = body.replace(/<p>ZZMATH(\d+)ZZ<\/p>/g, (_, i) => store[+i]).replace(/ZZMATH(\d+)ZZ/g, (_, i) => store[+i]);
  const head = `<header class="capa"><div class="inst">${meta.instituicao || ''}</div>
<h1>${meta.titulo}</h1><div class="sub">${meta.subtitulo || ''}</div>
<table class="meta"><tr>${(meta.info || '').split('|').map(s => { const [k, ...v] = s.split('='); return `<td><span>${k.trim()}</span>${v.join('=').trim()}</td>`; }).join('')}</tr></table></header>`;
  return { meta, html: `<!doctype html><html lang="pt"><head><meta charset="utf-8"><title>${meta.titulo}</title>
<link rel="stylesheet" href="${katexCss}"><style>${css}</style></head><body>${head}<main>${body}</main></body></html>` };
}

(async () => {
  const only = process.argv.slice(2);
  const files = fs.readdirSync(SRC).filter(f => /^\d\d-.*\.md$/.test(f)).filter(f => !only.length || only.some(o => f.includes(o))).sort();
  const browser = await chromium.launch();
  for (const f of files) {
    const { meta, html } = render(path.join(SRC, f));
    const hp = path.join(HTML, f.replace(/\.md$/, '.html'));
    fs.writeFileSync(hp, html);
    const page = await browser.newPage();
    await page.goto('file://' + hp, { waitUntil: 'networkidle' });
    await page.evaluate(() => document.fonts.ready);
    const out = path.join(OUT, meta.ficheiro || f.replace(/\.md$/, '.pdf'));
    await page.pdf({
      path: out, format: 'A4', printBackground: true, displayHeaderFooter: true,
      margin: { top: '18mm', bottom: '18mm', left: '17mm', right: '17mm' },
      headerTemplate: `<div style="width:100%;font-family:Inter,sans-serif;font-size:7.5px;color:#777;padding:0 17mm;display:flex;justify-content:space-between"><span>${meta.titulo}</span><span>${meta.rodape || ''}</span></div>`,
      footerTemplate: `<div style="width:100%;font-family:Inter,sans-serif;font-size:7.5px;color:#777;text-align:center">Página <span class="pageNumber"></span> de <span class="totalPages"></span></div>`,
    });
    await page.close();
    console.log('ok', path.basename(out));
  }
  await browser.close();
})().catch(e => { console.error(e.message); process.exit(1); });
