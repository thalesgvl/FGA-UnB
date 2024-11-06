#include <stdio.h>

int main()
{
	int n;
	scanf("%d", &n);
	
	for(int i = 0; i < n; i++)
	{
	int seq = 2*i + 1;
	int space = n - i - 1;
		for (int j = 0; j < space; j++)
		{
			printf(" ");
		}
		for(int k = 0; k < seq; k++)
		{
			printf("*");
		}	
	printf("\n");
	
	}
	return 0;
}
