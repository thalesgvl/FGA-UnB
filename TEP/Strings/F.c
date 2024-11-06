#include <stdio.h>

int main()
{
	int N;
	scanf("%d", &N);
	int ns[N];
	
	int menorN = 0, menorI = 0;
	
	for(int i = 0; i < N; i++)
	{
		scanf("%d", &ns[i]);
	
		if(i == 0)
		{
			menorN = ns[i];
			menorI = i;
		}
		else if(menorN > ns[i])
		{
			menorN = ns[i];
			menorI = i;
		}
	}
	
	printf("%d\n", menorI);
	return 0;
}
