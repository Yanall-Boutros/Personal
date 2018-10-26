#include "List.h"
#include <math.h>
#include <stdlib.h>
#include <stdio.h>

int isPrime(long double num)
{
	int lim = (int)sqrt(num)+1;
	for (int i = 2; i < lim; i++)
	{
		if (fmod(num, (long double)i) == 0)
		{
			return 0;
		}
	}
	return 1;
}

List genFactors(long double num)
{
	List F = newList();
	int lim = (int)sqrt(num)+1;
	for (int i = 2; i < lim; i++)
	{
		if (fmod(num, (long double)i) == 0)
		{
			if (isPrime(i))
			{
				append(F, num/(long double)i);
				num = num/(long double)i;
				i = 2;
			}
		}
	}
	return F;
}

int main()
{
	long double num = 600851475143;
	List F = genFactors(num);
	printList(stdout, F);
	return 0;
}
