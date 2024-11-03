#include <stdio.h>

double MEDIA(double A, double B, double C)
{
	double MEDIA = (2 * A + 3 * B + 5 * C) / 10;
	return MEDIA;
}

int main()
{
	double A, B, C;
	scanf("%lf %lf %lf", &A, &B, &C);
	
	printf("MEDIA = %.1lf\n", MEDIA(A, B, C));
}
