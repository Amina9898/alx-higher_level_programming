#include "lists.h"

/**
 * check_cycle - function checks if a singly linked list has
 * a cycle in it
 * @list: intery point
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	struct listint_s *f, *s;

	if (!list || !list->next)
		return (0);

	f = list;
	s = list->next;

	while (f && f->next)
	{
		if (s == f)
			return (1);
		s = s->next;
		f = f->next->next;
	}
	return (0);
}
