#include <stdio.h>

void mostrarCinema(int cinema[15][20])
{
    printf("  ");
    for (int j = 0; j < 20; j++)
    {
        printf("%2d ", j + 1); //colunas
    }
    printf("\n");
    
    for (int i = 0; i < 15; i++)
    {
        printf("%2d ", i + 1); //linhas

        for (int j = 0; j < 20; j++)
        {
            printf("%d  ", cinema[i][j]);
        }
        printf("\n");
    }
}

void reservar(int cinema[15][20])
{
    int linha;
    int coluna;

    while (1)
    {
    printf("Qual assento deseja reservar? (especifique fileira e coluna): ");
    scanf("%d %d", &linha, &coluna);

    if (linha >= 0 && linha <= 15 && coluna >= 0 && coluna <= 20)
    {
        if (cinema[linha - 1][coluna - 1] == 0)
        {
            cinema[linha - 1][coluna - 1] = 1;
            printf("Reserva realizada com sucesso!\n");
        }
        else
            printf("Assento ocupado\n");    
    }    
    else
        printf("Assento inválido\n");

    char opc;
    printf("Deseja reservar outro assento? (S/N): ");
    scanf(" %c", &opc);
    if (opc == 'n' || opc == 'N')
    {
        break;
    }
    }
}

int main()
{
    int cinema[15][20];
    // inicializa todos os assentos como "0" (assento vazio)
    for (int i = 0; i < 15; i++)
    {
        for (int j = 0; j < 20; j++)
        {
            cinema[i][j] = 0;
        }
    }

    while (1)
    {
        printf("Menu:\n");
        printf("1. Mostrar cinema\n");
        printf("2. Reservar assento\n");
        printf("3. Sair\n");
        printf("Escolha uma opção: ");
        
        int opcao;
        scanf("%d", &opcao);

        switch (opcao)
        {
            case 1:
                mostrarCinema(cinema);
                break;
            case 2:
                reservar(cinema);
                break;
            case 3:
                printf("Programa finalizado com sucesso!\n");
                return 0;
            default:
                printf("Opção inválida! Tente novamente.\n");
        }
    }
    return 0;
}