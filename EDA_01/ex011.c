#include <stdio.h>

int main()
{
    FILE *fp;
    char ch;

    fp = fopen("teste.txt", "r");
    if (fp == NULL) 
    {
        printf("Erro ao abrir o arquivo.\n");
        return 1;
    }

    while(1)
    {
        ch = fgetc(fp);
        if(ch == EOF)
            break;
        printf("%c", ch);
    }
    fclose(fp);

    return 0;
}