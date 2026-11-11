#include <stdio.h>

int main(void)
{
    int n, d, divisores;
    long long produto = 1;

    printf("Primos entre 1 e 20: ");
    for (n = 1; n <= 20; n++) {
        divisores = 0;
        for (d = 1; d <= n; d++)           /* conta os divisores de n */
            if (n % d == 0)
                divisores++;

        if (divisores == 2) {              /* primo: so 1 e n         */
            printf("%d ", n);
            produto *= n;
        }
    }
    printf("\nProduto dos primos = %lld\n", produto);
    return 0;
}
