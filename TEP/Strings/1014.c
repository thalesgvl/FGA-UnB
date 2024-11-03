#include <stdio.h>

int main()
{
	int D;
	double L;
	
	scanf("%d %lf", &D, &L);
	printf("%.3lf km/l\n",(double) D / L);
	return 0;
}
