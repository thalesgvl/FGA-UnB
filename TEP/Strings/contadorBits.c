#include <stdio.h>

int lsd(int n)
{
	return n & -n;
}

int erase_lsd(int n)
{
	return n - lsd(n);
}

int bit_count(int n)
{
	int count = 0;
	
	while(n)
	{
		++count;
		n = erase_lsd(n);	
	}	
	
	return count;
}
int main()
{
	int n;
	scanf("%d", &n);
	
	printf("Contagem de bits de %d é %d\n", n, bit_count(n));
	
	return 0; 
}
