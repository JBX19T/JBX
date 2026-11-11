#include <stdio.h>

int main(void)
{
    int n;

    printf("Numeros impares entre 100 e 400:\n");
    for (n = 101; n < 400; n += 2)     /* 101, 103, ..., 399 */
        printf("%d ", n);
    printf("\n");
    return 0;
}
