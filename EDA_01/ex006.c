#include <stdio.h>

int main()
{
	long long n;
	scanf("%lld", &n);
	
	if(n < 2)
		{
		printf("%lld não é primo\n", n);
		return 0;
		}
	if(n == 2)
		{
		printf("%lld é primo\n", n);
		return 0;
		}
	if(n % 2 == 0)
		{
		printf("%lld não é primo\n", n);
		return 0;
		}
	for(long long d = 3; d * d <= n; d += 2)
		{
		if (n % d == 0)
			{
			printf("%lld não é primo\n", n);
			return 0;
			}
		}
	printf("%lld é primo\n", n);
	
	return 0;
}
