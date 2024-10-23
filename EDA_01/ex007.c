#include <stdio.h>

int main()
{
    while(1)
    {
        char opc;
        float F, C;

        printf("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n");
        printf("'C' - Fahrenheit para Celsius\n");
        printf("'F' - Celsius para Fahrenheit\n");
        printf("'S' - Sair\n");
        printf("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n");

        scanf(" %c", &opc);

        switch(opc)
        {
        case 'C':
        case 'c':
            printf("Temperatura em F: ");
            scanf("%f", &F);

            C = 5.0/9.0 * (F - 32);

            printf("\n");
            printf("F: %.2f -> C: %.2f\n", F, C);
            break;

        case 'F':
        case 'f':
            printf("Temperatura em C: ");
            scanf("%f", &C);

            F = 9.0/5.0 * C + 32;

            printf("\n");
            printf("C: %.2f -> F: %.2f\n", C, F);
            break;

        case 'S':
        case 's':
            printf("Programa finalizado com sucesso!\n");
            return 0;

        default:
        printf("Opção inválida. Tente novamente\n");
            break;
        }
    }
}