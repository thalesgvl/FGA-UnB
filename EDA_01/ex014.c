#include <stdio.h>
#include <stdlib.h>

int main()
{
    int *ptr = malloc(sizeof(int));
    *ptr = 10;
    printf("%d\n", *ptr);
    free(ptr);
    printf("%d\n", *ptr);
    return 0;
}