#!/usr/bin/env python3
"""Gera as figuras (SVG) usadas nas resoluções. Saída: figs/*.svg"""
import math, os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'figs')
os.makedirs(OUT, exist_ok=True)

INK, BLUE, RED, GREEN, GREY = '#1c1c1e', '#1f5fae', '#c0392b', '#18794e', '#8a93a0'
SANS = 'Inter, Arial, sans-serif'
MATH = 'KaTeX_Main, "Times New Roman", serif'


class Svg:
    def __init__(self, w, h):
        self.w, self.h, self.e = w, h, []

    def add(self, s):
        self.e.append(s)

    def line(self, x1, y1, x2, y2, c=INK, w=1.3, dash=None, extra=''):
        d = f' stroke-dasharray="{dash}"' if dash else ''
        self.add(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{c}" stroke-width="{w}" stroke-linecap="round"{d} {extra}/>')

    def poly(self, pts, c=INK, w=1.5, fill='none', dash=None, close=False, op=1):
        d = f' stroke-dasharray="{dash}"' if dash else ''
        p = ' '.join(f'{x:.1f},{y:.1f}' for x, y in pts)
        tag = 'polygon' if close else 'polyline'
        self.add(f'<{tag} points="{p}" fill="{fill}" fill-opacity="{op}" stroke="{c}" stroke-width="{w}" stroke-linejoin="round" stroke-linecap="round"{d}/>')

    def circle(self, x, y, r, c=INK, w=1.3, fill='none'):
        self.add(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{fill}" stroke="{c}" stroke-width="{w}"/>')

    def rect(self, x, y, w, h, fill='#dfe7f2', c=INK, sw=1):
        self.add(f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" fill="{fill}" stroke="{c}" stroke-width="{sw}"/>')

    def text(self, x, y, s, size=10, c=INK, anchor='middle', font=SANS, weight='normal', style='normal'):
        self.add(f'<text x="{x:.1f}" y="{y:.1f}" font-size="{size}" fill="{c}" text-anchor="{anchor}" font-family=\'{font}\' font-weight="{weight}" font-style="{style}">{s}</text>')

    def arrow(self, x1, y1, x2, y2, c=INK, w=1.5, head=7):
        a = math.atan2(y2 - y1, x2 - x1)
        self.line(x1, y1, x2 - 0.6 * head * math.cos(a), y2 - 0.6 * head * math.sin(a), c, w)
        p = [(x2, y2), (x2 - head * math.cos(a - 0.4), y2 - head * math.sin(a - 0.4)),
             (x2 - head * math.cos(a + 0.4), y2 - head * math.sin(a + 0.4))]
        self.poly(p, c, 0.5, fill=c, close=True)

    def save(self, name):
        s = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {self.w} {self.h}" width="{self.w}" height="{self.h}">'
             + ''.join(self.e) + '</svg>')
        open(os.path.join(OUT, name + '.svg'), 'w').write(s)


def sub(a, b):
    return f'{a}<tspan baseline-shift="sub" font-size="70%">{b}</tspan>'


CH3 = 'CH₃'


# ───────────────────────── Química Orgânica ─────────────────────────
def newman(s, cx, cy, theta, r=15, L=28, fs=8.5):
    """Projecção de Newman do 2,3-dimetilbutano (C2 à frente, C3 atrás); theta = diedro H–C2–C3–H."""
    front = [(90, 'H'), (210, CH3), (330, CH3)]
    ecl = theta % 120 == 0
    off = 12 if ecl else 0  # pequeno desvio para se verem as ligações eclipsadas
    back = [(90 + theta, 'H'), (210 + theta, CH3), (330 + theta, CH3)]
    for ang, lab in back:
        a = math.radians(ang + off)
        s.line(cx + r * math.cos(a), cy - r * math.sin(a), cx + L * math.cos(a), cy - L * math.sin(a), RED, 1.3)
        t = math.radians(ang + (34 if ecl else 0))
        s.text(cx + (L + 10) * math.cos(t), cy - (L + 10) * math.sin(t) + 3, lab, fs, RED)
    s.circle(cx, cy, r, INK, 1.3, 'white')
    for ang, lab in front:
        a = math.radians(ang)
        s.line(cx, cy, cx + L * math.cos(a), cy - L * math.sin(a), INK, 1.3)
        s.text(cx + (L + 10) * math.cos(a), cy - (L + 10) * math.sin(a) + 3, lab, fs, INK)
    s.circle(cx, cy, 1.6, INK, 1, INK)


def fig_newman():
    W, H = 760, 470
    s = Svg(W, H)
    x0, dx = 62, 106
    yE = lambda e: 440 - (e / 30) * 250
    ang = [0, 60, 120, 180, 240, 300, 360]
    en = [26, 11.4, 23, 7.6, 23, 11.4, 26]
    rom = ['I', 'II', 'III', 'IV', 'V', 'VI', 'I']
    # eixos
    s.line(x0 - 22, 440, x0 + 6 * dx + 24, 440)
    s.line(x0 - 22, 440, x0 - 22, 175)
    for e in (0, 5, 10, 15, 20, 25, 30):
        s.line(x0 - 26, yE(e), x0 - 22, yE(e))
        s.text(x0 - 30, yE(e) + 3, str(e), 8.5, anchor='end')
    s.add(f'<text transform="translate(12,315) rotate(-90)" font-size="9.5" text-anchor="middle" font-family=\'{SANS}\'>Energia potencial (kJ/mol)</text>')
    s.text(x0 + 3 * dx, 468, 'Ângulo de torção (diedro H–C2–C3–H)', 9.5)
    pts = []
    for i in range(6):
        for k in range(41):
            t = k / 40
            e = en[i] + (en[i + 1] - en[i]) * (1 - math.cos(math.pi * t)) / 2
            pts.append((x0 + (i + t) * dx, yE(e)))
    s.poly(pts, BLUE, 2)
    for i, (a, e) in enumerate(zip(ang, en)):
        x = x0 + i * dx
        s.line(x, 128, x, yE(e) - 4, GREY, 0.8, dash='3 3')
        s.line(x, 440, x, 444)
        s.text(x, 455, f'{a}°', 8.5)
        s.circle(x, yE(e), 3, BLUE, 1, BLUE)
        lab = f'{e:g}'.replace('.', ',')
        s.text(x + (16 if i < 6 else -16), yE(e) + (14 if e < 15 else -7), lab, 8.5, BLUE, weight='600')
        newman(s, x, 70, a)
        s.text(x, 124, rom[i], 10, INK, weight='700')
        s.text(x, 14, 'eclipsada' if a % 120 == 0 else 'alternada', 8, GREY)
    s.save('qo-newman')


def zig(x0, y0, n, up_first=True, b=26):
    dx, dy = b * math.cos(math.radians(30)), b * math.sin(math.radians(30))
    pts = []
    for i in range(n):
        up = (i % 2 == 0) == up_first
        pts.append((x0 + i * dx, y0 - (dy if up else 0)))
    return pts


def vdir(pts, i):
    """Direcção 'para fora' do vértice i de um zigue-zague (+1 = para baixo no ecrã)."""
    j = i + 1 if i + 1 < len(pts) else i - 1
    return -1 if pts[i][1] < pts[j][1] else 1


def chain_sub(s, p, d, n, b=24, c=INK, w=1.5):
    """Substituinte de n carbonos a partir de p, na vertical (d=±1), em zigue-zague."""
    pts = [p]
    x, y = p
    for k in range(n):
        if k == 0:
            y += d * b
        else:
            x += b * math.cos(math.radians(30)) * (1 if k % 2 else -1)
            y += d * b * math.sin(math.radians(30))
        pts.append((x, y))
    s.poly(pts, c, w)
    return pts


def numbers(s, pts, labels=None, c=BLUE, fs=8.5):
    for i, p in enumerate(pts):
        d = vdir(pts, i)
        lab = labels[i] if labels else str(i + 1)
        if lab:
            s.text(p[0], p[1] + (-5 if d < 0 else 12), lab, fs, c, weight='600')


def numbers_opp(s, pts, c=BLUE, fs=8.5, start=1):
    """Numera do lado de dentro (oposto ao substituinte)."""
    for i, p in enumerate(pts):
        d = vdir(pts, i)
        s.text(p[0], p[1] + (12 if d < 0 else -5), str(i + start), fs, c, weight='600')


def fig_qo_structs():
    # a) biciclo[2.2.2]octano
    s = Svg(200, 130)
    A, B = (30, 65), (170, 65)
    br = [[(70, 22), (130, 22)], [(84, 56), (118, 74)], [(70, 108), (130, 108)]]
    for b_ in br:
        s.poly([A] + b_ + [B], INK, 1.6)
    for p in [A, B] + sum(br, []):
        s.circle(p[0], p[1], 2.2, INK, 1, INK)
    lab = {(30, 65): ('1', -10, 4), (70, 22): ('2', 0, -7), (130, 22): ('3', 0, -7), (170, 65): ('4', 10, 4),
           (130, 108): ('5', 0, 16), (70, 108): ('6', 0, 16), (84, 56): ('7', -2, -7), (118, 74): ('8', 4, 16)}
    for p, (t, dx, dy) in lab.items():
        s.text(p[0] + dx, p[1] + dy, t, 8.5, BLUE, weight='600')
    s.save('qo-4a')

    # b) 2,2,6,7-tetrametil-4-propiloctano
    s = Svg(260, 140)
    p = zig(30, 62, 8, up_first=False)
    s.poly(p, INK, 1.6)
    c2 = p[1]
    for a in (60, 120):
        s.line(c2[0], c2[1], c2[0] + 22 * math.cos(math.radians(a)), c2[1] - 22 * math.sin(math.radians(a)), INK, 1.6)
    chain_sub(s, p[3], -1, 3)
    chain_sub(s, p[5], -1, 1)
    chain_sub(s, p[6], 1, 1)
    for i, q in enumerate(p):
        d = vdir(p, i)
        s.text(q[0] + (0 if i not in (1, 3, 5) else 0), q[1] + (12 if d < 0 else -5) + (0), str(i + 1), 8.5, BLUE, weight='600')
    s.save('qo-4b')

    # c) 3-etil-2-metil-hexano
    s = Svg(200, 110)
    p = zig(30, 55, 6, up_first=False)
    s.poly(p, INK, 1.6)
    chain_sub(s, p[1], -1, 1)
    chain_sub(s, p[2], 1, 2)
    numbers_opp(s, p)
    s.save('qo-4c')

    # d) 1,4-diciclopropil-hexano
    s = Svg(250, 120)
    p = zig(70, 62, 6, up_first=True)
    s.poly(p, INK, 1.6)
    # ciclopropilo em C1 (à esquerda)
    a = (p[0][0] - 24, p[0][1] + 6)
    s.line(p[0][0], p[0][1], a[0], a[1], INK, 1.6)
    s.poly([a, (a[0] - 22, a[1] - 12), (a[0] - 22, a[1] + 14)], INK, 1.6, close=True)
    # ciclopropilo em C4 (para baixo)
    c4 = p[3]
    b_ = (c4[0], c4[1] + 24)
    s.line(c4[0], c4[1], b_[0], b_[1], INK, 1.6)
    s.poly([b_, (b_[0] - 13, b_[1] + 22), (b_[0] + 13, b_[1] + 22)], INK, 1.6, close=True)
    for i, q in enumerate(p):
        d = vdir(p, i)
        s.text(q[0] + (5 if i == 0 else 0), q[1] + (12 if d < 0 else -5) + (0 if i else -18 + 6), str(i + 1), 8.5, BLUE, weight='600')
    s.save('qo-4d')

    # e) 2,5-dibromo-4-etiloctano
    s = Svg(260, 130)
    p = zig(30, 62, 8, up_first=True)
    s.poly(p, BLUE, 2.2)
    q = chain_sub(s, p[1], 1, 1)
    s.text(q[-1][0], q[-1][1] + 11, 'Br', 10, INK, weight='600')
    chain_sub(s, p[3], 1, 2)
    q = chain_sub(s, p[4], -1, 1)
    s.text(q[-1][0], q[-1][1] - 4, 'Br', 10, INK, weight='600')
    numbers_opp(s, p)
    s.save('qo-4e')

    # f) 3,5,7-trimetilnonano  (cadeia principal a azul)
    s = Svg(260, 140)
    p = zig(40, 50, 7, up_first=True)   # zigue-zague desenhado no enunciado (7 C)
    e1 = chain_sub(s, p[1], 1, 2, c=BLUE, w=2.2)
    e2 = chain_sub(s, p[5], 1, 2, c=BLUE, w=2.2)
    s.poly(p[1:6], BLUE, 2.2)
    s.line(*p[0], *p[1], INK, 1.6)
    s.line(*p[6], *p[5], INK, 1.6)
    chain_sub(s, p[3], 1, 1)
    main = [e1[2], e1[1], p[1], p[2], p[3], p[4], p[5], e2[1], e2[2]]
    offs = [(-8, 4), (-9, 4), (0, -9), (0, -6), (0, -9), (0, -6), (0, -9), (-9, 4), (9, 4)]
    for i, (q, o) in enumerate(zip(main, offs)):
        s.text(q[0] + o[0], q[1] + o[1], str(i + 1), 8.5, BLUE, weight='600')
    s.save('qo-4f')

    # g) 7-clorobiciclo[2.2.1]heptano
    s = Svg(220, 150)
    C = {1: (40, 85), 2: (72, 128), 3: (138, 128), 4: (170, 85), 5: (130, 74), 6: (80, 74), 7: (105, 34)}
    for a, b_ in [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 1), (1, 7), (7, 4)]:
        s.line(*C[a], *C[b_], INK, 1.6)
    s.line(*C[7], 128, 14, INK, 1.6)
    s.text(139, 13, 'Cl', 10.5, INK, weight='600')
    off = {1: (-9, 4), 2: (-4, 13), 3: (4, 13), 4: (9, 4), 5: (2, -6), 6: (-2, -6), 7: (-9, 0)}
    for k, q in C.items():
        s.circle(q[0], q[1], 2.2, INK, 1, INK)
        s.text(q[0] + off[k][0], q[1] + off[k][1], str(k), 8.5, BLUE, weight='600')
    s.save('qo-4g')

    # h) ciclobutilciclopentano
    s = Svg(220, 110)
    cx, cy, r = 70, 55, 30
    pent = [(cx + r * math.cos(math.radians(72 * k)), cy - r * math.sin(math.radians(72 * k))) for k in range(5)]
    s.poly(pent, INK, 1.6, close=True)
    j = (pent[0][0] + 26, pent[0][1])
    s.line(*pent[0], *j, INK, 1.6)
    d = 22
    s.poly([j, (j[0] + d, j[1] - d), (j[0] + 2 * d, j[1]), (j[0] + d, j[1] + d)], INK, 1.6, close=True)
    s.text(cx, cy + 3, 'ciclopentano', 7.5, GREY)
    s.text(j[0] + d, j[1] + d + 14, 'ciclobutilo', 7.5, GREY)
    s.save('qo-4h')


# ───────────────────────── Gráficos (helper) ─────────────────────────
class Plot:
    def __init__(self, w, h, xr, yr, ml=46, mr=14, mt=14, mb=34):
        self.s = Svg(w, h)
        self.xr, self.yr = xr, yr
        self.x0, self.x1, self.y0, self.y1 = ml, w - mr, h - mb, mt

    def X(self, x):
        return self.x0 + (x - self.xr[0]) / (self.xr[1] - self.xr[0]) * (self.x1 - self.x0)

    def Y(self, y):
        return self.y0 + (y - self.yr[0]) / (self.yr[1] - self.yr[0]) * (self.y1 - self.y0)

    def P(self, x, y):
        return (self.X(x), self.Y(y))

    def axes_xy(self, xl='x', yl='y', xt=(), yt=(), fmt=lambda v: f'{v:g}'.replace('.', ',')):
        s = self.s
        ox = min(max(0, self.xr[0]), self.xr[1])
        oy = min(max(0, self.yr[0]), self.yr[1])
        s.arrow(self.x0 - 4, self.Y(oy), self.x1 + 8, self.Y(oy), INK, 1.1, 6)
        s.arrow(self.X(ox), self.y0 + 4, self.X(ox), self.y1 - 8, INK, 1.1, 6)
        s.text(self.x1 + 8, self.Y(oy) - 7, xl, 11, anchor='end', font=MATH, style='italic')
        s.text(self.X(ox) + 8, self.y1 - 2, yl, 11, anchor='start', font=MATH, style='italic')
        for v in xt:
            s.line(self.X(v), self.Y(oy) - 3, self.X(v), self.Y(oy) + 3, INK, 1)
            s.text(self.X(v), self.Y(oy) + 14, fmt(v), 8.5)
        for v in yt:
            s.line(self.X(ox) - 3, self.Y(v), self.X(ox) + 3, self.Y(v), INK, 1)
            s.text(self.X(ox) - 6, self.Y(v) + 3, fmt(v), 8.5, anchor='end')


def histogram(name, edges, freq, xlabel, w=520, h=270, polygon=True, fmt=lambda v: f'{v:g}'.replace('.', ',')):
    fm = max(freq)
    ymax = fm + 2
    hw = edges[1] - edges[0]
    p = Plot(w, h, (edges[0] - hw, edges[-1] + hw), (0, ymax), ml=44, mb=40)
    s = p.s
    for v in range(0, ymax + 1, 2):
        s.line(p.x0, p.Y(v), p.x1, p.Y(v), '#e3e7ed', 0.8)
        s.text(p.x0 - 6, p.Y(v) + 3, str(v), 8.5, anchor='end')
    for i, f in enumerate(freq):
        if f:
            s.rect(p.X(edges[i]), p.Y(f), p.X(edges[i + 1]) - p.X(edges[i]), p.Y(0) - p.Y(f), '#c9d8ee', '#1f3a5f', 1)
        s.text(p.X((edges[i] + edges[i + 1]) / 2), p.Y(f) - 5, str(f), 9, weight='600')
    for e in edges:
        s.line(p.X(e), p.Y(0), p.X(e), p.Y(0) + 4, INK, 1)
        s.text(p.X(e), p.Y(0) + 15, fmt(e), 8.5)
    s.line(p.x0, p.Y(0), p.x1, p.Y(0), INK, 1.2)
    s.line(p.x0, p.Y(0), p.x0, p.y1, INK, 1.2)
    if polygon:
        mids = [(edges[i] + edges[i + 1]) / 2 for i in range(len(freq))]
        pts = [p.P(edges[0] - hw / 2, 0)] + [p.P(m, f) for m, f in zip(mids, freq)] + [p.P(edges[-1] + hw / 2, 0)]
        s.poly(pts, RED, 1.5)
        for q in pts[1:-1]:
            s.circle(q[0], q[1], 2.4, RED, 1, RED)
    s.text((p.x0 + p.x1) / 2, h - 6, xlabel, 9.5)
    s.add(f'<text transform="translate(12,{(p.y0 + p.y1) / 2:.0f}) rotate(-90)" font-size="9.5" text-anchor="middle" font-family=\'{SANS}\'>Frequência absoluta</text>')
    s.save(name)


def fig_stats():
    histogram('est-hist-ep', [70.8 + 3 * i for i in range(8)], [3, 10, 3, 10, 6, 10, 8], 'Eficiência de Produção — E.P. (%)',
              fmt=lambda v: f'{v:.1f}'.replace('.', ','))
    histogram('est-hist-tp', [640 + 117 * i for i in range(7)], [11, 2, 13, 0, 11, 13], 'Taxa de produção — TP (bpd)')


# ───────────────────────── Física ─────────────────────────
def fig_fisica():
    # MHS
    p = Plot(520, 220, (0, 4), (-0.125, 0.125), ml=50, mb=24)
    s = p.s
    for v in (-0.10, -0.05, 0.05, 0.10):
        s.line(p.x0, p.Y(v), p.x1, p.Y(v), '#e3e7ed', 0.8)
    p.axes_xy('t (s)', 'x (m)', xt=(0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4), yt=(-0.10, -0.05, 0.05, 0.10),
              fmt=lambda v: f'{v:.2f}'.replace('.', ',') if abs(v) < 0.2 else f'{v:g}'.replace('.', ','))
    f = lambda t: 0.10 * math.cos(math.pi * t + math.pi / 3)
    s.poly([p.P(t / 100, f(t / 100)) for t in range(0, 401)], BLUE, 2)
    for t, lab, c in ((5 / 3, '1,67 s', GREEN), (11 / 3, '3,67 s', GREEN), (2 / 3, '0,67 s', RED), (8 / 3, '2,67 s', RED)):
        s.circle(p.X(t), p.Y(f(t)), 3, c, 1, c)
        s.text(p.X(t), p.Y(f(t)) + (-7 if f(t) > 0 else 14), lab, 8.5, c, weight='600')
    s.circle(p.X(0), p.Y(0.05), 3, INK, 1, INK)
    s.text(p.X(0) + 30, p.Y(0.05) - 5, 'x(0) = 0,05 m', 8.5)
    s.save('fis-mhs')

    # onda estacionária n = 4
    W, H = 520, 190
    s = Svg(W, H)
    xa, xb, ym, A = 50, 470, 78, 42
    L = xb - xa
    up = [(xa + L * k / 400, ym - A * math.sin(4 * math.pi * k / 400)) for k in range(401)]
    dn = [(x, 2 * ym - y) for x, y in up]
    s.line(xa, ym, xb, ym, GREY, 0.8, dash='4 3')
    s.poly(up, BLUE, 2)
    s.poly(dn, BLUE, 1.4, dash='5 4')
    s.rect(xa - 8, ym - 30, 8, 60, '#b9c1cd', INK, 1)
    s.rect(xb, ym - 30, 8, 60, '#b9c1cd', INK, 1)
    labs = ['x₁ = 0', 'x₂ = λ/2', 'x₃ = λ', 'x₄ = 3λ/2', 'x₅ = 2λ']
    vals = ['0', '0,30 m', '0,60 m', '0,90 m', '1,20 m']
    for i in range(5):
        x = xa + L * i / 4
        s.circle(x, ym, 3.6, RED, 1, RED)
        s.text(x, ym + 62, labs[i], 9.5, RED, weight='600')
        s.text(x, ym + 75, vals[i], 8.5, GREY)
        s.text(x, ym + 49, 'N', 9, RED, weight='700')
    for i in range(4):
        x = xa + L * (2 * i + 1) / 8
        s.text(x, ym - A - 7, 'V', 9, BLUE, weight='700')
    s.line(xa, 170, xb, 170, INK, 1)
    s.line(xa, 166, xa, 174, INK, 1)
    s.line(xb, 166, xb, 174, INK, 1)
    s.text((xa + xb) / 2, 184, 'L = 2λ = 1,20 m   (n = 4 ventres, 5 nós)', 9.5)
    s.save('fis-corda')

    # cargas
    p = Plot(400, 330, (-1, 5.6), (-1.2, 4), ml=20, mr=20, mt=16, mb=16)
    s = p.s
    for v in range(0, 6):
        s.line(p.X(v), p.Y(-1.2), p.X(v), p.Y(4), '#e9ecf1', 0.8)
    for v in range(-1, 5):
        s.line(p.X(-1), p.Y(v), p.X(5.6), p.Y(v), '#e9ecf1', 0.8)
    p.axes_xy('x (m)', 'y (m)', xt=(1, 2, 3, 4, 5), yt=(1, 2, 3))
    ch = [((0, 0), 'q₁ = +2 μC', RED, (36, 4)), ((4, 0), 'q₂ = −3 μC', BLUE, (10, 4)), ((0, 3), 'q₃ = +1 μC', RED, (44, -8))]
    for (x, y), lab, c, o in ch:
        s.line(p.X(x), p.Y(y), p.X(2), p.Y(1), GREY, 0.8, dash='3 3')
    sc = 1 / 3600  # 3600 N/C -> 1 m no desenho
    P_ = (2, 1)
    for (ex, ey), lab, c, o in (((3220, 1610), 'E₁', RED, (6, -4)), ((4830, -2415), 'E₂', BLUE, (4, 12)), ((795, -795), 'E₃', '#b9770e', (-14, 10))):
        s.arrow(p.X(2), p.Y(1), p.X(2 + ex * sc), p.Y(1 + ey * sc), c, 1.6)
        s.text(p.X(2 + ex * sc) + o[0], p.Y(1 + ey * sc) + o[1], lab, 10, c, weight='700')
    s.arrow(p.X(2), p.Y(1), p.X(2 + 8845 * sc), p.Y(1 - 1600 * sc), INK, 2.2, 8)
    s.text(p.X(2 + 8845 * sc) - 2, p.Y(1 - 1600 * sc) - 7, 'E', 11, INK, weight='700')
    for (x, y), lab, c, o in ch:
        s.circle(p.X(x), p.Y(y), 6.5, c, 1, c)
        s.text(p.X(x), p.Y(y) + 3.4, '+' if c == RED else '−', 10, 'white', weight='700')
        s.text(p.X(x) + o[0], p.Y(y) + o[1] + 26 if y == 0 else p.Y(y) + o[1], lab, 9, c, weight='600')
    s.circle(p.X(2), p.Y(1), 3, INK, 1, INK)
    s.text(p.X(2) - 4, p.Y(1) - 8, 'P(2; 1)', 9, INK, weight='600')
    s.save('fis-campo')

    p = Plot(400, 330, (-1, 5.6), (-1.2, 4.6), ml=20, mr=20, mt=16, mb=16)
    s = p.s
    p.axes_xy('x (m)', 'y (m)', xt=(1, 2, 3, 4, 5), yt=(1, 2, 3, 4))
    s.line(p.X(0), p.Y(3), p.X(4), p.Y(0), GREY, 0.8, dash='3 3')
    fs_ = 1 / 1.6  # 1,6 mN -> 1 m
    s.arrow(p.X(0), p.Y(3), p.X(0), p.Y(3 + 2.0 * fs_), RED, 1.8)
    s.text(p.X(0) - 14, p.Y(3 + 2.0 * fs_) + 6, 'F₁₃', 10, RED, weight='700')
    s.arrow(p.X(0), p.Y(3), p.X(0.864 * fs_), p.Y(3 - 0.648 * fs_), BLUE, 1.8)
    s.text(p.X(0.864 * fs_) + 12, p.Y(3 - 0.648 * fs_) + 10, 'F₂₃', 10, BLUE, weight='700')
    s.arrow(p.X(0), p.Y(3), p.X(0.864 * fs_), p.Y(3 + 1.352 * fs_), INK, 2.3, 8)
    s.text(p.X(0.864 * fs_) + 14, p.Y(3 + 1.352 * fs_), 'F₃', 11, INK, weight='700')
    s.line(p.X(0.864 * fs_), p.Y(3 - 0.648 * fs_), p.X(0.864 * fs_), p.Y(3 + 1.352 * fs_), GREY, 0.8, dash='3 3')
    s.line(p.X(0), p.Y(3 + 2.0 * fs_), p.X(0.864 * fs_), p.Y(3 + 1.352 * fs_), GREY, 0.8, dash='3 3')
    for (x, y), lab, c, o in (((0, 0), 'q₁ = +2 μC', RED, (40, 30)), ((4, 0), 'q₂ = −3 μC', BLUE, (10, 30)), ((0, 3), 'q₃', RED, (-14, 4))):
        s.circle(p.X(x), p.Y(y), 6.5, c, 1, c)
        s.text(p.X(x), p.Y(y) + 3.4, '+' if c == RED else '−', 10, 'white', weight='700')
        s.text(p.X(x) + o[0], p.Y(y) + o[1], lab, 9, c, weight='600')
    s.save('fis-forca')


# ───────────────────────── Cálculo III ─────────────────────────
def fig_cdi():
    # Q1: região sob a parábola y = 4 - x², -2 <= x <= 0
    p = Plot(300, 250, (-2.8, 1.2), (-0.6, 4.8), ml=16, mr=16, mt=12, mb=12)
    s = p.s
    reg = [p.P(-2, 0)] + [p.P(-2 + 2 * k / 60, 4 - (-2 + 2 * k / 60) ** 2) for k in range(61)] + [p.P(0, 0)]
    s.poly(reg, BLUE, 0.1, fill='#c9d8ee', close=True, op=0.9)
    p.axes_xy(xt=(-2, -1, 1), yt=(1, 2, 3, 4))
    s.poly([p.P(-2.25 + 2.9 * k / 80, 4 - (-2.25 + 2.9 * k / 80) ** 2) for k in range(81) if 4 - (-2.25 + 2.9 * k / 80) ** 2 > -0.6], BLUE, 1.8)
    s.text(p.X(-1.9), p.Y(3.2), 'y = 4 − x²', 10, BLUE, font=MATH, style='italic')
    s.text(p.X(-1.95), p.Y(2.75), '(x = −√(4 − y))', 9, BLUE, font=MATH, style='italic')
    s.text(p.X(-0.7), p.Y(1.3), 'D', 14, INK, font=MATH, style='italic')
    # faixa horizontal
    y = 2.2
    s.arrow(p.X(-math.sqrt(4 - y)), p.Y(y), p.X(0), p.Y(y), RED, 1.5, 6)
    s.text(p.X(-0.62), p.Y(y) - 5, 'dx (y fixo)', 8.5, RED)
    s.save('cdi-q1')

    # Q2: quarto de disco no 2.º quadrante
    p = Plot(300, 246, (-7.6, 3), (-1, 7.6), ml=14, mr=14, mt=12, mb=12)
    s = p.s
    reg = [p.P(0, 0)] + [p.P(6 * math.cos(math.radians(90 + k * 1.5)), 6 * math.sin(math.radians(90 + k * 1.5))) for k in range(61)]
    s.poly(reg, BLUE, 0.1, fill='#c9d8ee', close=True, op=0.9)
    p.axes_xy(xt=(-6, -3), yt=(3, 6))
    s.poly(reg[1:], BLUE, 1.8)
    a = math.radians(135)
    s.arrow(p.X(0), p.Y(0), p.X(6 * math.cos(a)), p.Y(6 * math.sin(a)), RED, 1.5, 6)
    s.text(p.X(-2.6), p.Y(3.3), 'r', 12, RED, font=MATH, style='italic')
    arc = [p.P(1.6 * math.cos(math.radians(k)), 1.6 * math.sin(math.radians(k))) for k in range(0, 136, 5)]
    s.poly(arc, RED, 1.1)
    s.text(p.X(1.2), p.Y(1.7), 'θ', 12, RED, font=MATH, style='italic')
    s.text(p.X(-5.2), p.Y(6.2), 'x² + y² = 36', 10, BLUE, font=MATH, style='italic')
    s.text(p.X(-2.2), p.Y(1.0), 'π/2 ≤ θ ≤ π,  0 ≤ r ≤ 6', 8.5, INK)
    s.save('cdi-q2')

    # Q3: corte no plano r–z
    p = Plot(300, 180, (-3.6, 3.6), (-0.5, 3.6), ml=14, mr=14, mt=12, mb=12)
    s = p.s
    R = math.sqrt(8)
    top = [p.P(R * math.sin(math.radians(k)), R * math.cos(math.radians(k))) for k in range(-45, 46, 3)]
    s.poly([p.P(0, 0)] + top, BLUE, 0.1, fill='#c9d8ee', close=True, op=0.9)
    p.axes_xy('r', 'z', xt=(-2, 2), yt=(2,))
    s.poly([p.P(R * math.sin(math.radians(k)), R * math.cos(math.radians(k))) for k in range(-90, 91, 3)], BLUE, 1.8)
    s.poly([p.P(-3.3, 3.3), p.P(0, 0), p.P(3.3, 3.3)], RED, 1.8)
    s.line(p.X(2), p.Y(0), p.X(2), p.Y(2), GREY, 0.9, dash='3 3')
    s.line(p.X(-2), p.Y(0), p.X(-2), p.Y(2), GREY, 0.9, dash='3 3')
    s.text(p.X(-1.75), p.Y(3.25), 'z = √(8 − r²)', 9.5, BLUE, font=MATH, style='italic')
    s.text(p.X(3.0), p.Y(2.45), 'z = r', 10, RED, font=MATH, style='italic')
    s.text(p.X(0.55), p.Y(1.9), 'W', 13, INK, font=MATH, style='italic')
    s.save('cdi-q3')

    # Q4: círculo x² + y² = 4x
    p = Plot(300, 252, (-1.2, 5.2), (-2.7, 2.7), ml=14, mr=14, mt=12, mb=12)
    s = p.s
    circ = [p.P(2 + 2 * math.cos(math.radians(k)), 2 * math.sin(math.radians(k))) for k in range(0, 361, 4)]
    s.poly(circ, BLUE, 1.8, fill='#c9d8ee', close=True, op=0.9)
    p.axes_xy(xt=(2, 4), yt=(-2, 2))
    a = math.radians(32)
    rr = 4 * math.cos(a)
    s.arrow(p.X(0), p.Y(0), p.X(rr * math.cos(a)), p.Y(rr * math.sin(a)), RED, 1.5, 6)
    s.text(p.X(1.9), p.Y(1.55), 'r = 4 cos θ', 10, RED, font=MATH, style='italic')
    arc = [p.P(0.9 * math.cos(math.radians(k)), 0.9 * math.sin(math.radians(k))) for k in range(0, 33, 4)]
    s.poly(arc, RED, 1.1)
    s.text(p.X(1.15), p.Y(0.22), 'θ', 11, RED, font=MATH, style='italic')
    s.text(p.X(2.9), p.Y(-1.0), '(x − 2)² + y² = 4', 9.5, BLUE, font=MATH, style='italic')
    s.save('cdi-q4')


if __name__ == '__main__':
    fig_newman()
    fig_qo_structs()
    fig_stats()
    fig_fisica()
    fig_cdi()
    print('figuras:', len(os.listdir(OUT)))
