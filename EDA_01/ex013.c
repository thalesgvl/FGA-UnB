#include <stdio.h>

void swap(int *a, int *b)
{
    int temp = *a;
    *a = *b;
    *b = temp;
}

int main()
{
    int x = 5;
    int y = 10;
    printf("X = %d | Y = %d\n", x, y);

    swap(&x, &y);
    printf("X = %d | Y = %d\n", x, y);

    return 0;
}