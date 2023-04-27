#include "main.h"

/**
 * print_alphabet_x10 - prints 10 times the alphabet,
 * in lowercase, followed by a new line.
 *
 * Return: nothing
 */
void print_alphabet_x10(void)
{
	int t = 10;
	int i = 0;
	char a[] = "abcdefghijklmnopqrstuvwxyz";

	while (t > 0)
	{
		while (a[i] != '\0')
		{
			_putchar(a[i]);
			i++;
		}
		_putchar('\n');
		i = 0;
		t--;
	}
}
