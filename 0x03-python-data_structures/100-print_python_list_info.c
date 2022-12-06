#include <stdio.h>
#include "Python.h"

/**
 * print_list - print list from python
 * @list: list
 *
 */
void print_list(PyObject *list)
{
        PyListObject *l;
        int i;

        printf("Hey there\n");

        l = (PyListObject *)list;
        printf("Size of the Python List: %ld\n", sizeof(list));
        printf("[*] Allocated = %ld\n", l->allocated);
        printf("ob_size = %ld\n", l->ob_base.ob_size);
        printf("tpname = %s\n", l->ob_base.ob_base.ob_type->tp_name);
        for (i = 0; i < l->ob_base.ob_size; i++)
        {
                printf("Element %d: %s\n", i, l->ob_item[i]->ob_type->tp_name);
        }
}
