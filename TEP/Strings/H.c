#include <stdio.h>

int main()
{
	int N;
	scanf("%d", &N);
	
	int xs[N];
	int ys[N];
	int soma[N];
	
	
	for(int i = 0; i < N; i++)
	{
		scanf("%d", &xs[i]);
	}
	
	for(int i = 0; i < N; i++)
	{
		scanf("%d", &ys[i]);
	}
	
	// soma dos vetores
	
	for(int i = 0; i < N; i++)
	{
		soma[i] = xs[i] + ys[i];
		printf("%d ", soma[i]);
	}
	
	
	return 0;
}
