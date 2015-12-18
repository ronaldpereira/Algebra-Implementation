//Para compilar o programa, use o comando no Terminal do Linux : gcc phi-calculation.c -lm -o phi-calculation
//Para executar o programa, use o comando no Terminal do Linux : ./phi-calculation

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#define MAX 10000

int main()
{
	int k, i, j, l = 0, verif, fatores[MAX], phi = 1, aux;

	printf("\nAlgebra A - 2015/2\n\nTrabalho Pratico - Parte 2 Exercicio 2\n\nAutor: Ronald Davi Rodrigues Pereira - 2015004437\n\nCalculo do Phi(k)\n\n");
	
	printf("Insira o número 'k':\n>");
	scanf("%d", &k);

	for(i = 2; i <= k; i++)
	{
		verif = 0;
		for(j = 2; j < i; j++)
		{
			if(i % j == 0)
			{
				verif++;
				break;
			}
		}
		if(verif == 0)
		{
			if(k % i == 0)
			{
				fatores[l] = i;
				l++;
				k = k/i;
				i = 1;
			}
		}
	}

	for(i = 0; i < l; i++)
	{
		aux = 1;
		for(j = i+1; j < l; j++)
		{
			if(fatores[i] == fatores[j])
			{
				aux++;
				fatores[j] = -1-i;
			}
		}
		if(aux == 1 && fatores[i] > 0)
			phi *= fatores[i] - 1;
		else if(aux != 0 && fatores[i] > 0)
			phi *= pow(fatores[i],aux) - pow(fatores[i], (aux-1));
	}
	printf("\nPhi(k) = %d\n", phi);	

	return 0;
}
