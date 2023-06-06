#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: pointer to head of the linked list
 * Return: 0 if no cycle, 1 if cycle
 */
#define MAX_SIZE 20
int check_cycle(listint_t *list)
{
	int i = 0;
	listint_t *tmp;
	listint_t **arr = malloc(sizeof(listint_t *) * MAX_SIZE);

	tmp = list;
	tmp = tmp->next;
	arr[0] = list;
	arr[1] = NULL;
	while (tmp)
	{
		for (i = 0; arr[i] != NULL; i++)
		{
			if (arr[i] == tmp)
			{
				free(arr);
				return (1);
			}
		}
		arr[i] = tmp;
		arr[i + 1] = NULL;
		tmp = tmp->next;
	}
	free(arr);
	return (0);
}
