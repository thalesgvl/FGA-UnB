#include <stdio.h>
#include <math.h>
typedef struct _Ponto
{
	double x;
	double y;
}Ponto;

double distancia(Ponto a, Ponto b)
{
	double d = sqrt(pow(b.x - a.x, 2) + pow(b.y - a.y, 2));
	return d;
}

int main()
{
	Ponto p1, p2;
	scanf("%lf %lf", &p1.x, &p1.y); 
	scanf("%lf %lf", &p2.x, &p2.y);
	
	printf("%.4lf\n", distancia(p1, p2));
	return 0;
}
