#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - function will insert a number into a sorted
 * singly list
 * @head: pointer the inserted node
 * @number: int valuse to be stored in n
 * Return: Return: the address of the new node, or
 * NULL if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head, *new_node;

	new_node = malloc(sizeof(listint_t));

	if (!new_node)
	{
		return (NULL);
	}

	new_node->n = number;

	if (current == NULL || current->n >= number)
	{
		new_node->next = current;
		*head = new_node;
		return (new_node);
	}

	while (current && current->next && current->n < number)
	{
		current = current->next;
	}

	new_node->next = current->next;
	current->next = new_node;
	return (new_node);
}
