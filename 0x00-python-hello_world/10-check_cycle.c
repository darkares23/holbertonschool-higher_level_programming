#include "lists.h"

/**
 * check_cycle - check for a cycle in a linked list
 * @list: singly linked list
 * Return: 0 if no cyle found, 1 if a cycle is found
 */

int check_cycle(listint_t *list)
{
	listint_t *rabit = list, *turtle = list;

	while (turtle && rabit && rabit->next)
	{
		turtle = turtle->next;
		rabit = rabit->next->next;
		if (turtle == rabit)
			return (1);
	}
	return (0);
}