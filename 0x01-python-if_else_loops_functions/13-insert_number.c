#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * insert_node - inserts a numuber into a linked list
 * @head: head of the linked linked
 * @number: number to be inserted in linked list
 * Return: address of new node, or NULL-failure
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node;
	listint_t *nxt;

	nxt = *head;

	node = malloc(sizeof(listint_t));
	if (node == NULL)
		return (NULL);
	node->n = number;

	if (*head == NULL || (*head)->n > number)
	{
		node->next = *head;
		*head = node;
		return (node);
	}
	while (nxt->next != NULL)
	{
		if ((nxt->next)->n >= number)
		{
			node->next = nxt->next;
			nxt->next = node;
			return (node);
		}
		nxt = nxt->next;
	}
	node->next = NULL;
	nxt->next = node;
	return (node);
}
