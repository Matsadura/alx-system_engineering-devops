#include <stdio.h>
#include <unistd.h>

/**
 * infinite_while - a function that loops infinitly
 * Return: 0 ( Success )
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - Creates 5 zombie processes
 * Return: 0 ( Success )
 */
int main(void)
{
	int id1, id2, id3;

	id1 = fork();
	if (id1 != 0)
	{
		id2 = fork();
		if (id2 != 0)
		{
			id3 = fork();
			if (id3 != 0)
				fork();
		}
	}
	printf("Zombie process created, PID: %d\n", getpid());
	infinite_while();
	return (0);
}
