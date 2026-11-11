---
titulo: Física Geral II — Resolução passo a passo
subtitulo: 1.ª Prova Parcelar (11/2025) · Prova de Consolidação II: Ondas Mecânicas
instituicao: ISPTEC — Instituto Superior Politécnico de Tecnologias e Ciências
info: Curso=Engenharia de Petróleos|Docente=João Vicente|Semestre=1.º Semestre|Conteúdo=MHS · Ondas · Efeito Doppler · Electrostática
ficheiro: 02_Fisica-Geral-II_Prova-Parcelar-e-Consolidacao.pdf
rodape: 1.ª Prova Parcelar · 11/2025
---

## Formulário (dado na prova) e significado dos símbolos

| Fórmula | Nome |
|---|---|
| $x(t) = A\cos(\omega t + \varphi_0)$ | Posição no Movimento Harmónico Simples (MHS) |
| $\omega = \dfrac{2\pi}{T} = 2\pi f$ | Frequência angular |
| $v_{máx} = \omega A$ ; $a_{máx} = \omega^2 A$ | Velocidade e aceleração máximas no MHS |
| $v = \sqrt{\dfrac{T}{\mu}}$ ; $\mu = \dfrac{m}{L}$ | Velocidade de uma onda numa corda |
| $\lambda_n = \dfrac{2L}{n}$ ; $f_n = \dfrac{n\,v}{2L}$ | Ondas estacionárias em corda fixa nas duas pontas |
| $P = \tfrac{1}{2}\,\mu\,v\,A^2\omega^2$ | Potência média transportada por uma onda na corda |
| $f_o = f_f\left(\dfrac{v \pm v_o}{v \mp v_f}\right)$ | Efeito Doppler |
| $v = \lambda f$ | Relação fundamental das ondas |
| $\vec{E} = k\,\dfrac{q}{r^2}\,\hat{r}$ ; $\vec{F} = k\,\dfrac{q_1q_2}{r^2}\,\hat{r}$ | Campo eléctrico e Lei de Coulomb |

<div class="simb">

**Significado dos símbolos**

- $x$ — deslocamento/posição (m)
- $A$ — amplitude: deslocamento máximo (m)
- $\omega$ — frequência angular (rad/s)
- $\varphi_0$ — fase inicial (rad)
- $T$ — período (s) no MHS; **tracção** (N) na corda
- $f$ — frequência (Hz)
- $v$ — velocidade de propagação da onda (m/s)
- $\mu$ — densidade linear de massa da corda (kg/m)
- $m$, $L$ — massa (kg) e comprimento (m) da corda
- $\lambda$ — comprimento de onda (m)
- $n$ — modo harmónico (n.º de ventres)
- $N_{nós}$ — número de nós
- $P$ — potência média (W)
- $f_f$, $f_o$ — frequência emitida pela fonte e recebida pelo observador
- $v_f$, $v_o$ — velocidades da fonte e do observador (m/s)
- $k = \dfrac{1}{4\pi\varepsilon_0} = 9\times10^9$ N·m²/C² — constante de Coulomb
- $\varepsilon_0 = 8,85\times10^{-12}$ F/m — permitividade do vácuo
- $q$ — carga eléctrica (C); $1\ \mu\text{C} = 10^{-6}$ C
- $r$ — distância entre a carga e o ponto (m)
- $\hat{r}$ — vector unitário que aponta da carga para o ponto
- $\vec{E}$ — campo eléctrico (N/C); $\vec{F}$ — força eléctrica (N)

</div>

## Questão 1 — Movimento Harmónico Simples

> O gráfico representa o deslocamento de uma partícula em função do tempo durante um MHS. A curva é descrita por uma função do tipo cosseno.
> (a) Escreva a função horária da posição $x(t)$, velocidade $v(t)$ e aceleração $a(t)$;
> (b) Indique dois instantes em que a partícula atinge o deslocamento máximo positivo e dois instantes para o máximo negativo;
> (c) Calcule $v_{máx}$ e $a_{máx}$.

<div class="dados">

**Dados lidos no gráfico:** amplitude $A = 0,10\ \text{m}$ · posição inicial $x_0 = x(0) = 0,05\ \text{m}$ · período $T = 2\ \text{s}$ (a curva repete-se de 2 em 2 s) · em $t=0$ a curva está a **descer** (velocidade negativa)

</div>

{{fig:fis-mhs}}

### 1 a) Funções $x(t)$, $v(t)$ e $a(t)$

**Passo 1 — Frequência angular:**

$$\omega = \frac{2\pi}{T} = \frac{2\pi}{2} = \pi\ \text{rad/s}$$

**Passo 2 — Fase inicial.** Em $t = 0$: $x_0 = A\cos\varphi_0$, logo

$$\cos\varphi_0 = \frac{x_0}{A} = \frac{0,05}{0,10} = 0,5 \;\;\Longrightarrow\;\; \varphi_0 = \pm\frac{\pi}{3}\ \text{rad}$$

Como em $t=0$ a partícula se move no sentido negativo ($v(0) = -\omega A\sin\varphi_0 < 0$), tem de ser $\sin\varphi_0 > 0$, portanto $\varphi_0 = +\dfrac{\pi}{3}$ rad.

**Passo 3 — Posição:**

$$\boxed{x(t) = 0,10\cos\!\left(\pi t + \frac{\pi}{3}\right)\ \text{(m)}}$$

**Passo 4 — Velocidade** (derivada da posição, $v = dx/dt = -\omega A\sin(\omega t + \varphi_0)$):

$$\boxed{v(t) = -0,10\,\pi\,\sin\!\left(\pi t + \frac{\pi}{3}\right) \approx -0,314\,\sin\!\left(\pi t + \frac{\pi}{3}\right)\ \text{(m/s)}}$$

**Passo 5 — Aceleração** (derivada da velocidade, $a = dv/dt = -\omega^2 A\cos(\omega t + \varphi_0) = -\omega^2 x$):

$$\boxed{a(t) = -0,10\,\pi^2\cos\!\left(\pi t + \frac{\pi}{3}\right) \approx -0,987\cos\!\left(\pi t + \frac{\pi}{3}\right)\ \text{(m/s}^2)}$$

### 1 b) Instantes de deslocamento máximo

**Máximo positivo** ($x = +A$) — acontece quando $\cos(\pi t + \varphi_0) = 1$:

$$\pi t + \frac{\pi}{3} = 2\pi n \;\;\Longrightarrow\;\; t = 2n - \frac{1}{3} \qquad (n = 1, 2, 3, \dots)$$

$$n = 1:\; \boxed{t_1 = 1,67\ \text{s}} \qquad\qquad n = 2:\; \boxed{t_2 = 3,67\ \text{s}}$$

**Máximo negativo** ($x = -A$) — acontece quando $\cos(\pi t + \varphi_0) = -1$:

$$\pi t + \frac{\pi}{3} = (2n + 1)\pi \;\;\Longrightarrow\;\; t = 2n + \frac{2}{3} \qquad (n = 0, 1, 2, \dots)$$

$$n = 0:\; \boxed{t_1 = 0,67\ \text{s}} \qquad\qquad n = 1:\; \boxed{t_2 = 2,67\ \text{s}}$$

(Confere com o gráfico: mínimo perto de 0,67 s e máximo perto de 1,67 s.)

### 1 c) Velocidade e aceleração máximas

$$v_{máx} = \omega A = \pi \times 0,10 = \boxed{0,314\ \text{m/s}}$$

$$a_{máx} = \omega^2 A = \pi^2 \times 0,10 = \boxed{0,987\ \text{m/s}^2}$$

<div class="simb">

**Significado dos símbolos**

- $x_0$ — posição no instante $t=0$
- $n$ — número inteiro (cada valor dá um instante diferente)
- $v_{máx}$ — velocidade máxima (ocorre ao passar em $x=0$)
- $a_{máx}$ — aceleração máxima (ocorre nos extremos $x=\pm A$)

</div>

## Questão 2 — Ondas estacionárias numa corda

> Uma corda de 120 cm, fixa nas duas extremidades, é posta a vibrar por um excitador mecânico. Em determinado ajuste, surgem **5 nós** ao longo da corda (incluindo os das extremidades). Determine:
> (a) o modo harmónico $n$ e o comprimento de onda em função de $n$ e de $N_{nós}$;
> (b) a velocidade de propagação da onda, sabendo que $m = 15$ g e $T = 45$ N, e a frequência de ressonância para o modo encontrado;
> (c) a potência transportada pela onda se a amplitude é $A = 1,5$ cm;
> (d) esboce o perfil da onda estacionária e mostre a posição $x$ de cada nó em função de $\lambda$.

<div class="dados">

**Dados:** $L = 120\ \text{cm} = 1,20\ \text{m}$ · $N_{nós} = 5$ · $m = 15\ \text{g} = 0,015\ \text{kg}$ · $T = 45\ \text{N}$ · $A = 1,5\ \text{cm} = 0,015\ \text{m}$

</div>

### 2 a) Modo harmónico e comprimento de onda

Numa corda fixa nas duas pontas, o modo $n$ tem $n$ ventres e $n+1$ nós:

$$N_{nós} = n + 1 \;\;\Longrightarrow\;\; n = N_{nós} - 1 = 5 - 1 = \boxed{4}$$

A corda tem de conter um número inteiro de meios comprimentos de onda, $L = n\,\dfrac{\lambda}{2}$:

$$\lambda = \frac{2L}{n} = \frac{2L}{N_{nós} - 1} = \frac{2 \times 1,20}{4} = \boxed{0,60\ \text{m}}$$

### 2 b) Velocidade e frequência de ressonância

**Passo 1 — Densidade linear:**

$$\mu = \frac{m}{L} = \frac{0,015}{1,20} = 0,0125\ \text{kg/m}$$

**Passo 2 — Velocidade de propagação:**

$$v = \sqrt{\frac{T}{\mu}} = \sqrt{\frac{45}{0,0125}} = \sqrt{3600} = \boxed{60\ \text{m/s}}$$

**Passo 3 — Frequência do 4.º harmónico:**

$$f_n = \frac{n\,v}{2L} \;\;\Longrightarrow\;\; f_4 = \frac{4 \times 60}{2 \times 1,20} = \boxed{100\ \text{Hz}}$$

(o mesmo que $f = v/\lambda = 60/0,60 = 100$ Hz)

### 2 c) Potência transportada

**Passo 1 — Frequência angular:** $\omega = 2\pi f = 2\pi \times 100 = 628,3\ \text{rad/s}$

**Passo 2 — Potência média:**

$$P = \tfrac{1}{2}\,\mu\,v\,A^2\,\omega^2 = \tfrac{1}{2} \times 0,0125 \times 60 \times (0,015)^2 \times (628,3)^2$$

$$P = 0,375 \times 2,25\times10^{-4} \times 3,948\times10^{5} = \boxed{33,3\ \text{W}}$$

### 2 d) Perfil da onda estacionária e posição dos nós

Os nós ficam separados de meio comprimento de onda: $x_k = (k-1)\,\dfrac{\lambda}{2}$, com $k = 1, \dots, 5$.

{{fig:fis-corda}}

<div class="leg">N = nó (ponto que não vibra) · V = ventre (ponto de amplitude máxima)</div>

<div class="resp">

**Resposta:** a) $n = 4$ (4.º harmónico), $\lambda = \dfrac{2L}{N_{nós}-1} = 0,60$ m · b) $v = 60$ m/s e $f_4 = 100$ Hz · c) $P \approx 33,3$ W · d) nós em $x = 0;\ \dfrac{\lambda}{2};\ \lambda;\ \dfrac{3\lambda}{2};\ 2\lambda$ (ou seja 0; 0,30; 0,60; 0,90 e 1,20 m).

</div>

## Questão 3 — Efeito Doppler (estudo sísmico marinho)

> Uma fonte sísmica emite pulsos de som de frequência $f_f = 1500$ Hz enquanto se desloca a 6,0 m/s em direcção a uma plataforma estacionária de recepção (hidrofones). A velocidade do som na água é $v = 1500$ m/s.
> (a) Frequência percebida pelos hidrofones durante a aproximação;
> (b) os hidrofones movem-se a 3,0 m/s em direcção à fonte, que continua a 6,0 m/s;
> (c) o detector é um geofone no solo (arenitos saturados), onde a velocidade da onda é 2500 m/s;
> (d) comprimento de onda emitido e comprimento de onda percebido no caso da alínea (b).

<div class="dados">

**Dados:** $f_f = 1500\ \text{Hz}$ · $v_f = 6,0\ \text{m/s}$ · $v = 1500\ \text{m/s}$ (água) · b) $v_o = 3,0\ \text{m/s}$ · c) $v = 2500\ \text{m/s}$

</div>

**Fórmula geral e regra dos sinais:**

$$f_o = f_f\left(\frac{v \pm v_o}{v \mp v_f}\right)$$

- **Aproximação** → a frequência **aumenta**: usa-se $+v_o$ no numerador e $-v_f$ no denominador.
- **Afastamento** → a frequência **diminui**: usa-se $-v_o$ no numerador e $+v_f$ no denominador.

### 3 a) Fonte a aproximar-se, detector parado ($v_o = 0$)

$$f_o = f_f\left(\frac{v}{v - v_f}\right) = 1500 \times \frac{1500}{1500 - 6} = 1500 \times \frac{1500}{1494} = \boxed{1506,02\ \text{Hz}}$$

### 3 b) Fonte e detector a aproximarem-se um do outro

$$f_o = f_f\left(\frac{v + v_o}{v - v_f}\right) = 1500 \times \frac{1500 + 3}{1500 - 6} = 1500 \times \frac{1503}{1494} = \boxed{1509,04\ \text{Hz}}$$

### 3 c) Geofone no solo ($v = 2500$ m/s, $v_o = 0$)

$$f_o = f_f\left(\frac{v}{v - v_f}\right) = 1500 \times \frac{2500}{2500 - 6} = 1500 \times \frac{2500}{2494} = \boxed{1503,61\ \text{Hz}}$$

Quanto maior a velocidade de propagação no meio, menor é o efeito Doppler (a velocidade da fonte «pesa» menos face a $v$).

### 3 d) Comprimentos de onda

**Emitido** (fonte, $\lambda = v/f$):

$$\lambda_f = \frac{v}{f_f} = \frac{1500}{1500} = \boxed{1,00\ \text{m}}$$

**Percebido no caso (b):**

$$\lambda_o = \frac{v}{f_o} = \frac{1500}{1509,04} = \boxed{0,994\ \text{m}}$$

<div class="simb">

**Significado dos símbolos**

- $f_f$ — frequência emitida pela fonte
- $f_o$ — frequência percebida pelo observador/detector
- $v$ — velocidade do som no meio
- $v_f$ — velocidade da fonte
- $v_o$ — velocidade do observador (hidrofone/geofone)
- $\lambda_f$ — comprimento de onda emitido
- $\lambda_o$ — comprimento de onda percebido

</div>

<div class="resp">

**Resposta:** a) $1506,02$ Hz · b) $1509,04$ Hz · c) $1503,61$ Hz · d) $\lambda_f = 1,00$ m e $\lambda_o \approx 0,994$ m. Na aproximação a frequência percebida é maior do que a emitida e o comprimento de onda percebido é menor.

</div>

<div class="nota">

**Nota:** estes valores coincidem com a chave do professor (que usa $\lambda_o = v/f_o$). Em rigor, o comprimento de onda **no meio**, à frente da fonte em movimento, é $\lambda' = (v - v_f)/f_f = 1494/1500 = 0,996$ m, e o movimento do detector altera apenas a frequência que ele mede. Na prova, usar o método da chave.

</div>

## Questão 4 — Electrostática: três cargas pontuais

> Três cargas pontuais $q_1 = 2\ \mu$C, $q_2 = -3\ \mu$C e $q_3 = 1\ \mu$C estão localizadas nos pontos $P_1 = (0; 0)$ m, $P_2 = (4; 0)$ m e $P_3 = (0; 3)$ m.
> (a) Determine o vector, módulo e direcção do campo eléctrico no ponto $P = (2; 1)$ m.
> (b) Qual a força resultante (vector, módulo e direcção) sobre $q_3$ devido à acção de $q_1$ e $q_2$?

<div class="dados">

**Dados:** $q_1 = +2\times10^{-6}$ C em $(0; 0)$ · $q_2 = -3\times10^{-6}$ C em $(4; 0)$ · $q_3 = +1\times10^{-6}$ C em $(0; 3)$ · $P = (2; 1)$ m · $k = 9\times10^{9}$ N·m²/C²

</div>

### 4 a) Campo eléctrico em $P(2; 1)$

Princípio da sobreposição: $\vec{E}_P = \vec{E}_1 + \vec{E}_2 + \vec{E}_3$, com $\vec{E}_i = k\,\dfrac{q_i}{r_i^2}\,\hat{r}_i$, onde $\vec{r}_i$ vai **da carga $i$ para o ponto $P$**.

{{fig:fis-campo}}

**Passo 1 — Vectores posição (carga → P), distâncias e versores:**

| Carga | $\vec{r}_i = P - P_i$ | $r_i^2$ | $r_i$ | $\hat{r}_i = \vec{r}_i / r_i$ |
|:-:|:-:|:-:|:-:|:-:|
| $q_1$ | $2\hat{\imath} + 1\hat{\jmath}$ | $2^2 + 1^2 = 5$ | $\sqrt{5}$ | $\dfrac{2\hat{\imath} + \hat{\jmath}}{\sqrt5}$ |
| $q_2$ | $-2\hat{\imath} + 1\hat{\jmath}$ | $(-2)^2 + 1^2 = 5$ | $\sqrt{5}$ | $\dfrac{-2\hat{\imath} + \hat{\jmath}}{\sqrt5}$ |
| $q_3$ | $2\hat{\imath} - 2\hat{\jmath}$ | $2^2 + (-2)^2 = 8$ | $\sqrt{8}$ | $\dfrac{2\hat{\imath} - 2\hat{\jmath}}{\sqrt8}$ |

**Passo 2 — Campo de cada carga:**

$$\vec{E}_1 = \frac{(9\times10^9)(2\times10^{-6})}{5}\cdot\frac{2\hat{\imath} + \hat{\jmath}}{\sqrt5} = 3600\cdot\frac{2\hat{\imath} + \hat{\jmath}}{\sqrt5} = (3220\,\hat{\imath} + 1610\,\hat{\jmath})\ \text{N/C}$$

$$\vec{E}_2 = \frac{(9\times10^9)(-3\times10^{-6})}{5}\cdot\frac{-2\hat{\imath} + \hat{\jmath}}{\sqrt5} = -5400\cdot\frac{-2\hat{\imath} + \hat{\jmath}}{\sqrt5} = (4830\,\hat{\imath} - 2415\,\hat{\jmath})\ \text{N/C}$$

$$\vec{E}_3 = \frac{(9\times10^9)(1\times10^{-6})}{8}\cdot\frac{2\hat{\imath} - 2\hat{\jmath}}{\sqrt8} = 1125\cdot\frac{2\hat{\imath} - 2\hat{\jmath}}{\sqrt8} = (795,5\,\hat{\imath} - 795,5\,\hat{\jmath})\ \text{N/C}$$

(O campo de uma carga positiva **afasta-se** dela; o de uma carga negativa **aponta para** ela — por isso $\vec{E}_2$ aponta para $q_2$.)

**Passo 3 — Somar componente a componente:**

$$E_x = 3220 + 4830 + 795,5 = 8845\ \text{N/C} \qquad E_y = 1610 - 2415 - 795,5 = -1600\ \text{N/C}$$

$$\boxed{\vec{E}_P = (8845\,\hat{\imath} - 1600\,\hat{\jmath})\ \text{N/C}}$$

**Passo 4 — Módulo:**

$$|\vec{E}_P| = \sqrt{E_x^2 + E_y^2} = \sqrt{8845^2 + (-1600)^2} = \boxed{8989\ \text{N/C} \approx 8,99\times10^{3}\ \text{N/C}}$$

**Passo 5 — Direcção** (ângulo com o eixo $+x$):

$$\alpha = \tan^{-1}\!\left(\frac{E_y}{E_x}\right) = \tan^{-1}\!\left(\frac{-1600}{8845}\right) = \boxed{-10,3^\circ}$$

isto é, $10,3^\circ$ **abaixo** do eixo $+x$ (4.º quadrante).

### 4 b) Força resultante sobre $q_3$

$\vec{F}_3 = \vec{F}_{13} + \vec{F}_{23}$, com $\vec{F}_{i3} = k\,\dfrac{q_i\,q_3}{r_{i3}^2}\,\hat{r}_{i3}$, onde $\vec{r}_{i3}$ vai **da carga $i$ para $q_3$**.

{{fig:fis-forca}}

**Passo 1 — Força de $q_1$ sobre $q_3$.** $\vec{r}_{13} = (0; 3) - (0; 0) = 3\hat{\jmath}$, $r_{13} = 3$ m, $\hat{r}_{13} = \hat{\jmath}$:

$$\vec{F}_{13} = \frac{(9\times10^9)(2\times10^{-6})(1\times10^{-6})}{3^2}\,\hat{\jmath} = 2,0\times10^{-3}\,\hat{\jmath}\ \text{N} \quad \text{(repulsão: cargas do mesmo sinal)}$$

**Passo 2 — Força de $q_2$ sobre $q_3$.** $\vec{r}_{23} = (0; 3) - (4; 0) = -4\hat{\imath} + 3\hat{\jmath}$, $r_{23} = \sqrt{16 + 9} = 5$ m, $\hat{r}_{23} = \dfrac{-4\hat{\imath} + 3\hat{\jmath}}{5}$:

$$\vec{F}_{23} = \frac{(9\times10^9)(-3\times10^{-6})(1\times10^{-6})}{5^2}\cdot\frac{-4\hat{\imath} + 3\hat{\jmath}}{5} = -1,08\times10^{-3}\cdot\frac{-4\hat{\imath} + 3\hat{\jmath}}{5}$$

$$\vec{F}_{23} = (0,864\,\hat{\imath} - 0,648\,\hat{\jmath})\times10^{-3}\ \text{N} \quad \text{(atracção: aponta de } q_3 \text{ para } q_2)$$

**Passo 3 — Resultante:**

$$\vec{F}_3 = \big(0,864\,\hat{\imath} + (2,000 - 0,648)\,\hat{\jmath}\big)\times10^{-3}\ \text{N}$$

$$\boxed{\vec{F}_3 = (0,864\,\hat{\imath} + 1,352\,\hat{\jmath})\times10^{-3}\ \text{N} = (0,864\,\hat{\imath} + 1,352\,\hat{\jmath})\ \text{mN}}$$

**Passo 4 — Módulo e direcção:**

$$|\vec{F}_3| = \sqrt{0,864^2 + 1,352^2}\times10^{-3} = \boxed{1,604\times10^{-3}\ \text{N} = 1,604\ \text{mN}}$$

$$\alpha = \tan^{-1}\!\left(\frac{F_y}{F_x}\right) = \tan^{-1}\!\left(\frac{1,352}{0,864}\right) = \boxed{57,4^\circ}$$

acima do eixo $+x$ (1.º quadrante).

<div class="simb">

**Significado dos símbolos**

- $\vec{E}_i$ — campo criado pela carga $q_i$ no ponto $P$
- $\vec{r}_i$ — vector que vai da carga $q_i$ até $P$
- $\hat{\imath}$, $\hat{\jmath}$ — vectores unitários dos eixos $x$ e $y$
- $E_x$, $E_y$ — componentes do campo
- $\vec{F}_{13}$ — força que $q_1$ exerce sobre $q_3$
- $\vec{F}_{23}$ — força que $q_2$ exerce sobre $q_3$
- $r_{13}$, $r_{23}$ — distâncias de $q_1$ e $q_2$ a $q_3$
- $\alpha$ — ângulo do vector com o eixo $+x$

</div>

<div class="resp">

**Resposta:** a) $\vec{E}_P = (8845\,\hat{\imath} - 1600\,\hat{\jmath})$ N/C, $|\vec{E}_P| \approx 8989$ N/C, $\alpha \approx -10,3^\circ$ · b) $\vec{F}_3 = (0,864\,\hat{\imath} + 1,352\,\hat{\jmath})$ mN, $|\vec{F}_3| \approx 1,60$ mN, $\alpha \approx 57,4^\circ$.

</div>

<div class="pb"></div>

## Prova de Consolidação II — Ondas Mecânicas (SIM / NÃO)

> Responda no lugar indicado com uma destas palavras: SIM – NÃO, conforme a opinião que tem em cada afirmação.

<table class="esq">
<tr><th>N.º</th><th>Afirmação</th><th>Resposta certa</th><th>Justificação</th></tr>
<tr><td>1</td><td>Todas as ondas mecânicas são governadas pelas leis de Newton e existem apenas em meios materiais.</td><td><span class="ok">SIM</span></td><td>As ondas mecânicas são perturbações de um meio material (corda, ar, água, rocha) e o movimento das suas partículas obedece às leis de Newton. Não se propagam no vácuo.</td></tr>
<tr><td>2</td><td>Quando a direcção de oscilação é paralela à direcção de propagação de uma onda, dizemos que a onda é transversal.</td><td><span class="no">NÃO</span></td><td>Nesse caso a onda é <strong>longitudinal</strong> (ex.: som). É transversal quando a oscilação é <strong>perpendicular</strong> à propagação (ex.: corda).</td></tr>
<tr><td>3</td><td>Um comprimento de onda é a distância (medida paralelamente à direcção de propagação) entre repetições da forma de onda.</td><td><span class="ok">SIM</span></td><td>É a definição de $\lambda$: distância entre dois pontos consecutivos em fase (ex.: duas cristas).</td></tr>
<tr><td>4</td><td>A velocidade de uma onda numa corda ideal esticada depende apenas da tracção da corda.</td><td><span class="no">NÃO</span></td><td>Depende da tracção <strong>e</strong> da densidade linear: $v = \sqrt{T/\mu}$.</td></tr>
<tr><td>5</td><td>Ondas superpostas somam-se algebricamente para produzir uma onda resultante ou onda total.</td><td><span class="ok">SIM</span></td><td>Princípio da sobreposição: $y(x,t) = y_1(x,t) + y_2(x,t)$.</td></tr>
<tr><td>6</td><td>Se duas ondas sinusoidais de mesma amplitude e comprimento de onda se propagam no mesmo sentido numa corda, interferem para produzir uma onda que se propaga no sentido oposto.</td><td><span class="no">NÃO</span></td><td>A onda resultante propaga-se no <strong>mesmo sentido</strong>, com amplitude $2A\cos(\phi/2)$, que depende da diferença de fase $\phi$.</td></tr>
<tr><td>7</td><td>Uma interferência é dita destrutiva quando as ondas que interferem têm a mesma fase, produzindo assim grandes amplitudes.</td><td><span class="no">NÃO</span></td><td>Mesma fase → interferência <strong>construtiva</strong> (amplitude máxima). A destrutiva ocorre em oposição de fase ($\phi = \pi$), com amplitude mínima.</td></tr>
<tr><td>8</td><td>Numa corda presa nas extremidades produz-se uma onda estacionária se a frequência de oscilação for muito próxima da frequência natural de oscilação.</td><td><span class="ok">SIM</span></td><td>É a condição de <strong>ressonância</strong>: $f \approx f_n = \dfrac{n\,v}{2L}$.</td></tr>
<tr><td>9</td><td>O factor determinante para a velocidade do som num meio elástico é a densidade volumétrica do meio.</td><td><span class="no">NÃO</span></td><td>Depende de duas propriedades — a elástica e a inercial: $v = \sqrt{B/\rho}$. O módulo de elasticidade $B$ é tão determinante como a densidade (o som é mais rápido nos sólidos, apesar de mais densos).</td></tr>
<tr><td>10</td><td>A aproximação entre um detector e uma fonte sonora produz uma diminuição da frequência.</td><td><span class="no">NÃO</span></td><td>Efeito Doppler: na aproximação a frequência percebida <strong>aumenta</strong>; diminui no afastamento.</td></tr>
<tr><td>11</td><td>Para uma interferência construtiva de ondas sonoras, a diferença de percurso é igual a um número inteiro de $\lambda$.</td><td><span class="ok">SIM</span></td><td>Construtiva: $\Delta L = m\lambda$ ($m = 0, 1, 2, \dots$). Destrutiva: $\Delta L = (m + \tfrac12)\lambda$.</td></tr>
<tr><td>12</td><td>A intensidade sonora é a taxa média com que a energia é transferida numa determinada área.</td><td><span class="ok">SIM</span></td><td>$I = \dfrac{P}{A_s}$: potência média por unidade de área (W/m²).</td></tr>
</table>

<div class="simb">

**Significado dos símbolos**

- $T$ — tracção na corda (N)
- $\mu$ — densidade linear de massa (kg/m)
- $\phi$ — diferença de fase entre as duas ondas (rad)
- $B$ — módulo de elasticidade volumétrico do meio (Pa)
- $\rho$ — densidade volumétrica do meio (kg/m³)
- $\Delta L$ — diferença de percurso entre as duas ondas (m)
- $m$ — número inteiro
- $I$ — intensidade sonora (W/m²)
- $P$ — potência da fonte (W)
- $A_s$ — área atravessada pela onda (m²)

</div>

<div class="resp">

**Chave:** 1-SIM · 2-NÃO · 3-SIM · 4-NÃO · 5-SIM · 6-NÃO · 7-NÃO · 8-SIM · 9-NÃO · 10-NÃO · 11-SIM · 12-SIM

</div>
