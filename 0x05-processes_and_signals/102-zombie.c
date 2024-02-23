#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>

/**
 * infinite_while - Creates an infinite loop
 *
 * Return: Always returns 0
 */
int infinite_while(void)
{
	while (1)
		sleep(1);
	return (0);
}

/**
 * main - Entry point of the program
 *
 * Return: Always returns 0
 */
int main(void)
{
	int zombies;
	pid_t child_pid;

	for (zombies = 0; zombies < 5; zombies++)
	{
		child_pid = fork();

		if (child_pid == -1)
			perror("Fork error"),
				exit(EXIT_FAILURE);

		if (child_pid == 0)
			printf("Zombie process created, PID: %d\n", getpid()),
				exit(EXIT_SUCCESS);
		else
			sleep(1);
	}

	/* This will give us a chance to observe the zombie processes using tools like ps */
	infinite_while();

	return (EXIT_SUCCESS);
}
