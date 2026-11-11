#include <stdio.h>

#define N 20                 /* numero de pessoas pesquisadas */
#define LIMITE_SALARIO 100000.0

int main(void)
{
    int i, idade, maior, menor, mulheres = 0;
    char sexo;
    double salario, soma = 0.0;

    for (i = 1; i <= N; i++) {
        printf("Pessoa %d - idade, sexo (F/M) e salario (AKZ): ", i);
        scanf("%d %c %lf", &idade, &sexo, &salario);

        soma += salario;                       /* acumula salarios       */

        if (i == 1) {                          /* 1.a pessoa inicia      */
            maior = idade;                     /* maior e menor idade    */
            menor = idade;
        } else {
            if (idade > maior) maior = idade;
            if (idade < menor) menor = idade;
        }

        if ((sexo == 'F' || sexo == 'f') && salario <= LIMITE_SALARIO)
            mulheres++;                        /* conta as mulheres      */
    }

    printf("\na) Media de salario do grupo: %.2f AKZ\n", soma / N);
    printf("b) Maior idade: %d anos | Menor idade: %d anos\n", maior, menor);
    printf("c) Mulheres com salario ate 100000 AKZ: %d\n", mulheres);
    return 0;
}
