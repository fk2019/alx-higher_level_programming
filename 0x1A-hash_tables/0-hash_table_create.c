#include "hash_tables.h"

/**
 * hash_table_t - creates a hash table
 * @size: size of array
 *
 * Return: pointer to newly created hash table
 */
hash_table_t *hash_table_create(unsigned long int size)
{
        hash_table_t *ht;
        unsigned long int i;

        ht = malloc(sizeof(ht));
        if (ht == NULL)
                return (NULL);
        ht->size = size;
        ht->array = malloc(sizeof(hash_node_t *) * size);
        if (ht->array == NULL)
                return (NULL);
        for (i = 0; i < ht->size; i++)
        {
                ht->array[i] = NULL;
        }
        return (ht);
}
