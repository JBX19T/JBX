---
titulo: Físico-Química — Resolução passo a passo
subtitulo: Exame de Época Normal · 19 de Novembro de 2025
instituicao: ISPTEC — Instituto Superior Politécnico de Tecnologias e Ciências
info: Curso=Engenharia de Petróleos|Docente=Joaquim Quimonha|Semestre=2025-26/1|Duração=90 minutos
ficheiro: 01_Fisico-Quimica_Exame-Epoca-Normal.pdf
rodape: Exame de Época Normal · 19/11/2025
---

## Formulário e significado dos símbolos

| Fórmula | Nome | Quando se usa |
|---|---|---|
| $PV = nRT$ | Equação dos gases ideais | Gás ideal (perfeito) |
| $Z = \dfrac{PV_m}{RT}$ | Factor de compressibilidade | Mede o desvio do gás real em relação ao ideal |
| $\left(P + \dfrac{a}{V_m^2}\right)(V_m - b) = RT$ | Equação de Van der Waals | Gás real |
| $Z \approx 1 + \dfrac{B}{V_m}$ | Equação do virial (truncada) | Gás real a pressões moderadas |
| $v_{rms} = \sqrt{\dfrac{3RT}{M}}$ | Velocidade média quadrática | Teoria cinética dos gases |
| $\Delta U = q + w$ | 1.ª Lei da Termodinâmica | Qualquer processo |
| $w = -P_{ext}\,\Delta V$ | Trabalho contra pressão externa constante | Expansão/compressão irreversível |
| $\Delta U = nC_{V,m}\Delta T$ ; $\Delta H = nC_{P,m}\Delta T$ | Energia interna e entalpia | Gás ideal |
| $C_{P,m} = C_{V,m} + R$ | Relação de Mayer | Gás ideal |

<div class="simb">

**Significado dos símbolos**

- $P$ — pressão do gás (atm ou Pa)
- $V$ — volume (dm³ = L, ou m³)
- $V_m = V/n$ — volume molar (dm³·mol⁻¹)
- $n$ — quantidade de substância (mol)
- $T$ — temperatura absoluta (K)
- $R$ — constante dos gases: $0,0821$ atm·dm³·mol⁻¹·K⁻¹ $= 8,314$ J·mol⁻¹·K⁻¹
- $Z$ — factor de compressibilidade (sem unidades)
- $a$ — constante de Van der Waals ligada às **forças atractivas**
- $b$ — constante de Van der Waals ligada ao **volume próprio das moléculas** (co-volume)
- $B$ — segundo coeficiente do virial (dm³·mol⁻¹)
- $M$ — massa molar (kg·mol⁻¹)
- $v_{rms}$ — velocidade média quadrática (m·s⁻¹)
- $k_B$ — constante de Boltzmann ($1,38\times10^{-23}$ J·K⁻¹)
- $U$ — energia interna (J)
- $H$ — entalpia, $H = U + PV$ (J)
- $q$ — calor trocado (J); $q>0$ se o sistema recebe
- $w$ — trabalho (J); $w<0$ se o sistema realiza trabalho
- $P_{ext}$ — pressão externa (Pa)
- $C_{V,m}$, $C_{P,m}$ — capacidades caloríficas molares a volume e a pressão constante (J·mol⁻¹·K⁻¹)
- $\Delta$ — variação (valor final − valor inicial)

</div>

<div class="nota">

**Conversões úteis:** $1\ \text{atm} = 101\,325\ \text{Pa}$ · $1\ \text{dm}^3 = 1\ \text{L} = 10^{-3}\ \text{m}^3$ · $1\ \text{kPa}\cdot\text{dm}^3 = 1\ \text{J}$ · $1\ \text{mmol} = 10^{-3}\ \text{mol}$

</div>

## Questão 1 — Gases e termodinâmica (teoria)

### 1 a) Diferença entre gás ideal e gás real

> Explique a diferença fundamental entre um gás ideal e um gás real em termos das interacções moleculares e do volume das moléculas.

| | Gás ideal | Gás real |
|---|---|---|
| **Interacções moleculares** | Não existem forças de atracção nem de repulsão entre as moléculas; só há choques perfeitamente elásticos. | Existem forças intermoleculares: **atractivas** a distâncias médias e **repulsivas** a distâncias muito curtas. |
| **Volume das moléculas** | As moléculas são pontos materiais: o seu volume próprio é desprezável (nulo) face ao volume do recipiente. | As moléculas têm volume próprio (finito), que reduz o volume livre disponível para o movimento. |
| **Equação de estado** | $PV_m = RT$ | $\left(P + \dfrac{a}{V_m^2}\right)(V_m - b) = RT$ |

<div class="resp">

**Resposta:** No gás ideal admite-se que as moléculas **não interagem** entre si e **não ocupam volume**. No gás real as moléculas **atraem-se e repelem-se** e **têm volume próprio**. Por isso o gás real só se aproxima do ideal a **baixas pressões e altas temperaturas** (moléculas afastadas e rápidas). Na equação de Van der Waals, o termo $a/V_m^2$ corrige as atracções e o termo $b$ corrige o volume das moléculas.

</div>

### 1 b) Significado físico da temperatura absoluta

> De acordo com a Teoria Cinética dos Gases, qual é o significado físico da temperatura absoluta $T$ de um gás e como ela se relaciona com a velocidade média quadrática das moléculas?

Segundo a teoria cinética, a pressão resulta dos choques das moléculas com as paredes:

$$PV = \tfrac{1}{3}\,nM\,v_{rms}^2$$

Comparando com a equação dos gases ideais $PV = nRT$:

$$\tfrac{1}{3}\,nM\,v_{rms}^2 = nRT \;\;\Longrightarrow\;\; v_{rms} = \sqrt{\frac{3RT}{M}}$$

E a energia cinética média de translação de uma molécula é

$$\langle E_c \rangle = \tfrac{1}{2}\,m\,v_{rms}^2 = \tfrac{3}{2}\,k_B T$$

<div class="simb">

**Significado dos símbolos**

- $v_{rms}$ — velocidade média quadrática, $v_{rms} = \sqrt{\langle v^2\rangle}$
- $M$ — massa molar do gás (kg·mol⁻¹)
- $m$ — massa de uma molécula (kg)
- $\langle E_c \rangle$ — energia cinética média de translação por molécula (J)
- $k_B = R/N_A$ — constante de Boltzmann
- $N_A$ — constante de Avogadro

</div>

<div class="resp">

**Resposta:** A temperatura absoluta é uma **medida da energia cinética média de translação das moléculas** do gás ($\langle E_c\rangle = \tfrac32 k_BT$): quanto maior $T$, maior a agitação molecular. A relação com a velocidade é $v_{rms} = \sqrt{3RT/M}$, isto é, $T \propto v_{rms}^2$ — a velocidade média quadrática é directamente proporcional a $\sqrt{T}$ e inversamente proporcional a $\sqrt{M}$.

</div>

### 1 c) Factor de compressibilidade

> $Z = \dfrac{PV_m}{RT}$. Qual é o valor de $Z$ para um gás ideal? E o que valores de $Z<1$ indicam sobre as forças intermoleculares dominantes num gás real?

Para o gás ideal, $PV_m = RT$, logo

$$Z = \frac{PV_m}{RT} = \frac{RT}{RT} = 1$$

Como $Z = \dfrac{V_m\,(\text{real})}{V_m\,(\text{ideal})}$, tem-se:

| Valor de $Z$ | Significado | Forças dominantes |
|---|---|---|
| $Z = 1$ | Comportamento ideal | Nenhuma |
| $Z < 1$ | $V_m$ real **menor** que o ideal → gás mais compressível | **Atractivas** |
| $Z > 1$ | $V_m$ real **maior** que o ideal → gás menos compressível | **Repulsivas** |

<div class="resp">

**Resposta:** Para um gás ideal $\boxed{Z = 1}$ em quaisquer condições. Valores de $Z<1$ indicam que predominam as **forças atractivas**: as moléculas puxam-se umas às outras, o volume molar fica menor do que o do gás ideal e o gás é mais fácil de comprimir (ocorre a pressões baixas/moderadas e temperaturas baixas).

</div>

## Questão 2 — Demonstração de $C_P = C_V + R$

> Demonstre a relação entre as capacidades caloríficas em transformações isométrica e isobárica como $C_P = C_V + R$.

**Passo 1 — Definições** (para 1 mol de gás ideal):

$$C_{V} = \left(\frac{\partial U}{\partial T}\right)_V \qquad\qquad C_{P} = \left(\frac{\partial H}{\partial T}\right)_P$$

**Passo 2 — Transformação isométrica** ($V$ constante, $dV = 0$, logo $w = 0$). Pela 1.ª Lei:

$$dU = \delta q_V = C_V\,dT$$

Como no gás ideal $U$ só depende de $T$, a expressão $dU = C_V\,dT$ vale para **qualquer** transformação.

**Passo 3 — Transformação isobárica** ($P$ constante). O calor trocado é $\delta q_P = C_P\,dT$ e o trabalho é $\delta w = -P\,dV$. Pela 1.ª Lei:

$$dU = \delta q_P + \delta w \;\;\Longrightarrow\;\; C_V\,dT = C_P\,dT - P\,dV$$

**Passo 4 — Usar a equação do gás ideal** (1 mol, $P$ constante): $PV = RT \Rightarrow P\,dV = R\,dT$. Substituindo:

$$C_V\,dT = C_P\,dT - R\,dT$$

**Passo 5 — Dividir por $dT$:**

$$\boxed{C_P = C_V + R}$$

**Demonstração alternativa (pela entalpia):** $H = U + PV = U + RT$. Derivando em ordem a $T$:

$$\frac{dH}{dT} = \frac{dU}{dT} + R \;\;\Longrightarrow\;\; C_P = C_V + R$$

<div class="simb">

**Significado dos símbolos**

- $C_V$ — capacidade calorífica molar a volume constante (isométrica)
- $C_P$ — capacidade calorífica molar a pressão constante (isobárica)
- $\delta q_V$, $\delta q_P$ — calor infinitesimal trocado a $V$ e a $P$ constante
- $\delta w = -P\,dV$ — trabalho infinitesimal de expansão
- $dU$, $dH$, $dT$ — variações infinitesimais de energia interna, entalpia e temperatura
- $R$ — constante dos gases ideais

</div>

<div class="resp">

**Interpretação:** $C_P > C_V$ porque, a pressão constante, parte do calor fornecido é usada para o gás **realizar trabalho de expansão** ($R$ é exactamente esse trabalho, por mol e por kelvin); a volume constante todo o calor serve para aumentar a energia interna.

</div>

## Questão 3 — Volume molar do H₂ como gás de Van der Waals

> Estime o volume molar de H₂ a 300 K e 200 atm admitindo que o gás se comporta como gás de Van der Waals. Sendo $a = 0,244$ dm⁶·atm·mol⁻² e $b = 0,0266$ dm³·mol⁻¹.
> a) Qual seria o valor do factor de compressibilidade e diga, justificando, quais forças são predominantes.

<div class="dados">

**Dados:** $T = 300\ \text{K}$ · $P = 200\ \text{atm}$ · $a = 0,244\ \text{dm}^6\,\text{atm}\,\text{mol}^{-2}$ · $b = 0,0266\ \text{dm}^3\,\text{mol}^{-1}$ · $R = 0,0821\ \text{atm}\,\text{dm}^3\,\text{mol}^{-1}\,\text{K}^{-1}$ · **Pedido:** $V_m$ e $Z$

</div>

**Passo 1 — Equação de Van der Waals:**

$$\left(P + \frac{a}{V_m^2}\right)(V_m - b) = RT$$

Esta equação é do 3.º grau em $V_m$ ($PV_m^3 - (Pb + RT)V_m^2 + aV_m - ab = 0$), por isso resolve-se por **aproximações sucessivas**. Isolando o $V_m$ do segundo parêntesis:

$$V_m = b + \frac{RT}{P + \dfrac{a}{V_m^2}}$$

**Passo 2 — Valor inicial (gás ideal):**

$$RT = 0,0821 \times 300 = 24,63\ \text{atm}\,\text{dm}^3\,\text{mol}^{-1}$$

$$V_m^{(0)} = \frac{RT}{P} = \frac{24,63}{200} = 0,1232\ \text{dm}^3\,\text{mol}^{-1}$$

**Passo 3 — Iterações** (substitui-se o valor anterior no lado direito):

$$V_m^{(1)} = 0,0266 + \frac{24,63}{200 + \dfrac{0,244}{(0,1232)^2}} = 0,0266 + \frac{24,63}{216,09} = 0,1406\ \text{dm}^3\,\text{mol}^{-1}$$

| Iteração | $V_m$ usado (dm³/mol) | $a/V_m^2$ (atm) | Novo $V_m$ (dm³/mol) |
|:-:|:-:|:-:|:-:|
| 1 | 0,1232 | 16,09 | 0,1406 |
| 2 | 0,1406 | 12,35 | 0,1426 |
| 3 | 0,1426 | 12,00 | 0,1428 |
| 4 | 0,1428 | 11,97 | 0,1428 |

O valor deixou de variar, logo convergiu:

$$\boxed{V_m \approx 0,143\ \text{dm}^3\,\text{mol}^{-1}}$$

**Verificação:** $\left(200 + \dfrac{0,244}{0,1428^2}\right)(0,1428 - 0,0266) = 211,97 \times 0,1162 = 24,63 = RT$ ✓

### 3 a) Factor de compressibilidade

$$Z = \frac{PV_m}{RT} = \frac{200 \times 0,1428}{24,63} = \boxed{1,16}$$

Também se pode escrever $Z = \dfrac{V_m\,(\text{real})}{V_m\,(\text{ideal})} = \dfrac{0,1428}{0,1232} = 1,16$.

<div class="simb">

**Significado dos símbolos**

- $V_m$ — volume molar do gás real (dm³·mol⁻¹)
- $V_m^{(0)}$ — primeira estimativa (volume molar do gás ideal)
- $a/V_m^2$ — «pressão interna»: correcção devida às atracções
- $b$ — co-volume: volume excluído pelas próprias moléculas
- $RT$ — produto da constante dos gases pela temperatura
- $Z$ — factor de compressibilidade

</div>

<div class="resp">

**Resposta:** $V_m \approx 0,143\ \text{dm}^3\,\text{mol}^{-1}$ e $Z \approx 1,16$. Como $Z > 1$, o volume molar real é **maior** do que o ideal ($0,143 > 0,123$): predominam as **forças repulsivas**. Justificação: a 200 atm as moléculas estão muito próximas e o seu volume próprio (termo $b$) pesa mais do que as atracções; além disso o H₂ é uma molécula pequena e apolar, com atracções muito fracas ($a$ pequeno) — a correcção das atracções é só $a/V_m^2 \approx 12$ atm em 200 atm.

</div>

## Questão 4 — Factor de compressibilidade e coeficiente do virial

> A 300 K e 20 atm, o factor de compressibilidade do gás é 0,86. Calcule o volume ocupado por 8,2 mmol do gás nessas condições e b) o valor aproximado do segundo coeficiente de virial $B$ a 300 K.

<div class="dados">

**Dados:** $T = 300\ \text{K}$ · $P = 20\ \text{atm}$ · $Z = 0,86$ · $n = 8,2\ \text{mmol} = 8,2\times10^{-3}\ \text{mol}$ · $R = 0,0821\ \text{atm}\,\text{dm}^3\,\text{mol}^{-1}\,\text{K}^{-1}$ · **Pedido:** $V$ e $B$

</div>

### 4 a) Volume ocupado

**Passo 1 — Da definição de $Z$ tira-se o volume molar:**

$$Z = \frac{PV_m}{RT} \;\;\Longrightarrow\;\; V_m = \frac{ZRT}{P}$$

$$V_m = \frac{0,86 \times 0,0821 \times 300}{20} = \frac{21,18}{20} = 1,059\ \text{dm}^3\,\text{mol}^{-1}$$

**Passo 2 — Volume total** ($V = n\,V_m$):

$$V = 8,2\times10^{-3} \times 1,059 = 8,68\times10^{-3}\ \text{dm}^3$$

$$\boxed{V \approx 8,7\times10^{-3}\ \text{dm}^3 = 8,7\ \text{cm}^3}$$

### 4 b) Segundo coeficiente do virial

**Passo 1 — Equação do virial truncada no segundo termo:**

$$Z = 1 + \frac{B}{V_m} + \dots \;\;\Longrightarrow\;\; B \approx V_m\,(Z - 1)$$

**Passo 2 — Substituir:**

$$B \approx 1,059 \times (0,86 - 1) = 1,059 \times (-0,14)$$

$$\boxed{B \approx -0,15\ \text{dm}^3\,\text{mol}^{-1}}$$

<div class="simb">

**Significado dos símbolos**

- $Z$ — factor de compressibilidade
- $V_m$ — volume molar real nas condições dadas
- $V$ — volume total ocupado pela amostra
- $n$ — quantidade de gás (mol)
- $B$ — segundo coeficiente do virial: mede as interacções entre **pares** de moléculas

</div>

<div class="resp">

**Resposta:** a) $V \approx 8,7\ \text{cm}^3$; b) $B \approx -0,15\ \text{dm}^3\,\text{mol}^{-1}$. O sinal negativo de $B$ (e $Z<1$) mostra que, nestas condições, predominam as forças **atractivas**.

</div>

## Questão 5 — Expansão adiabática do CO₂ contra pressão constante

> Uma amostra de 5,0 mol de CO₂(g), inicialmente confinada num volume de 15 dm³ a 280 K, sofre uma expansão adiabática contra uma pressão constante de 78,5 kPa, até o seu volume aumentar de um factor de 4. Calcule $q$, $w$, $\Delta U$ e $\Delta H$. (A pressão final do gás não é necessariamente 78,5 kPa.)

<div class="dados">

**Dados:** $n = 5,0\ \text{mol}$ · $V_i = 15\ \text{dm}^3$ · $T_i = 280\ \text{K}$ · $P_{ext} = 78,5\ \text{kPa}$ · $V_f = 4V_i = 60\ \text{dm}^3$ · processo adiabático · $C_{P,m}(\text{CO}_2) = 37,11\ \text{J}\,\text{mol}^{-1}\,\text{K}^{-1}$ (valor tabelado) · $R = 8,314\ \text{J}\,\text{mol}^{-1}\,\text{K}^{-1}$

</div>

**Passo 1 — Calor.** O processo é adiabático (não há troca de calor):

$$\boxed{q = 0}$$

**Passo 2 — Trabalho.** A expansão é irreversível, contra pressão externa constante:

$$w = -P_{ext}\,\Delta V = -P_{ext}\,(V_f - V_i)$$

$$w = -78,5\ \text{kPa} \times (60 - 15)\ \text{dm}^3 = -78,5 \times 45 = -3532,5\ \text{J}$$

$$\boxed{w \approx -3,5\ \text{kJ}}$$

(lembrar que $1\ \text{kPa}\cdot\text{dm}^3 = 10^3\ \text{Pa} \times 10^{-3}\ \text{m}^3 = 1\ \text{J}$)

**Passo 3 — Energia interna.** Pela 1.ª Lei, com $q = 0$:

$$\Delta U = q + w = 0 + (-3532,5) \;\;\Longrightarrow\;\; \boxed{\Delta U \approx -3,5\ \text{kJ}}$$

**Passo 4 — Variação de temperatura** (necessária para $\Delta H$). Para o gás ideal, $\Delta U = nC_{V,m}\Delta T$, com

$$C_{V,m} = C_{P,m} - R = 37,11 - 8,314 = 28,80\ \text{J}\,\text{mol}^{-1}\,\text{K}^{-1}$$

$$\Delta T = \frac{\Delta U}{nC_{V,m}} = \frac{-3532,5}{5,0 \times 28,80} = -24,5\ \text{K} \qquad (T_f = 280 - 24,5 = 255,5\ \text{K})$$

**Passo 5 — Entalpia:**

$$\Delta H = nC_{P,m}\Delta T = 5,0 \times 37,11 \times (-24,5) = -4552\ \text{J}$$

$$\boxed{\Delta H \approx -4,6\ \text{kJ}}$$

**Verificação:** $\Delta H = \Delta U + nR\Delta T = -3532,5 + 5,0\times 8,314\times(-24,5) = -3532,5 - 1019,9 = -4552\ \text{J}$ ✓

<div class="simb">

**Significado dos símbolos**

- $q$ — calor trocado com a vizinhança
- $w$ — trabalho ($<0$: o gás realiza trabalho ao expandir)
- $P_{ext}$ — pressão externa constante contra a qual o gás se expande
- $V_i$, $V_f$ — volume inicial e final
- $\Delta V = V_f - V_i$ — variação de volume
- $\Delta U$ — variação de energia interna
- $\Delta H$ — variação de entalpia
- $\Delta T = T_f - T_i$ — variação de temperatura
- $C_{V,m}$, $C_{P,m}$ — capacidades caloríficas molares do CO₂

</div>

<div class="resp">

**Resposta:** $q = 0$ · $w \approx -3,5\ \text{kJ}$ · $\Delta U \approx -3,5\ \text{kJ}$ · $\Delta H \approx -4,6\ \text{kJ}$ (com $\Delta T \approx -24,5\ \text{K}$).

O gás realiza trabalho à custa da sua própria energia interna (não recebe calor), por isso **arrefece**. Nota: a pressão final é $P_f = nRT_f/V_f = 5,0\times8,314\times255,5/0,060 \approx 177\ \text{kPa}$, diferente de 78,5 kPa, tal como o enunciado avisa.

</div>
