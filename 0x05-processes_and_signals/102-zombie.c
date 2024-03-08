#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
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
	int i;
	pid_t ID;

	for (i = 0; i <= 4; i++)
	{
		ID = fork();
		if (ID == -1 || ID == 0)
			exit(1);
		else
			printf("Zombie process created, PID: %d\n", ID);
	}

	infinite_while();
	return (0);
}
