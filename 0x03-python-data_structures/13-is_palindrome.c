#include "lists.h"
#include <stdio.h>

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
 * is_palindrome - checks if singly linked list is a palindrome
 * @head: pointer to a pointer of the start of the list
 *
 * Return: 1 if palindrome otherwise 0
 */
int is_palindrome(listint_t **head)
{
        listint_t *current, *new;
        int i, j;

        current = *head;

        new = NULL;
        i = 0;
        while (current != NULL)
        {
                current = current->next;
                i++;
        }
        j = i / 2;
        i = 0;
        current = *head;
        while (i < j)
        {
                current = current->next;
                i++;
        }
        while (current != NULL)
        {
                add_nodeint(&new, current->n);
                current = current->next;
        }

        current = *head;
        while (new->next != NULL && current->next != NULL)
        {
                if (current->n != new->n)
                {
                        free_listint(new);
                        return (0);
                }
                current = current->next;
                new = new->next;
        }
        if (current->n != new->n)
        {
                free_listint(new);
                return (0);
        }
        free_listint(new);
        return (1);
}

