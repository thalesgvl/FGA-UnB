#include <stdio.h>

unsigned long long memo[1] = {0};

unsigned long long fibr(int N)
{
	if (N == 0)
    {
        return 0;
    }
    else if (N == 1 || N == 2)
    {
        return 1;
    }
		
	if(!memo[N])
	{
		memo[N] = fibr(N - 1) + fibr(N - 2);
	}
	return memo[N];
}

int main()
{
    int N;
    scanf("%d", &N);

	unsigned long long fib = fibr(N);
    printf("Fib(%d) = %llu\n", N, fib);

    return 0;
}
