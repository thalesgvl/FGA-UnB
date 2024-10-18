#include <stdio.h>

double media(double a[5])
{
	double soma = 0;
	for(int i = 0; i < 5; i++)
	{	
		soma += a[i];
	}

	return soma/5;
}

int main()
{
	double ns[5];
	for(int i = 0; i < 5; i++)
	{	
		printf("Elem %d\n", i+1);
		scanf("%lf", &ns[i]);
	}
	printf("%lf\n", media(ns));
	return 0;
}
