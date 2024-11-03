#include<stdio.h>

int main()
{
	int num, htrab;
	double valorh;
	scanf("%d %d %lf", &num, &htrab, &valorh);
	
	printf("NUMBER = %d\n", num);
	printf("SALARY = U$ %.2lf\n", htrab * valorh);
	
	return 0;
} 
