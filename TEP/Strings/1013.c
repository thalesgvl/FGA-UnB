#include <stdio.h>

int maiorAB(int a, int b, int c)
{
	int maior = a;
	if (maior < b)
	{
		maior = b;
	}else if (maior < c)
	{
		maior = c;
	}
	return maior;
}
		
int main()
{
	int a, b, c;
	scanf("%d %d %d", &a, &b, &c);
	
	printf("%d eh o maior\n", maiorAB(a, b, c));
	return 0;
}
