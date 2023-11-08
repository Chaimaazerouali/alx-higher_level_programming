#include "/usr/include/python3.4/Python.h"
#include <stdio.h>

/**
 * print_hex_bytes - Print hexadecimal representation of bytes.
 * @bytes: Pointer to the bytes.
 * @length: Length of the bytes.
 *
 * This function prints the hexadecimal representation of a byte array.
 */
void print_hex_bytes(const char *bytes, int length)
{
    int i;

    for (i = 0; i < length - 1; ++i)
    {
        printf("%02x ", (unsigned char)bytes[i]);
    }

    printf("%02x\n", bytes[i]);
}

/**
 * print_python_bytes_info - Print information about Python bytes objects.
 * @p: Python bytes object.
 *
 * This function prints information about Python bytes objects.
 */
void print_python_bytes_info(PyObject *p)
{
    PyBytesObject *byte_obj = (PyBytesObject *)p;
    int size = 0;
    int count_bytes = 0;

    printf("[.] bytes object info\n");

    if (PyBytes_Check(byte_obj))
    {
        size = PyBytes_Size(p);
        count_bytes = size + 1;

        if (count_bytes >= 10)
        {
            count_bytes = 10;
        }

        printf("  size: %d\n", size);
        printf("  trying string: %s\n", byte_obj->ob_sval);
        printf("  first %d bytes: ", count_bytes);
        print_hex_bytes(byte_obj->ob_sval, count_bytes);
        printf("\n");
    }
    else
    {
        printf("  [ERROR] Invalid Bytes Object\n");
    }
}

/**
 * print_python_list_info - Print information about Python lists.
 * @p: Python list object.
 *
 * This function prints information about Python lists.
 */
void print_python_list_info(PyObject *p)
{
    int i = 0, length = 0;
    PyObject *item;
    PyListObject *list_obj = (PyListObject *)p;

    printf("[*] Python list info\n");
    length = PyList_GET_SIZE(p);
    printf("[*] Size of the Python List = %d\n";
    printf("[*] Allocated = %d\n", (int)list_obj->allocated);

    for (; i < length; ++i)
    {
        item = PyList_GET_ITEM(p, i);
        printf("Element %d: %s\n", i, item->ob_type->tp_name);

        if (PyBytes_Check(item))
        
            print_python_bytes_info(item);
        
    }
}

