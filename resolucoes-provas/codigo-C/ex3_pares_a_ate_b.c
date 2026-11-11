#include <stdio.h>

int main(void)
{
    int par, a, b, n;

    for (par = 1; par <= 5; par++) {
        do {                                   /* valida a entrada       */
            printf("Par %d - introduza a e b (inteiros positivos, a < b): ", par);
            scanf("%d %d", &a, &b);
        } while (a <= 0 || b <= 0 || a >= b);

        printf("Pares de %d ate %d: ", a, b);
        for (n = a; n <= b; n++)
            if (n % 2 == 0)                    /* resto 0 -> par         */
                printf("%d ", n);
        printf("\n");
    }
    return 0;
}
