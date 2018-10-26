#include "List.h"

#define MAX_LEN 1000

typedef struct NodeObj
{
	int item;
	struct NodeObj* next;
	struct NodeObj* prev;
} NodeObj;

typedef NodeObj* Node;

typedef struct ListObj
{
	int len;
	int cursor_index;

	Node front;
	Node back;
	Node cursor;
} ListObj;
//-------------------------------------------------------------------
//Constructors-Destructors
//-------------------------------------------------------------------
Node newNode(int x)
{
	Node N = malloc(sizeof(NodeObj));
	assert (N != NULL);
	N->item = x;
	N->next = NULL;
	N->prev = NULL;
	return N;
}

void freeNode(Node* pN)
{
	if (pN != NULL && *pN != NULL)
	{
		free(*pN);
		*pN = NULL;
	}
}

List newList()
{
	List L = malloc(sizeof(ListObj));
	assert (L != NULL);
	L->len = 0;
	L->cursor_index = -1;
	L->front = NULL;
	L->back = NULL;
	L->cursor = NULL;

	return L;
}

void freeList(List* pL)
{
	if (pL != NULL && *pL != NULL)
	{
		//clear the list
		clear(*pL);
		//free head and tail
		//deconstruct the List
		free(*pL);
		*pL = NULL;
	}
}
//-------------------------------------------------------------------
//Access functions
//-------------------------------------------------------------------
int length(List L)
{
	return L->len;
}

int index(List L)
{
	if (L->cursor == NULL)
	{
		return -1;
	}
	return L->cursor_index;
}

int front(List L)
{
	if (length(L) > 0)
	{
		return L->front->item;
	}
	else
	{
		assert("Cannot retrieve front element from List of length < 1");
		return -1;
	}
}

int back(List L)
{
	if (length(L) > 0)
	{
		return L->back->item;
	}
	else
	{
		assert("Cannot retrieve back element from List of length < 1");
		return -1;
	}
}

int get(List L)
{
	if (length(L) > 0 && index(L) != -1)
	{
		return L->cursor->item;
	}
	else
	{
		if (index(L) == -1)
		{
			assert("Cannot retrieve NULL cursor element");
			return -1;
		}
		else
		{
			assert("Cannot retrieve cursor element from List of length < 1");
			return -1;
		}
	}
}

int equals(List A, List B)
{
	if (length(A) != length(B))
	{
		return 0;
	}
	else
	{
		moveFront(A);
		moveFront(B);
		while(index(A) >= 0)
		{
			if (get(A) != get(B))
			{
				return 0;
			}
			moveNext(A);
			moveNext(B);
		}
	}
	return 1;
}
//-------------------------------------------------------------------
//Manipulation procedures
//-------------------------------------------------------------------
void clear(List L)
{
	while (length(L) > 0)
	{
		deleteFront(L);
	}
}

void moveFront(List L)
{
	if (length(L) != 0)
	{
		L->cursor = L->front;
		L->cursor_index = 0;
	}
}

void moveBack(List L)
{
	if (length(L) != 0)
	{
		L->cursor = L->back;
		L->cursor_index = length(L)-1;
	}
}

void movePrev(List L)
{
	if (index(L) != 0)
	{
		L->cursor = L->cursor->prev;
		L->cursor_index--;
	}
	else if (index(L) == 0)
	{
		L->cursor = NULL;
		L->cursor_index = -1;
	}
}

void moveNext(List L)
{
	if (index(L) == length(L) - 1)
	{
		L->cursor = NULL;
		L->cursor_index = -1;
	}
	else if (index(L) != length(L) - 1)
	{
		
		L->cursor = L->cursor->next;
		L->cursor_index++;
	}
}

void prepend(List L, int data)
{
	Node N = newNode(data);
	if (length(L) == 0)
	{
		L->front = L->back = N; 
	}
	else
	{

		if (index(L) >= 0)
		{
			L->cursor_index++;
		}
		N->next = L->front;
		L->front->prev = N;
		L->front = N;
	}
	L->len++;
}

void append(List L, int data)
{
	Node N = newNode(data);
	if (length(L) == 0)
	{
		L->front = L->back = N; 
	}
	else
	{
		N->prev = L->back;
		L->back->next = N;
		L->back = N;
	}
	L->len++;
}

void insertBefore(List L, int data)
{
	if (length(L) > 0 && index(L) >= 0)
	{
		if (L->cursor == L->front)
		{
			prepend(L, data);
			return;
		}
		Node N = newNode(data);
		N->next = L->cursor;
		N->prev = L->cursor->prev;
		L->cursor->prev->next = N;
		L->cursor->prev = N;
		L->len++;
		L->cursor_index++;
	}
}

void insertAfter(List L, int data)
{
	if (length(L) > 0 && index(L) >= 0)
	{
		if (L->cursor == L->back)
		{
			append(L, data);
			return;
		}
		Node N = newNode(data);
		N->prev = L->cursor;
		N->next = L->cursor->next;
		L->cursor->next->prev = N;
		L->cursor->next = N;
		L->len++;
	}
}

void deleteFront(List L)
{
	if (length(L) == 1)
	{
		Node N = L->front;
		L->front = L->back = L->cursor = NULL;
		L->len = 0;
		L->cursor_index = -1;
		freeNode(&N);
	}
	else
	{
		if (L->cursor == L->front) {
			L->cursor = NULL;
			L->cursor_index = -1;
		}
		Node N = L->front;
		L->front = L->front->next;
		L->front->prev = NULL;
		freeNode(&N);
		L->len--;
		if (L->cursor != NULL) L->cursor_index--;
	}
}

void deleteBack(List L)
{

	if (length(L) == 1)
	{
		Node N = L->front;
		L->front = L->back = L->cursor = NULL;
		L->len = 0;
		L->cursor_index = -1;
		freeNode(&N);
	}
	else
	{
		if (L->cursor == L->back) {
			L->cursor = NULL;
			L->cursor_index = -1;
		}
		Node N = L->back;
		L->back = L->back->prev;
		L->back->next = NULL;
		freeNode(&N);
		L->len--;
	}
}

void delete(List L)
{
	if (length(L) > 0 && index(L) >= 0)
	{
		if (L->cursor == L->front) //if we're not at the front...
		{
			deleteFront(L);
			return;
		}
		else if (L->cursor == L->back)
		{
			deleteBack(L);
			return;	
		}
		L->cursor->prev->next = L->cursor->next;
		L->cursor->next->prev = L->cursor->prev;
		freeNode(&(L->cursor)); //free our node
		L->cursor_index = -1;
		L->len--;
	}
}
//-------------------------------------------------------------------
//Other operations
//-------------------------------------------------------------------
void printList(FILE* out, List L)
{
	for (Node N = L->front; N != NULL; N = N->next)
	{
		fprintf(out, "%d ", N->item);
	}
	fprintf(out, "\n");
}

List copyList(List L)
{
	List M = newList();
	for (Node N = L->front; N != NULL; N = N->next)
	{
		append(M, N->item);
	}
	return M;
}

List concatList(List A, List B)
{
	List M = newList();
	moveFront(A);
	while (index(A) >= 0)
	{
		append(M, get(A));
		moveNext(A);
	}
	moveFront(B);
	while (index(B) >= 0)
	{
		append(M, get(B));
		moveNext(B);
	}
	return M;
}
