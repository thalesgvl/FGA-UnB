#include <stdio.h>

int main()
{
	char nome[100];
	scanf("%99[^\n]", nome);
	
	double salario;
	scanf("%lf", &salario);
	double vendas;
	scanf("%lf", &vendas);
	
	printf("TOTAL = R$ %.2lf", salario + 0.15 * vendas);	
	
	return 0;
}
