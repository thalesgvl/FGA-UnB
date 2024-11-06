#include <stdio.h>

double litros(int h, int vm)
{
	double l =  (h * vm) / 12.0;
	return l; 
}

int main()
{
	int h, vm;
	scanf("%d %d", &h, &vm);
	
	printf("%.3lf\n", litros(h, vm));
	return 0;
}
