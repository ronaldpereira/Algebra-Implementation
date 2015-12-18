//Para compilar o programa, use o comando no Terminal do Linux : gcc number-inverser.c -o number-inverser
//Para executar o programa, use o comando no Terminal do Linux : ./number-inverser

#include <stdio.h>
#include <stdlib.h>

int main()
{
	int a, p, inv, aux, b;
	printf("\nAlgebra A - 2015/2\n\nTrabalho Pratico - Parte 2 Exercicio 1\n\nAutor: Ronald Davi Rodrigues Pereira - 2015004437\n\nCalculo do inverso de um numero\n\n");
	
	printf("Insira o número 'a' de qual devera ser calculado o inverso:\n>");
	scanf("%d", &a);
	printf("Insira o numero primo 'p' para o calculo do inverso de 'a':\n>");
	scanf("%d", &p);

	if(a % p == 0)
	{
		printf("P eh um divisor de A.\n");
		return 0;
	}



	else
	{
		for(b = 0; b < p; b++)
		{
			aux = (a * b) % p;
			if((aux % p) == 1)
			{
				printf("\na = %d\np = %d\nInverso de a = %d\n", a, p, b);
				printf("\nO inverso de %d em %d eh %d, pois %d * %d eh equivalente a 1 (mod %d)\n", a, p, b, a, b, p);
				break;
			}
		}
		if(b == p)
			printf("\nO numero a = %d nao possui inverso em p = %d\n", a, p);
	}

	return 0;
}
