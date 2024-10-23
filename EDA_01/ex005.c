#include <stdio.h>

int main()
{
    int opc;
    double n1, n2, r;

    while (1)
    {
        printf("-=-=-=-=-=-=-=-=-=-=-\n");
        printf("Escolha uma opção:\n");
        printf("1 - SOMA\n");
        printf("2 - SUBTRAÇÃO\n");
        printf("3 - MULTIPLICAÇÃO\n");
        printf("4 - DIVISÃO\n");
        printf("0 - FINALIZAR\n");
        printf("-=-=-=-=-=-=-=-=-=-=-\n");

        printf("Digite sua escolha: ");


        scanf("%d", &opc);

        if (opc == 0)
        {
            printf("Programa finalizado com sucesso!\n");
            return 0;
        }
        
        printf("Primeiro valor: ");
        scanf("%lf", &n1);

        printf("Segundo valor: ");
        scanf("%lf", &n2);

        switch (opc)
        {
        case 1:
            r = n1 + n2;
            printf("\n");
            printf("%.2lf + %.2lf = %.2lf\n", n1, n2, r);
            break;
        case 2:
            r = n1 - n2;
            printf("\n");
            printf("%.2lf - %.2lf = %.2lf\n", n1, n2, r);
            break;
        case 3:
            r = n1 * n2;
            printf("\n");
            printf("%.2lf * %.2lf = %.2lf\n", n1, n2, r);
            break;
        case 4:
            r = n1 / n2;
            printf("\n");
            printf("%.2lf / %.2lf = %.2lf\n", n1, n2, r);
            break;
        default:
            printf("\n");
            printf("Opção inválida. Tente novamente\n");
            return 1;
        }
    }
    return 0;
}