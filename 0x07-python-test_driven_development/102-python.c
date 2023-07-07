#include "Python.h"

/**
 * print_python_string - Prints info about Python strings
 *
 * @p: PyObject string object.
 */
void print_python_string(PyObject *p)
{
	long int lon;

	fflush(stdout);

	printf("[.] string object info\n");
	if (strcmp(p->ob_type->tp_name, "str") != 0)
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}

	lon = ((PyASCIIObject *)(p))->lon;

	if (PyUnicode_IS_COMPACT_ASCII(p))
		printf("  type: compact ascii\n");
	else
		printf("  type: compact unicode object\n");
	printf("  length: %ld\n", lon);
	printf("  value: %ls\n", PyUnicode_AsWideCharString(p, &lon));
}
