#include "main.h"

/**
 * main - Prints _putchar.
 *
 * Return: Always 0 (Success)
 */
int main(void)
{
	int i = 0;
	char w[] = "_putchar";

	while (w[i] != '\0')
	{
		_putchar(w[i]);
		i++;
	}

	_putchar('\n');

	return (0);
}
