---
titulo: Cálculo Diferencial e Integral III — Resolução passo a passo
subtitulo: 1.ª Prova Parcelar · 2 de Dezembro de 2025
instituicao: ISPTEC — Instituto Superior Politécnico de Tecnologias e Ciências
info: Curso=Engenharia de Petróleos|Docente=Valter Tomé|Duração=90 minutos|Conteúdo=Integrais duplos e triplos
ficheiro: 04_Calculo-Diferencial-e-Integral-III_Prova-Parcelar.pdf
rodape: 1.ª Prova Parcelar · 02/12/2025
---

## Formulário e significado dos símbolos

| Fórmula | Nome / uso |
|---|---|
| $\displaystyle\iint_D f\,dA = \int_a^b\!\int_{g_1(x)}^{g_2(x)} f\,dy\,dx = \int_c^d\!\int_{h_1(y)}^{h_2(y)} f\,dx\,dy$ | Teorema de Fubini (a ordem pode trocar-se) |
| $x = r\cos\theta$, $y = r\sin\theta$, $dA = r\,dr\,d\theta$ | Mudança para coordenadas polares |
| $x^2 + y^2 = r^2$ | Relação entre cartesianas e polares |
| $V = \displaystyle\iint_D \big(z_{sup} - z_{inf}\big)\,dA$ | Volume entre duas superfícies |
| $M = \displaystyle\iint_D \rho(x,y)\,dA$ | Massa de uma lâmina com densidade $\rho$ |
| $\displaystyle\int \cos^4\theta\,d\theta$ via $\cos^2\theta = \dfrac{1+\cos 2\theta}{2}$ | Potências de cosseno |
| $\displaystyle\int z^3 e^{z^4}\,dz = \dfrac{e^{z^4}}{4} + C$ | Substituição $u = z^4$ |

<div class="simb">

**Significado dos símbolos**

- $D$ — região de integração no plano $xy$
- $f(x,y)$ — função integranda; $dA$ — elemento de área
- $\iint_D$ — integral duplo sobre a região $D$
- $r$ — distância à origem (coordenada polar); $\theta$ — ângulo medido a partir do eixo $+x$
- $z_{sup}$, $z_{inf}$ — superfícies que limitam o sólido por cima e por baixo
- $V$ — volume; $M$ — massa
- $\rho(x,y)$ — densidade superficial (massa por unidade de área)
- $W$ — sólido do espaço
- $\ln$ — logaritmo natural; $e$ — número de Neper

</div>

## Questão 1 — Inverter a ordem de integração

> Inverta a ordem de integração e calcule o integral. Esboce a região de integração.
> $$\int_{-2}^{0}\!\int_{0}^{4-x^2} \frac{6x\cos(3y)}{4-y}\,dy\,dx$$

**Passo 1 — Identificar a região.** Pelos limites: $-2 \le x \le 0$ e $0 \le y \le 4 - x^2$. É a zona abaixo da parábola $y = 4 - x^2$, acima do eixo $x$, à esquerda do eixo $y$.

{{fig:cdi-q1}}

**Passo 2 — Porquê inverter?** Integrar $\dfrac{\cos 3y}{4-y}$ em ordem a $y$ não tem primitiva elementar; já em ordem a $x$ a função é um simples polinómio ($6x$).

**Passo 3 — Novos limites.** Fixando $y$ entre 0 e 4: $y = 4 - x^2 \Rightarrow x^2 = 4 - y \Rightarrow x = -\sqrt{4-y}$ (ramo com $x \le 0$). Logo $x$ vai de $-\sqrt{4-y}$ até $0$:

$$\int_{0}^{4}\!\int_{-\sqrt{4-y}}^{0} \frac{6x\cos(3y)}{4-y}\,dx\,dy$$

**Passo 4 — Integral interior (em $x$):**

$$\int_{-\sqrt{4-y}}^{0} 6x\,dx = \Big[3x^2\Big]_{-\sqrt{4-y}}^{0} = 0 - 3(4-y) = -3(4-y)$$

**Passo 5 — Substituir e simplificar** (o factor $4-y$ cancela):

$$\int_0^4 \frac{-3(4-y)\cos(3y)}{4-y}\,dy = \int_0^4 -3\cos(3y)\,dy$$

**Passo 6 — Integral exterior:**

$$\Big[-\sin(3y)\Big]_0^4 = -\sin(12) + \sin(0) = -\sin(12)$$

Com $12$ rad (calculadora em radianos): $\sin 12 = -0,5366$.

<div class="resp">

**Resposta:** $\displaystyle\int_{0}^{4}\!\int_{-\sqrt{4-y}}^{0} \dfrac{6x\cos(3y)}{4-y}\,dx\,dy = -\sin 12 \approx \mathbf{0,5366}$

</div>

## Questão 2 — Mudança de variáveis (coordenadas polares)

> Calcule, utilizando uma mudança de variáveis apropriada, o integral
> $$\int_{-6}^{0}\!\int_{0}^{\sqrt{36-x^2}} \frac{(x^2+y^2)^{-1/2}}{\sqrt{36-x^2-y^2}}\,dy\,dx$$

**Passo 1 — Região.** $-6 \le x \le 0$ e $0 \le y \le \sqrt{36 - x^2}$: é o **quarto de círculo** de raio 6 situado no 2.º quadrante ($x \le 0$, $y \ge 0$). Os termos $x^2+y^2$ sugerem coordenadas polares.

{{fig:cdi-q2}}

**Passo 2 — Novos limites:** $0 \le r \le 6$ e $\dfrac{\pi}{2} \le \theta \le \pi$.

**Passo 3 — Reescrever o integral** ($x^2 + y^2 = r^2$ e $dA = r\,dr\,d\theta$):

$$\int_{\pi/2}^{\pi}\!\int_0^6 \frac{(r^2)^{-1/2}}{\sqrt{36 - r^2}}\;r\,dr\,d\theta = \int_{\pi/2}^{\pi}\!\int_0^6 \frac{1}{r}\cdot\frac{r}{\sqrt{36 - r^2}}\,dr\,d\theta = \int_{\pi/2}^{\pi}\!\int_0^6 \frac{dr}{\sqrt{36 - r^2}}\,d\theta$$

**Passo 4 — Integral em $r$** (primitiva de $\dfrac{1}{\sqrt{a^2 - r^2}}$ é $\arcsin\dfrac{r}{a}$, com $a = 6$):

$$\int_0^6 \frac{dr}{\sqrt{36 - r^2}} = \Big[\arcsin\frac{r}{6}\Big]_0^6 = \arcsin 1 - \arcsin 0 = \frac{\pi}{2}$$

**Passo 5 — Integral em $\theta$:**

$$\int_{\pi/2}^{\pi} \frac{\pi}{2}\,d\theta = \frac{\pi}{2}\left(\pi - \frac{\pi}{2}\right) = \frac{\pi^2}{4}$$

<div class="resp">

**Resposta:** $\dfrac{\pi^2}{4} \approx \mathbf{2,467}$

</div>

## Questão 3 — Volume com integral duplo

> Calcule, usando integral duplo, o volume do sólido $W$, limitado superiormente pela semiesfera $z = \sqrt{8 - x^2 - y^2}$ e inferiormente pelo cone $z = \sqrt{x^2 + y^2}$.

**Passo 1 — Curva de intersecção.** Igualando as duas superfícies:

$$\sqrt{8 - x^2 - y^2} = \sqrt{x^2 + y^2} \;\Longrightarrow\; 8 - r^2 = r^2 \;\Longrightarrow\; r^2 = 4 \;\Longrightarrow\; r = 2$$

A projecção do sólido no plano $xy$ é o **disco** $D: x^2 + y^2 \le 4$ (em polares: $0 \le r \le 2$, $0 \le \theta \le 2\pi$). A figura mostra um corte do sólido pelo plano $r$–$z$.

{{fig:cdi-q3}}

**Passo 2 — Volume** ($z_{sup} - z_{inf}$, com $dA = r\,dr\,d\theta$):

$$V = \iint_D \Big(\sqrt{8 - x^2 - y^2} - \sqrt{x^2 + y^2}\Big)dA = \int_0^{2\pi}\!\int_0^2 \big(\sqrt{8 - r^2} - r\big)\,r\,dr\,d\theta$$

**Passo 3 — Integral em $r$.** Primitivas: $\displaystyle\int r\sqrt{8 - r^2}\,dr = -\tfrac13(8 - r^2)^{3/2}$ (substituição $u = 8 - r^2$) e $\displaystyle\int r^2\,dr = \tfrac{r^3}{3}$:

$$\int_0^2 \big(r\sqrt{8 - r^2} - r^2\big)dr = \Big[-\tfrac13(8 - r^2)^{3/2} - \tfrac{r^3}{3}\Big]_0^2$$

$$= \left(-\tfrac13\cdot 4^{3/2} - \tfrac83\right) - \left(-\tfrac13\cdot 8^{3/2}\right) = -\tfrac83 - \tfrac83 + \tfrac{16\sqrt2}{3} = \frac{16\sqrt2 - 16}{3}$$

**Passo 4 — Integral em $\theta$:**

$$V = 2\pi \cdot \frac{16(\sqrt2 - 1)}{3}$$

<div class="resp">

**Resposta:** $V = \dfrac{32\pi\,(\sqrt{2} - 1)}{3} \approx \mathbf{13,88}$ unidades de volume

</div>

## Questão 4 — Massa de uma lâmina circular

> Uma lâmina tem forma circular $x^2 + y^2 = 4x$ e tem densidade em cada ponto igual ao quadrado da distância até à origem. Calcule a massa.

**Passo 1 — Região.** Completando o quadrado: $x^2 - 4x + y^2 = 0 \Rightarrow (x - 2)^2 + y^2 = 4$, um disco de centro $(2; 0)$ e raio 2, que passa pela origem.

{{fig:cdi-q4}}

**Passo 2 — Densidade.** $\rho(x,y) = (\text{distância à origem})^2 = x^2 + y^2 = r^2$.

**Passo 3 — Fronteira em polares.** $x^2 + y^2 = 4x \Rightarrow r^2 = 4r\cos\theta \Rightarrow r = 4\cos\theta$. Para varrer o disco: $-\dfrac{\pi}{2} \le \theta \le \dfrac{\pi}{2}$ e $0 \le r \le 4\cos\theta$.

**Passo 4 — Massa:**

$$M = \iint_D \rho\,dA = \int_{-\pi/2}^{\pi/2}\!\int_0^{4\cos\theta} r^2\cdot r\,dr\,d\theta = \int_{-\pi/2}^{\pi/2} \frac{(4\cos\theta)^4}{4}\,d\theta = 64\int_{-\pi/2}^{\pi/2} \cos^4\theta\,d\theta$$

**Passo 5 — Potência de cosseno.** Usando $\cos^2\theta = \dfrac{1 + \cos 2\theta}{2}$:

$$\cos^4\theta = \frac{1 + 2\cos 2\theta + \cos^2 2\theta}{4} = \frac{3}{8} + \frac{\cos 2\theta}{2} + \frac{\cos 4\theta}{8}$$

$$\int_{-\pi/2}^{\pi/2} \cos^4\theta\,d\theta = \left[\frac{3\theta}{8} + \frac{\sin 2\theta}{4} + \frac{\sin 4\theta}{32}\right]_{-\pi/2}^{\pi/2} = \frac{3}{8}\cdot\pi = \frac{3\pi}{8}$$

(os termos com seno anulam-se nos limites)

**Passo 6 — Resultado:**

$$M = 64 \times \frac{3\pi}{8} = 24\pi$$

<div class="resp">

**Resposta:** $M = 24\pi \approx \mathbf{75,40}$ unidades de massa

</div>

## Questão 5 — Integral triplo

> Calcule o integral triplo
> $$\int_{1}^{3}\!\int_{0}^{3x}\!\int_{0}^{\sqrt[4]{\ln(36xy^3 + 45y^4 + 1)}} z^3\,e^{z^4}\,dz\,dy\,dx$$

**Passo 1 — Integral mais interior (em $z$).** Substituição $u = z^4$, $du = 4z^3\,dz$:

$$\int z^3 e^{z^4}\,dz = \frac{e^{z^4}}{4}$$

Nos limites, com $z_1 = \sqrt[4]{\ln(36xy^3 + 45y^4 + 1)}$, tem-se $z_1^4 = \ln(36xy^3 + 45y^4 + 1)$ e $e^{z_1^4} = 36xy^3 + 45y^4 + 1$:

$$\left[\frac{e^{z^4}}{4}\right]_0^{z_1} = \frac{(36xy^3 + 45y^4 + 1) - 1}{4} = 9xy^3 + \frac{45}{4}y^4$$

**Passo 2 — Integral em $y$** (de $0$ a $3x$; $x$ é constante):

$$\int_0^{3x}\!\left(9xy^3 + \frac{45}{4}y^4\right)dy = 9x\cdot\frac{(3x)^4}{4} + \frac{45}{4}\cdot\frac{(3x)^5}{5} = \frac{729}{4}x^5 + \frac{2187}{4}x^5 = \frac{2916}{4}x^5 = 729\,x^5$$

**Passo 3 — Integral em $x$:**

$$\int_1^3 729\,x^5\,dx = 729\left[\frac{x^6}{6}\right]_1^3 = \frac{729\,(729 - 1)}{6} = \frac{729 \times 728}{6} = 88\,452$$

<div class="resp">

**Resposta:** $\mathbf{88\,452}$

</div>

<div class="nota">

**Nota sobre a leitura do enunciado:** na foto, o limite superior de $z$ é lido como $\sqrt[4]{\ln(36xy^3 + 45y^4 + 1)}$. Esta leitura é a que faz o integral «fechar» de forma exacta, pois $e^{z^4}$ cancela o logaritmo.

</div>

<div class="resp">

**Resumo das respostas:** 1) $-\sin 12 \approx 0,5366$ · 2) $\pi^2/4$ · 3) $\dfrac{32\pi(\sqrt2 - 1)}{3}$ · 4) $24\pi$ · 5) $88\,452$

</div>
