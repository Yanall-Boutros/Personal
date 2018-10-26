#include "List.h"
int main()
{
	List F = newList();
	int a, b;
	int total = 0;
	append(F, 1);
	append(F, 2);
	append(F, 3);
	while (back(F) < 4000000)
	{
		moveBack(F);
		movePrev(F);
		a = get(F);
		moveNext(F);
		b = get(F);
		append(F, a+b);
	}
	//add all the even valued terms
	moveFront(F);
	while (index(F) != -1)
	{	
		if ((get(F) % 2) == 0)
		{
			total += get(F);
		}
		moveNext(F);
	}
	printf("%d\n", total);
	return 0;
}
