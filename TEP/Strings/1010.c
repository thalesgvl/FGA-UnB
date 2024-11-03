#include <stdio.h>

int main()
{
	int cod, qtd;
	double preco, total = 0;
	
	for (int i = 0; i < 2; i++)
	{
		scanf("%d %d %lf", &cod, &qtd, &preco);
		total += preco * qtd;
	}
	
	printf("VALOR A PAGAR: R$ %.2lf\n", total);
	return 0;
}
