#include <stdio.h>
#include <string.h>
#include <math.h>

int convBinDec(char numStr[])
{
	int decimal = 0;
	int length = strlen(numStr);

	for(int i = 0; i < length; i++ )
	{
		int bit = numStr[i] - '0';  //converte char para int
		if(bit == 1)
			decimal += pow(2, length - 1 - i);
	}
	return decimal;
}

int main()
{
	char bin[100];
	printf("Número em binário: ");
	scanf("%s", bin);

	printf("%d\n", convBinDec(bin));
	return 0;
}
