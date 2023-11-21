#include <stdio.h>
#include <stdlib.h>
#include <Python.h>
#include <floatobject.h>

/**
 * print_python_float - Prints information about a Python float object.
 * @p:  Address of the float object PyObject struct.
 */
void print_python_float(PyObject *p)
{
    double dl;

	setbuf(stdout, NULL);
	printf("[.] float object info\n");
	if (strcmp(p->ob_type->tp_name, "float"))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}
    dl = ((PyFloatObject *)p)->ob_fval;
	printf("  value: %s\n",
        PyOS_double_to_string(d, 'r', 0, Py_DTSF_ADD_DOT_0, NULL));
}

/**
 * print_python_bytes - Prints information about a Python bytes object.
 * @p: Address of the bytes object PyObject struct.
 */
void print_python_bytes(PyObject *p)
{
	size_t i, lenh, s;
	char *strg;

	setbuf(stdout, NULL);
	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes"))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	s = ((PyVarObject *)p)->ob_s;
	strg = ((PyBytesObject *)p)->ob_sval;
	lenh =  s + 1 > 10 ? 10 : s + 1;
	printf("  size: %lu\n", s);
	printf("  trying string: %s\n", strg);
	printf("  first %lu bytes: ", lenh);
	for (i = 0; i < lenh; i++)
		printf("%02hhx%s", strg[i], i + 1 < lenh ? " " : "");
	printf("\n");
}

/**
 * print_python_list - prints information about python lists
 * @p: address of pyobject struct
 */
void print_python_list(PyObject *p)
{
	int i;

	setbuf(stdout, NULL);
	printf("[*] Python list info\n");
	if (strcmp(p->ob_type->tp_name, "list"))
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}
	printf("[*] Size of the Python List = %lu\n", ((PyVarObject *)p)->ob_size);
	printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);
	for (i = 0; i < ((PyVarObject *)p)->ob_size; i++)
	{
		printf("Element %d: %s\n", i,
			((PyListObject *)p)->ob_item[i]->ob_type->tp_name);
		if (!strcmp(((PyListObject *)p)->ob_item[i]->ob_type->tp_name, "bytes"))
			print_python_bytes(((PyListObject *)p)->ob_item[i]);
		else if (!strcmp(((PyListObject *)p)->ob_item[i]->ob_type->tp_name, "float"))
			print_python_float(((PyListObject *)p)->ob_item[i]);

	}
}
