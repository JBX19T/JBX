---
titulo: Estatística Básica — Resolução passo a passo
subtitulo: Prova Parcelar · 12 de Novembro de 2025 · Departamento de Geociência
instituicao: ISPTEC — Instituto Superior Politécnico de Tecnologias e Ciências
info: Curso=Engenharia de Petróleos|Turma=EPT3-T3|Docente=Augusto Lucubo (MSc.)|Conteúdo=Distribuição de frequências · Medidas descritivas
ficheiro: 03_Estatistica-Basica_Prova-Parcelar.pdf
rodape: Prova Parcelar · 12/11/2025
---

## Formulário e significado dos símbolos

| Fórmula | Nome |
|---|---|
| $A_T = x_{máx} - x_{mín}$ | Amplitude total |
| $k = 1 + 3,322\,\log_{10} n$ | Número de classes (regra de Sturges) |
| $h = \dfrac{A_T}{k}$ | Amplitude de classe |
| $x_i = \dfrac{l_i + L_i}{2}$ | Ponto médio da classe |
| $f_r = \dfrac{f_i}{n}$ | Frequência relativa |
| $\bar{x} = \dfrac{\sum f_i\,x_i}{n}$ | Média aritmética (dados agrupados) |
| $M_d = l_{Md} + \dfrac{\frac{n}{2} - F_{ant}}{f_{Md}}\cdot h$ | Mediana (dados agrupados) |
| $M_o = l_{Mo} + \dfrac{\Delta_1}{\Delta_1 + \Delta_2}\cdot h$ | Moda (fórmula de Czuber) |
| $s^2 = \dfrac{\sum f_i\,(x_i - \bar{x})^2}{n - 1}$ ; $s = \sqrt{s^2}$ | Variância e desvio padrão amostrais |
| $CV = \dfrac{s}{\bar{x}}\times 100\%$ | Coeficiente de variação |

<div class="simb">

**Significado dos símbolos**

- $n$ — número total de observações (aqui $n = 50$ poços)
- $x_{máx}$, $x_{mín}$ — maior e menor valor observado
- $A_T$ — amplitude total dos dados
- $k$ — número de classes
- $h$ — amplitude (largura) de cada classe
- $l_i$, $L_i$ — limite inferior e limite superior da classe $i$
- $x_i$ — ponto médio da classe $i$
- $f_i$ — frequência absoluta (n.º de poços na classe)
- $f_r$ — frequência relativa; $f_r\%$ em percentagem
- $F_i$ — frequência absoluta acumulada
- $\bar{x}$ — média aritmética
- $M_d$ — mediana; $l_{Md}$, $f_{Md}$ — limite inferior e frequência da classe mediana
- $F_{ant}$ — frequência acumulada da classe anterior à mediana
- $M_o$ — moda; $l_{Mo}$ — limite inferior da classe modal
- $\Delta_1$ — diferença entre a frequência da classe modal e a da classe anterior
- $\Delta_2$ — diferença entre a frequência da classe modal e a da classe seguinte
- $s^2$, $s$ — variância e desvio padrão
- $CV$ — coeficiente de variação (dispersão relativa)
- $\sum$ — somatório (soma de todas as classes)

</div>

## Questão 1 — Eficiência de Produção (E.P. %) de 50 poços

> A base de dados representa 50 poços de petróleo em produção. (a) Apresente a tabela de distribuição de frequência da variável Eficiência de Produção. (b) Calcule as medidas de tendência central e o coeficiente de variação. (c) Apresente o relatório analítico dos resultados obtidos.

**Tabela 1 — Valores observados da E.P. (%)**

| | | | | | | | | | |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| 87,5 | 81,2 | 74,0 | 90,1 | 79,5 | 85,3 | 70,8 | 86,2 | 80,6 | 88,0 |
| 75,4 | 85,9 | 79,8 | 89,2 | 73,6 | 86,7 | 90,5 | 82,4 | 74,8 | 85,0 |
| 80,2 | 71,4 | 87,1 | 80,8 | 88,4 | 73,9 | 86,0 | 89,5 | 79,9 | 74,5 |
| 84,0 | 81,0 | 91,0 | 76,0 | 85,0 | 82,5 | 89,0 | 74,0 | 83,0 | 79,0 |
| 91,5 | 75,0 | 86,0 | 80,0 | 88,5 | 76,0 | 83,5 | 79,2 | 90,0 | 75,5 |

### 1 a) Tabela de distribuição de frequências

**Passo 1 — Rol (dados por ordem crescente):**

70,8 · 71,4 · 73,6 · 73,9 · 74,0 · 74,0 · 74,5 · 74,8 · 75,0 · 75,4 · 75,5 · 76,0 · 76,0 · 79,0 · 79,2 · 79,5 · 79,8 · 79,9 · 80,0 · 80,2 · 80,6 · 80,8 · 81,0 · 81,2 · 82,4 · 82,5 · 83,0 · 83,5 · 84,0 · 85,0 · 85,0 · 85,3 · 85,9 · 86,0 · 86,0 · 86,2 · 86,7 · 87,1 · 87,5 · 88,0 · 88,4 · 88,5 · 89,0 · 89,2 · 89,5 · 90,0 · 90,1 · 90,5 · 91,0 · 91,5

**Passo 2 — Amplitude total:**

$$A_T = x_{máx} - x_{mín} = 91,5 - 70,8 = 20,7$$

**Passo 3 — Número de classes (regra de Sturges):**

$$k = 1 + 3,322\,\log_{10}(50) = 1 + 3,322 \times 1,699 = 6,64 \approx 7$$

Portanto, utilizaremos **7 classes**.

**Passo 4 — Amplitude de classe:**

$$h = \frac{A_T}{k} = \frac{20,7}{7} = 2,957 \;\;\Longrightarrow\;\; \boxed{h \approx 3}$$

(arredonda-se sempre **para cima**, para que o maior valor fique dentro da última classe).

**Passo 5 — Classes.** Começa-se no menor valor e soma-se $h = 3$: $70,8 \vdash 73,8$; $73,8 \vdash 76,8$; … ; $88,8 \vdash 91,8$. O símbolo $\vdash$ significa que o limite inferior **pertence** à classe e o superior **não** pertence.

**Passo 6 — Contagem e tabela:**

| Classe | E.P. (%) | $f_i$ | $x_i$ | $f_r$ | $f_r\%$ | $F_i$ | $F_r\%$ |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| 1 | $70,8 \vdash 73,8$ | 3 | 72,3 | 0,06 | 6 | 3 | 6 |
| 2 | $73,8 \vdash 76,8$ | 10 | 75,3 | 0,20 | 20 | 13 | 26 |
| 3 | $76,8 \vdash 79,8$ | 3 | 78,3 | 0,06 | 6 | 16 | 32 |
| 4 | $79,8 \vdash 82,8$ | 10 | 81,3 | 0,20 | 20 | 26 | 52 |
| 5 | $82,8 \vdash 85,8$ | 6 | 84,3 | 0,12 | 12 | 32 | 64 |
| 6 | $85,8 \vdash 88,8$ | 10 | 87,3 | 0,20 | 20 | 42 | 84 |
| 7 | $88,8 \vdash 91,8$ | 8 | 90,3 | 0,16 | 16 | 50 | 100 |
| **Total** | | **50** | | **1,00** | **100** | | |

{{fig:est-hist-ep}}

<div class="leg">Histograma e polígono de frequências da Eficiência de Produção</div>

### 1 b) Medidas de tendência central e coeficiente de variação

**Tabela auxiliar de cálculo** (com $\bar{x} = 82,38$, calculado a seguir):

| Classe | $f_i$ | $x_i$ | $f_i\,x_i$ | $x_i - \bar{x}$ | $(x_i - \bar{x})^2$ | $f_i\,(x_i - \bar{x})^2$ |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| $70,8 \vdash 73,8$ | 3 | 72,3 | 216,9 | −10,08 | 101,6064 | 304,82 |
| $73,8 \vdash 76,8$ | 10 | 75,3 | 753,0 | −7,08 | 50,1264 | 501,26 |
| $76,8 \vdash 79,8$ | 3 | 78,3 | 234,9 | −4,08 | 16,6464 | 49,94 |
| $79,8 \vdash 82,8$ | 10 | 81,3 | 813,0 | −1,08 | 1,1664 | 11,66 |
| $82,8 \vdash 85,8$ | 6 | 84,3 | 505,8 | 1,92 | 3,6864 | 22,12 |
| $85,8 \vdash 88,8$ | 10 | 87,3 | 873,0 | 4,92 | 24,2064 | 242,06 |
| $88,8 \vdash 91,8$ | 8 | 90,3 | 722,4 | 7,92 | 62,7264 | 501,81 |
| **Total** | **50** | | **4119,0** | | | **1633,68** |

#### Média aritmética

$$\bar{x} = \frac{\sum f_i\,x_i}{n} = \frac{4119,0}{50} \;\;\Longrightarrow\;\; \boxed{\bar{x} = 82,38\ \%}$$

#### Mediana

**Passo 1 — Posição:** $\dfrac{n}{2} = \dfrac{50}{2} = 25$. A primeira classe cuja frequência acumulada atinge 25 é a 4.ª ($F_4 = 26$): classe mediana $79,8 \vdash 82,8$.

**Passo 2 — Fórmula** ($l_{Md} = 79,8$; $F_{ant} = 16$; $f_{Md} = 10$; $h = 3$):

$$M_d = 79,8 + \frac{25 - 16}{10}\times 3 = 79,8 + 2,7 \;\;\Longrightarrow\;\; \boxed{M_d = 82,5\ \%}$$

#### Moda

A maior frequência ($f_i = 10$) aparece em **três classes** (2.ª, 4.ª e 6.ª), por isso a distribuição é **multimodal (trimodal)**. Aplicando a fórmula de Czuber a cada classe modal:

$$M_{o1} = 73,8 + \frac{10 - 3}{(10 - 3) + (10 - 3)}\times 3 = 73,8 + \frac{7}{14}\times 3 = \boxed{75,3\ \%}$$

$$M_{o2} = 79,8 + \frac{10 - 3}{(10 - 3) + (10 - 6)}\times 3 = 79,8 + \frac{7}{11}\times 3 = \boxed{81,7\ \%}$$

$$M_{o3} = 85,8 + \frac{10 - 6}{(10 - 6) + (10 - 8)}\times 3 = 85,8 + \frac{4}{6}\times 3 = \boxed{87,8\ \%}$$

#### Variância, desvio padrão e coeficiente de variação

$$s^2 = \frac{\sum f_i\,(x_i - \bar{x})^2}{n - 1} = \frac{1633,68}{49} = 33,34\ (\%)^2$$

$$s = \sqrt{33,34} \;\;\Longrightarrow\;\; \boxed{s = 5,77\ \%}$$

$$CV = \frac{s}{\bar{x}}\times 100 = \frac{5,77}{82,38}\times 100 \;\;\Longrightarrow\;\; \boxed{CV = 7,0\ \%}$$

<div class="nota">

**Nota:** se o professor usar a fórmula populacional (dividir por $n$ em vez de $n-1$), obtém-se $\sigma^2 = 1633,68/50 = 32,67$; $\sigma = 5,72$ e $CV = 6,9\%$ — a conclusão é a mesma. Interpretação habitual do $CV$: até 15% → baixa dispersão (dados homogéneos); de 15% a 30% → média dispersão; acima de 30% → alta dispersão (dados heterogéneos).

</div>

<div class="resp">

**Resumo das medidas (E.P.):** $\bar{x} = 82,38\%$ · $M_d = 82,5\%$ · $M_o = 75,3\%;\ 81,7\%;\ 87,8\%$ (trimodal) · $s = 5,77\%$ · $CV = 7,0\%$

</div>

### 1 c) Relatório analítico

Para a interpretação usam-se as faixas típicas dadas no enunciado:

| Classificação | Faixa de E.P. (%) | Interpretação | N.º de poços | % |
|---|:-:|---|:-:|:-:|
| Excelente | 90 – 100 | Poço operando próximo ao potencial máximo | 5 | 10 |
| Boa | 80 – 90 | Pequenas perdas de desempenho | 27 | 54 |
| Regular | 70 – 80 | Restrições de escoamento ou baixa eficiência de elevação | 18 | 36 |
| Baixa | 60 – 70 | Necessidade de intervenção ou optimização | 0 | 0 |
| Crítica | < 60 | Problemas severos de escoamento ou bombeio | 0 | 0 |

(Contagem feita no rol: 18 valores abaixo de 80; 27 valores de 80,0 a 89,5; 5 valores de 90,0 a 91,5.)

<div class="resp">

**Relatório**

Foram analisados **50 poços** em produção da mesma bacia sedimentar. A eficiência de produção variou entre **70,8% e 91,5%** (amplitude total de 20,7 pontos percentuais) e os dados foram organizados em 7 classes de amplitude 3.

**Tendência central.** A eficiência média é **82,38%** e a mediana é **82,5%**: metade dos poços opera abaixo de 82,5% e a outra metade acima. Como a média e a mediana praticamente coincidem, a distribuição é aproximadamente **simétrica** e a média representa bem o conjunto. Pelas faixas típicas, o campo situa-se, em média, na classificação **«Boa»** (80–90%), isto é, com pequenas perdas de desempenho.

**Forma da distribuição.** Existem três classes com a mesma frequência máxima (10 poços), em torno de 75,3%, 81,7% e 87,8%. A distribuição é **trimodal**, o que sugere três subgrupos de poços com comportamentos distintos — coerente com o facto de estarem localizados em blocos diferentes da bacia.

**Dispersão.** O desvio padrão é 5,77% e o coeficiente de variação é **7,0%** (inferior a 15%). A dispersão é **baixa**: os poços são **homogéneos** quanto à eficiência.

**Classificação operacional.** 10% dos poços são «Excelentes», 54% «Bons» e 36% «Regulares»; nenhum poço está nas faixas «Baixa» ou «Crítica». Ou seja, 64% dos poços têm eficiência igual ou superior a 80%.

**Conclusão e recomendação.** O desempenho global do campo é bom e estável, sem poços que exijam intervenção urgente. As oportunidades de optimização concentram-se nos **18 poços «Regulares»** (70–80%), em especial os 13 poços abaixo de 76,8%, nos quais se deve investigar restrições de escoamento ou baixa eficiência do sistema de elevação.

</div>

## Questão 2 — Histograma da Taxa de Produção (TP)

> Com base no histograma da Taxa de produção, proceda à análise que se impõe, comparando-o com a Eficiência de produção.

{{fig:est-hist-tp}}

<div class="leg">Histograma da Taxa de produção (reprodução do enunciado)</div>

**Passo 1 — Ler o histograma e montar a tabela** ($h = 757 - 640 = 117$ bpd; $n = 11 + 2 + 13 + 0 + 11 + 13 = 50$):

| TP (bpd) | $f_i$ | $x_i$ | $f_r\%$ | $F_i$ | $f_i\,x_i$ | $f_i\,(x_i - \bar{x})^2$ |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| $640 \vdash 757$ | 11 | 698,5 | 22 | 11 | 7683,5 | 1 130 486,9 |
| $757 \vdash 874$ | 2 | 815,5 | 4 | 13 | 1631,0 | 82 889,6 |
| $874 \vdash 991$ | 13 | 932,5 | 26 | 26 | 12 122,5 | 97 449,3 |
| $991 \vdash 1108$ | 0 | 1049,5 | 0 | 26 | 0 | 0 |
| $1108 \vdash 1225$ | 11 | 1166,5 | 22 | 37 | 12 831,5 | 239 059,2 |
| $1225 \vdash 1342$ | 13 | 1283,5 | 26 | 50 | 16 685,5 | 908 933,2 |
| **Total** | **50** | | **100** | | **50 954,0** | **2 458 818,2** |

**Passo 2 — Média:**

$$\bar{x} = \frac{\sum f_i\,x_i}{n} = \frac{50\,954}{50} = \boxed{1019,1\ \text{bpd}}$$

**Passo 3 — Mediana** ($n/2 = 25$ → classe $874 \vdash 991$, com $F_{ant} = 13$ e $f_{Md} = 13$):

$$M_d = 874 + \frac{25 - 13}{13}\times 117 = 874 + 108 = \boxed{982\ \text{bpd}}$$

**Passo 4 — Moda.** Há duas classes com frequência máxima (13): a distribuição é **bimodal**.

$$M_{o1} = 874 + \frac{13 - 2}{(13 - 2) + (13 - 0)}\times 117 = 874 + \frac{11}{24}\times 117 = \boxed{927,6\ \text{bpd}}$$

$$M_{o2} = 1225 + \frac{13 - 11}{(13 - 11) + (13 - 0)}\times 117 = 1225 + \frac{2}{15}\times 117 = \boxed{1240,6\ \text{bpd}}$$

**Passo 5 — Desvio padrão e coeficiente de variação:**

$$s = \sqrt{\frac{\sum f_i\,(x_i - \bar{x})^2}{n - 1}} = \sqrt{\frac{2\,458\,818,2}{49}} = \sqrt{50\,180} = \boxed{224,0\ \text{bpd}}$$

$$CV = \frac{s}{\bar{x}}\times 100 = \frac{224,0}{1019,1}\times 100 = \boxed{22,0\ \%}$$

**Passo 6 — Comparação com a Eficiência de Produção:**

| Medida | E.P. (%) | TP (bpd) |
|---|:-:|:-:|
| Média | 82,38 | 1019,1 |
| Mediana | 82,5 | 982 |
| Moda | 75,3 · 81,7 · 87,8 (trimodal) | 927,6 · 1240,6 (bimodal) |
| Desvio padrão | 5,77 | 224,0 |
| Coeficiente de variação | 7,0% (baixa dispersão) | 22,0% (média dispersão) |
| Forma | Aproximadamente simétrica, sem classes vazias | Irregular, com «vazios» (classes com 0 e 2 poços) |

<div class="resp">

**Análise**

**Forma.** O histograma da TP é **irregular e multimodal**: as frequências sobem e descem alternadamente (11 – 2 – 13 – 0 – 11 – 13) e existe uma classe **vazia** ($991 \vdash 1108$ bpd) e outra quase vazia ($757 \vdash 874$ bpd). Isto revela **grupos distintos de poços**: baixa produção (640–757 bpd; 11 poços, 22%), produção intermédia (874–991 bpd; 13 poços, 26%) e alta produção (1108–1342 bpd; 24 poços, 48%).

**Tendência central.** A média é 1019 bpd e a mediana 982 bpd. A média cai precisamente na classe onde **não existe nenhum poço**, logo **não é representativa** de um poço típico; a descrição por grupos (ou pelas modas 928 e 1241 bpd) é mais adequada.

**Dispersão.** O coeficiente de variação da TP é **22%** (média dispersão), cerca de **três vezes maior** do que o da E.P. (7%). Em termos relativos, a taxa de produção é muito mais variável do que a eficiência.

**Comparação e conclusão.** Os poços são **homogéneos na eficiência** (todos entre 70,8% e 91,5%, classificação média «Boa»), mas **heterogéneos na taxa de produção**. Como poços com eficiências semelhantes produzem volumes muito diferentes, as diferenças de produção não se explicam só pela eficiência: dependem de outros factores, como a profundidade, as características do reservatório e o bloco em que o poço se encontra. A optimização deve, portanto, ser estudada **por grupo de poços**, dando prioridade ao grupo de baixa produção (640–757 bpd). Para quantificar a relação entre as duas variáveis seria necessário um estudo de **correlação** com os pares de valores (E.P.; TP) de cada poço.

</div>
