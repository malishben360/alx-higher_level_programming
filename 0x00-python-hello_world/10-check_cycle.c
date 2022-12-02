#include "lists.h"

/**
  * check_cycle - check for loop in single linked list
  * @list: Single single linked list of integers
  *
  * Return: 0 contains no loop, or 1 if there is a loop.
  */
int check_cycle(listint_t *list)
{
	listint_t *s, *f;

	if (list == NULL)
		exit(EXIT_FAILURE);

	s = list, f = list->next;
	while (f != NULL)
	{
		if (s != f)
		{
			s = s->next;
			if (f->next != NULL)
				f = f->next->next;
			else
				f = f->next;
		}
		else
		{
			return (1);
		}
	}
	return (0);
}
