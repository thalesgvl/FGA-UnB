#include <stdio.h>

int tempo (int d)
{
	int t = d * 2;
	return t;
}
int main()
{
	int dist;
	scanf("%d", &dist);
	
	printf("%d minutos\n", tempo(dist));
	return 0;
}
