#include <stdio.h>

int main()
{
    int TS[4];
    int maxt = 0;

    scanf("%d %d %d %d", &TS[0], &TS[1], &TS[2], &TS[3]);


    for(int i = 0; i < 4; i++)
    {
        if(i == 0)
            maxt += TS[i];

        else
            maxt += TS[i] - 1;
    }

    printf("%d\n", maxt);

    return 0;
}