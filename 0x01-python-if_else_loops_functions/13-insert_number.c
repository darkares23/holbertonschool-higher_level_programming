#include "lists.h"

/**
 * insert_node - insert node in correctly sorted position in list
 * @head: pointer to head of linked list
 * @number: node value
 * Return: New node or NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp = NULL, *current = *head;
	listint_t *newnode = NULL;

	newnode = malloc(sizeof(listint_t));
	if (newnode == NULL)
		return (NULL);
	newnode->n = number;
	newnode->next = NULL;

	if ((number < (*head)->n) || !(*head))
	{
		temp = *head;
		*head = newnode;
		newnode->next = temp;
		return (newnode);
	}
	while (current!= NULL)
	{
		if (number < current->next->n)
		{
			temp = current->next;
			current->next = newnode;
			newnode->next = temp;
			return (newnode);
		}
		if (current->next == NULL)
		{
			current->next = newnode;
			return (newnode);
		}
		current = current->next;
	}
	free(newnode);
	return (NULL);
}