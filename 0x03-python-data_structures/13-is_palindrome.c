#include "lists.h"

/**
 * is_palindrome - function checks if a list is a palindrome
 * @head: pointer to the head of the list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	if (*head == NULL || (*head)->next == NULL)
		return(1);
	listint_t *slow, *fast = *head;
	listint_t *previous = NULL;
	listint_t *part2;

	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		previous = slow;
		slow = slow->next;
	}

	if (fast != NULL)
	{
		part2 = slow->next;
		slow->next = NULL;
	}
	else
	{
		part2 =slow;
		previous->next = NULL;
	}
	
	listint_t *current = part2;
	listint_t *next = NULL;
	listint_t *previous2 = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = previous2;
		previous2 = current;
		current = next;
	}

	part2 = previous2;

	listint_t *list1 = *head;
	listint_t *list2 = part2;

	while (list1 != NULL && list2 != NULL)
	{
		if (list1->n != list2->n)
			return (0);
		list1 = list1->next;
		list2 = list2->next;
	}
	return (1);
}
