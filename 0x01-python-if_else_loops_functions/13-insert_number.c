#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - inserts a number into a sorted singly linked list
 * Return: the address of a new node or NULL if failed
 * @head: pointer to head pointer
 * @number: data to insert
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newNode = malloc(sizeof(listint_t));
	listint_t *traverse = *head;

	if (newNode == NULL)
		return (NULL);
	if (*head == NULL)
	{
		*head = newNode;
		return (newNode);
	}
	newNode->n = number;
	newNode->next = NULL;
	while (traverse != NULL)
	{
		if (traverse->n < number && traverse->next->n > number)
		{
			newNode->next = traverse->next;
			traverse->next = newNode;
		}
		traverse = traverse->next;
	}
	if (newNode == NULL)
		traverse->next = newNode;
	return (newNode);
}
