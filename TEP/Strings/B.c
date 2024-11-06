#include <stdio.h>

int main()
{
	int A, B, C;
	scanf("%d %d %d", &A, &B, &C);
	
	if(A == B && B != C)
	{
		printf("C\n");
	}
		else if(B == C && C != A)
		{
			printf("A\n");
		}
			else if(A == C && C != B)
			{
				printf("B\n");
			}
				else
				{
					printf("empate\n");
				}
	
	
	return 0;
}
