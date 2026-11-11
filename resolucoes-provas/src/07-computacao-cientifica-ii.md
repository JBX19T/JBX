---
titulo: Computação Científica II — Resolução passo a passo
subtitulo: Ficha de Trabalho · Estruturas de repetição (for, while e do-while) em C
instituicao: ISPTEC — Instituto Superior Politécnico de Tecnologias e Ciências
info: Disciplina=CC II – Computação Científica II|Docente=André Filemon|Semestre=1.º|Linguagem=C
ficheiro: 07_Computacao-Cientifica-II_Ficha-de-Trabalho.pdf
rodape: Ficha de Trabalho · Estruturas de repetição
---

## Conceitos usados e significado dos símbolos

| Estrutura / operador | Para que serve |
|---|---|
| `for (inicio; condicao; passo)` | Repetição com **número de voltas conhecido** |
| `while (condicao)` | Repete **enquanto** a condição for verdadeira (testa antes) |
| `do { ... } while (condicao);` | Repete **pelo menos uma vez** (testa depois) — ideal para validar dados |
| `if (...) { ... } else { ... }` | Decisão |
| `%` (resto da divisão) | `n % 2 == 0` → $n$ é par; `n % d == 0` → $d$ divide $n$ |
| `+=`, `*=`, `++` | `x += y` é `x = x + y`; `x *= y` é `x = x * y`; `i++` soma 1 a `i` |
| `&&`, `\|\|` | «E» lógico, «OU» lógico |
| `scanf` / `printf` | Ler do teclado / escrever no ecrã |

<div class="simb">

**Significado dos tipos e formatos**

- `int` — número inteiro · `long long` — inteiro grande · `double` — número real · `char` — um carácter
- `%d` — inteiro · `%lf` — `double` na leitura · `%.2f` — real com 2 casas decimais · `%c` — carácter · `%lld` — `long long`
- `#define N 20` — constante simbólica (o compilador substitui `N` por 20)
- **acumulador** — variável que soma valores a cada volta (`soma += salario`)
- **contador** — variável que conta ocorrências (`mulheres++`)
- **divisor** — $d$ é divisor de $n$ se o resto de $n / d$ é zero
- $\bar{x} = \dfrac{\sum x_i}{N}$ — média aritmética de $N$ valores

</div>

## Exercício 1 — Pesquisa entre habitantes da província de Luanda

> Foram coletados os dados de idade, sexo (F/M) e salário de **20 pessoas**. Escrever um programa em C que mostre: a) a média de salário do grupo; b) maior e menor idade do grupo; c) quantidade de mulheres com salários até AKZ 100 000.

**Passo 1 — Entradas e saídas.** Entradas: idade (`int`), sexo (`char`) e salário (`double`) de cada pessoa. Saídas: média, maior/menor idade e contagem.

**Passo 2 — Variáveis:** `soma` (acumulador de salários), `maior` e `menor` (idades extremas), `mulheres` (contador).

**Passo 3 — Ciclo `for`** de 1 a 20 (número de pessoas conhecido):

- lê os três dados;
- soma o salário a `soma`;
- na 1.ª pessoa, `maior` e `menor` recebem a idade lida; nas seguintes compara-se (`idade > maior`, `idade < menor`);
- se for mulher **e** o salário for ≤ 100 000, incrementa `mulheres`.

**Passo 4 — Depois do ciclo:** média $=$ `soma / N`.

{{code:ex1_pesquisa_luanda.c}}

**Teste (dados de exemplo):** média $196\,850{,}00$ AKZ; maior idade 58; menor idade 18; 3 mulheres com salário ≤ 100 000 — igual ao valor calculado independentemente.

## Exercício 2 — Números ímpares entre 100 e 400

> Fazer um programa em C que gera e mostre os números ímpares entre 100 e 400.

**Ideia:** o 1.º ímpar depois de 100 é **101**; depois soma-se **2** a cada volta, parando antes de 400 (o último é **399**). Assim não é preciso testar se cada número é ímpar.

{{code:ex2_impares_100_400.c}}

**Alternativa** (testando cada número): `for (n = 100; n <= 400; n++) if (n % 2 != 0) printf("%d ", n);`

**Resultado:** 101 103 105 … 397 399 — são **150** números ímpares, de 101 a 399.

## Exercício 3 — Pares entre $a$ e $b$ (5 pares de valores)

> Escrever um programa em C que lê 5 pares de valores $a$, $b$, todos inteiros e positivos, um par de cada vez, e com $a < b$, mostre os inteiros pares de $a$ até $b$, incluindo o $a$ e o $b$ se forem pares.

**Passo 1 — Ciclo exterior `for`** repete 5 vezes (um par por volta).

**Passo 2 — Validação com `do-while`:** pede os valores **pelo menos uma vez** e repete enquanto forem inválidos (`a <= 0 || b <= 0 || a >= b`).

**Passo 3 — Ciclo interior `for`** de $n = a$ até $n = b$ (inclui os dois extremos, por causa do `<=`): imprime $n$ se `n % 2 == 0`.

{{code:ex3_pares_a_ate_b.c}}

**Teste** (entradas 2 9, 3 3 ✗ repete, 5 10, 1 4, 10 15, 7 12):

| Par | Saída |
|:-:|---|
| 2 9 | 2 4 6 8 |
| 5 10 | 6 8 10 |
| 1 4 | 2 4 |
| 10 15 | 10 12 14 |
| 7 12 | 8 10 12 |

O par «3 3» foi rejeitado e voltou a pedir (pois exige $a < b$).

## Exercício 4 — Produto dos números primos entre 1 e 20

> Elabore um programa em C que calcule e mostre o produto dos números primos entre 1 e 20. (Número primo é todo número que possui apenas dois divisores, o número 1 e o próprio número.)

**Passo 1 — Usar a definição do enunciado:** $n$ é primo se tiver **exactamente 2 divisores** (1 e $n$). O número 1 só tem 1 divisor, por isso não é primo.

**Passo 2 — Ciclo exterior** de $n = 1$ a $20$. Para cada $n$:

- ciclo interior $d = 1, \dots, n$ conta os divisores (`n % d == 0`);
- se `divisores == 2`, mostra $n$ e multiplica-o ao acumulador `produto` (inicializado a **1**, o elemento neutro do produto).

**Passo 3 — Tipo da variável:** o produto é grande, por isso usa-se `long long`.

{{code:ex4_produto_primos.c}}

**Cálculo à mão** (confirma o programa): primos entre 1 e 20: $2, 3, 5, 7, 11, 13, 17, 19$.

$$2 \times 3 \times 5 \times 7 \times 11 \times 13 \times 17 \times 19 = 9\,699\,690$$

<div class="resp">

**Resposta:** os primos são 2, 3, 5, 7, 11, 13, 17, 19 e o produto é **9 699 690**.

</div>

<div class="nota">

**Como compilar e executar:** `gcc ex1_pesquisa_luanda.c -o ex1` e depois `./ex1` (Linux/Mac) ou `ex1.exe` (Windows). Os ficheiros `.c` estão também na pasta `codigo-C` do repositório. Os programas foram compilados com `-Wall -Wextra` sem avisos e testados.

</div>
