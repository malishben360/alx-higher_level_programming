#include "lists.h"

/**
  * insert_node - insert new node in an ordered manner
  * @head: pionter to the first node of the linked list
  * @number: Integer for the new node
  *
  * Return: Alway point to the new node, or NULL if failed.
  */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *prev = NULL;
	listint_t *curr = NULL;
	listint_t *node = NULL;

	node = malloc(sizeof(listint_t));
	if (!node)
		return (NULL);

	node->n = number;
	node->next = NULL;
	if (*head == NULL)
	{
		*head = node;
		return (node);
	}

	prev = NULL;
	curr = *head;
	while (curr != NULL)
	{
		if (curr->n > number)
		{
			if (prev != NULL)
				prev->next = node;
			else
				*head = node;
			node->next = curr;
			return (node);
		}
		else if (curr->next == NULL)
		{
			curr->next = node;
			return (node);
		}
		prev = curr;
		curr = curr->next;
	}
	return (node);
}
