#include <stdio.h>

double calcIMC(float p, float h)
{
	double imc = p/(h*h);
	return imc;
}

int main()
{
	float peso, altura;
	printf("Peso: \n");
	scanf("%f", &peso);

	printf("Altura: \n");
	scanf("%f", &altura);

	printf("%.2lf\n",calcIMC(peso, altura));

	return 0;
}
