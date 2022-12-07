#include "lists.h"

/**
 * is_palindrome - checks if singly linked list is a palindrome
 * @head: pointer to a pointer of the start of the list
 *
 * Return: 1 if palindrome otherwise 0
 */
int is_palindrome(listint_t **head)
{
        listint_t *current;

        current = *head;
        int i, k, j;

        i = 0;
        while (current != NULL)
        {
                current = current->next;
                i++;
        }
        current = *head;
        int s[i];
        j = 0;
        while (current != NULL)
        {
                s[j++] = current->n;
                current = current->next;
        }
        int p[i];
        k = 0;
        j = i-1;
        while (k < i)
        {
                p[k] = s[j];
                k++;
                j--;
        }
        j = 0;
        while (j < i)
        {
                if (s[j] != p[j])
                        return (0);
                j++;
        }
        return (1);
}
