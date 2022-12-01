#include "lists.h"

/**
 * add_nodeint - adds a new node at the beginning of a listint_t list
 * @head: pointer to a pointer of the start of the list
 * @n: integer to be included in node
 * Return: address of the new element or NULL if it fails
 */
listint_t *add_nodeint(listint_t **head, const int n)
{
    listint_t *new;

    new = malloc(sizeof(listint_t));
    if (new == NULL)
        return (NULL);

    new->n = n;
    new->next = *head;
    *head = new;

    return (new);
}
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
        if (number < current->n)
        {
                current = add_nodeint(&current, number);
                (*head) = current;
                return (*head);
        }
        while (current->next != NULL)
        {
                current = current->next;
        }
        if (current->next == NULL && number > current->n)
        {
                add_nodeint_end(&current, number);
                return (current);
        }
        i = 0;
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
