#include <stdio.h>

int main()
{
    int cin = 0;
    int cout = 0;
    int N;

    scanf("%d", &N);

    for(int i = 0; i < N; i++)
    {
        int X;

        scanf("%d", &X);

        if(X >= 10 && X <= 20)
            cin++;
        else
            cout++;
    }

    printf("%d in\n", cin);
    printf("%d out\n", cout);

    return 0;
}