#include <stdio.h>

int main()
{
    int N, MENOR, POS;

    scanf("%d", &N);

    int X[N];

    for(int i = 0; i < N; i++)
        scanf("%d", &X[i]);

    for(int i = 0; i < N; i++)
    {
        if(i == 0)
        {
            MENOR = X[i];
            POS = i;
        }
        else if(X[i] < MENOR)
        {
            MENOR = X[i];
            POS = i;
        }
    }

    printf("Menor valor: %d\n", MENOR);
    printf("Posicao: %d\n", POS);
    
    return 0;
}