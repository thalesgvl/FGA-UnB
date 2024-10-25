#include <stdio.h>
#include <stdlib.h>
#include <time.h>

const int N = 10;

void mostrarProdutos(int ps[])
{
    printf("-=-=-=-=-=-=-=-=-=-=-=-\n");
    for (int i = 0; i < N; i++)
    {
        printf("Produto %d: %d unidades\n", i, ps[i]);
    }

    printf("-=-=-=-=-=-=-=-=-=-=-=-\n");
}

void comprar(int ps[], int opc)
{   
    if (ps[opc] > 0)
    {
        ps[opc] = ps[opc] - 1;
        printf("Compra realizada!\n");
    }
    else
    {
        printf("Produto sem estoque\n");
    }
}

void estocar(int ps[], int opc, int qtde)
{
    ps[opc] = ps[opc] + qtde;
}

int main()
{
    int produtos[N];
    int opc, qtde;

    srand(time(NULL));

    for (int i = 0; i < N; i++)
    {
        produtos[i] = rand() % 100 + 1;  // gera um número entre 1 e 100
    }

    while (1)
    {
        
        mostrarProdutos(produtos);

        printf("-=-=-=-=-=-=-\n");
        printf("1 - Comprar\n");
        printf("2 - Estocar \n");
        printf("3 - Sair\n");
        printf("-=-=-=-=-=-=-\n");

        scanf("%d", &opc);
        if (opc == 1)
        {
            printf("Qual produtor comprar? ");
            scanf("%d", &opc);
            if (opc >= 0 && opc <= N)
            {
                comprar(produtos, opc);
                printf("Estoque do produto %d: %d\n", opc, produtos[opc]);
            }
            else
                printf("Fora de alcance do vetor produtos\n");
            
        }
        else if (opc == 2)
        {
            printf("Qual produto estocar? ");
            scanf("%d", &opc);
            if (opc >= 0 && opc <= N)
            {
                printf("Quantidade: ");
                scanf("%d", &qtde);
                estocar(produtos, opc, qtde);
                printf("Estoque do produto %d: %d\n", opc, produtos[opc]);
            }
            else
                printf("Fora de alcance do vetor produtos\n");

        }
        else if (opc == 3)
        {   
            printf("Programa finalizado com sucesso!\n");
            break;
        }

        else
            printf("Opção inválida. Tente novamente\n");
    }

    return 0;
}