#include "lists.h"

/**
 * check_cycle - check if single linked list has a cycle in it
 * @list: singly linked list
 *
 * Return: 1 if present otherwise 0
 */
int check_cycle(listint_t *list)
{
	listint_t *current;
	unsigned int i, n;

	current = list;
	n = 0;
	while ((current !=NULL) && (current->next != list))
	{
		current = current->next;
		n++;
	}
	i = 0;
	current = list;
	while (i < n - 1)
	{
		current = current->next;
		i++;
	}
	if (current->next != NULL)
		current = current->next;
	if (current->next == list)
		return (1);
	else
		return (0);
}
