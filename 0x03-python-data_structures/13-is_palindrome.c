#include "lists.h"

/**
 * is_palindrome -  checks if a singly linked list is a palindrome.
 * @head: pointer to pointer to head of singly linked list
 * Return: 0 if not palindrome or 1 if it is
 */
int is_palindrome(listint_t **head)
{
	int buffer[12];
	unsigned int i = 0, mid_len, j;
	listint_t *temp = *head;

	if (*head == NULL || head == NULL)
		return (1);
		
	while (temp)
	{
		buffer[i] = temp->n;
		temp = temp->next;
		i++;
	}
	mid_len = i / 2;
	i -= 1;
	
	for (j = 0; j < mid_len; i--, j++)
	{
		if (buffer[j] != buffer[i])
			return (0);
	}
	return (1);
}
