#include <stdio.h>

double calcularAreaTriangulo(double A, double C)
{
	return A * C / 2; 
}

double calcularAreaCirculo(double C)
{
	return 3.14159 * C * C;
}

double calcularAreaTrapezio(double A, double B, double C)
{
	return (A + B) * C / 2;
}

double calcularAreaQuadrado(double B)
{
	return B * B;
}

double calcularAreaRetangulo(double A, double B)
{
	return A * B;
}
int main()
{
	double A, B, C;
	scanf("%lf %lf %lf", &A, &B, &C);
	
	printf("TRIANGULO: %.3lf\n", calcularAreaTriangulo(A, C));
	printf("CIRCULO: %.3lf\n", calcularAreaCirculo(C));
	printf("TRAPEZIO: %.3lf\n", calcularAreaTrapezio(A, B, C));
	printf("QUADRADO: %.3lf\n", calcularAreaQuadrado(B));
	printf("RETANGULO: %.3lf\n", calcularAreaRetangulo(A, B));
	return 0;
}
