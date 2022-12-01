#include "lists.h"

/**
 *insert_node: insert node into a sorted array
 * @head: head
 * @number: number to insert
 *
 */
listint_t *insert_node(listint_t **head, int number)
{
        listint_t *current, *temp, *new;
        int i, j;

        current = *head;
        i = 0;
        while (current->n < number)
        {
                current = current->next;
                i++;
        }
        temp = *head;
        j = 0;
        while (j < i - 1)
        {
                temp = temp->next;
                j++;
        }
        temp->next = NULL;
        new = add_nodeint_end(&temp, number);
        new->next = current;
        return (new);
}
