#include <stdio.h>

int main()
{
	int saque, copia;
	scanf("%d", &saque);
	copia = saque;
	
	int c100, c50, c20, c10, c5, c2, c1 = 0;
	
	while(saque > 0)
	{
		if(saque >= 100)
		{
			++c100;
			saque -= 100;
		}
			else if(saque >= 50)
			{
				c50++;
				saque -= 50;
			}
				else if(saque >= 20)
				{
					c20++;
					saque -= 20;
				}
					else if(saque >= 10)
					{
						c10++;
						saque -= 10;
					}
						else if(saque >= 5)
						{
							c5++;
							saque -= 5;
						}
							else if(saque >= 2)
							{
								c2++;
								saque -= 2;
							}
								else
								{
									c1++;
									saque -= 1;
								}
	}
	printf("%d\n", copia);
    	printf("%d nota(s) de R$ 100,00\n", c100);
    	printf("%d nota(s) de R$ 50,00\n", c50);
	printf("%d nota(s) de R$ 20,00\n", c20);
        printf("%d nota(s) de R$ 10,00\n", c10);
        printf("%d nota(s) de R$ 5,00\n", c5);
        printf("%d nota(s) de R$ 2,00\n", c2);
        printf("%d nota(s) de R$ 1,00\n", c1);
	
	
	return 0;
}
