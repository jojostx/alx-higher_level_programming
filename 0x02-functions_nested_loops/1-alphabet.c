#include "main.h"

/**
 * print_alphabet - Prints the alphabet in lowercase.
 *
 * Return: Nothing
 */
void print_alphabet(void)
{
	int i = 0;
	char a[] = "abcdefghijklmnopqrstuvwxyz";

	while (a[i] != '\0')
	{
		_putchar(a[i]);
		i++;
	}
	_putchar('\n');
}
