#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: the singly linked list to scan through
 * Return: 0 if no cycle, 1 if there is cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *white = list;
	listint_t *black = list;
	int out = 0;
	
	while ((white && black) && black->next)
	{
		white = white->next;
		if (black->next ||black->next->next)
			black = black->next->next;
		else
			break;
		if (white == black)
		{
			out = 1;
			break;
		}
	}
	return (out);
}
