# Petisqueira Bar Dourada — Menu

Menu digital (`index.html`) desenhado como ferramenta de venda, seguindo a
estratégia de venda persuasiva definida para a marca: hierarquia visual,
descrições gastronómicas, produtos-âncora, microcopy de cross-selling e
identidade premium dourado/preto alinhada com o logótipo.

Abrir `index.html` num navegador para visualizar o menu.

## Conteúdo e fontes

- **Para Começar**, **Sabores da Casa** e **Para Refrescar / Para Brindar**:
  transcritos do menu atual da casa ("MENU BAR PETISCARIA DOURADA").
- **As Nossas Pizzas**: transcrito do menu de pizzas fotografado (preços
  Grande/Média).
- **Especial da Noite**: conteúdo do menu "Plano JC" (evento Heavy C),
  reenquadrado como secção fixa da casa. Confirmar com a equipa se estes
  pratos e preços devem manter-se permanentes no menu ou se eram exclusivos
  daquele evento pontual — a data e o local originais do evento não foram
  incluídos por já não se aplicarem.

## Folha dedicada "As Nossas Pizzas" (`pizzas.html` / `pizzas.pdf`)

Peça separada, em formato editorial premium, seguindo o esboço de estrutura
diagonal fornecido: módulos que alternam foto em cima/informação em baixo e
informação em cima/foto em baixo, com costura diagonal entre os dois blocos
de cada módulo. Preços por Mini/Pequena/Média/Grande conforme tabela
fornecida.

**As fotografias das pizzas ainda não foram inseridas.** Tentei obtê-las a
partir da internet (Unsplash, Wikimedia Commons, Pinterest), mas a política
de rede desta sessão bloqueou os três domínios — não é algo que dê para
contornar a partir daqui. Cada módulo tem um espaço reservado com moldura
dourada e a etiqueta "Fotografia a inserir". Para adicionar uma foto,
preencher o atributo `src` do `<img>` correspondente (ex.:
`src="assets/img/pizzas/margarida.jpg"`); a etiqueta de placeholder
desaparece automaticamente assim que houver uma imagem.

## Pontos a confirmar com a equipa

- **Etiquetas de destaque** (Mais Pedido, Favorito da Casa, Recomendado):
  os estilos já existem no CSS, mas só foram aplicados a "Para Partilhar",
  "Ideal para 2" e "Especial da Casa"/"Experiência Dourada", que decorrem
  logicamente do tamanho ou preço do prato. As restantes etiquetas devem ser
  atribuídas pela equipa com base em dados reais de vendas.
- Não foram incluídos morada/telefone/redes sociais da Petisqueira Bar
  Dourada por não terem sido fornecidos (o contacto visível numa das fotos
  pertence a outro estabelecimento).
