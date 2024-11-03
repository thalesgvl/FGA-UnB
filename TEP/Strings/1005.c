#include <stdio.h>

double MEDIA(double A, double B)
{
	double MEDIA = (3.5 * A + 7.5 * B) / 11;
	return MEDIA;
}

int main()
{
	double A, B;
	scanf("%lf %lf", &A, &B);
	printf("MEDIA = %.5lf", MEDIA(A, B));
	return 0;
}
