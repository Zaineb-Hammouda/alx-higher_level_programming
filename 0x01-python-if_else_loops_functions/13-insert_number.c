#include "lists.h"
#include <stdlib.h>
#include <stdio.h>
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
	newNode->n = number;
	newNode->next = NULL;
	if (*head == NULL)
	{
		*head = newNode;
		return (newNode);
	}
	while (traverse != NULL)
	{
		if (traverse->n < number && traverse->next->n > number)
		{
			newNode->next = traverse->next;
			traverse->next = newNode;
			break;
		}
		else if (traverse->n > number)
		{
			*head = newNode;
			newNode->next = traverse->next;
			break;
		}
		traverse = traverse->next;
	}
	if (newNode->next == NULL)
		traverse->next = newNode;
	return (newNode);
}
