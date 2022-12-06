#include <stdlib.h>
#include "lists.h"

/**
  * is_palindrome - check if a linked list is palindrome
  * @head: first node of the list
  *
  * Return: 1 if is palindrone, else 0.
  */
int is_palindrome(listint_t **head)
{
	listint_t *ptr = NULL;
	listint_t *tmp1 = NULL;
	listint_t *tmp2 = NULL;

	if (head == NULL)
		exit(EXIT_FAILURE);

	tmp1 = *head;
	while (tmp1 != NULL)
	{
		ptr = add_nodeint(&ptr, tmp1->n);
		if (ptr == NULL)
			exit(EXIT_FAILURE);
		tmp1 = tmp1->next;
	}

	tmp1 = *head;
	tmp2 = ptr;
	while (tmp2 != NULL)
	{
		if (tmp1->n != tmp2->n)
		{
			free_listint(ptr);
			tmp1 = NULL;
			tmp2 = NULL;
			return (0);
		}
		tmp1 = tmp1->next;
		tmp2 = tmp2->next;
	}
	free_listint(ptr);
	tmp1 = NULL;
	tmp2 = NULL;
	return (1);
}

/**
  * add_nodeint - add a new node to the head of a list
  * @head: first node of the list
  * @n: data of the new node
  *
  * Return: Address of the new node.
  */
listint_t *add_nodeint(listint_t **head, const int n)
{
	listint_t *node = NULL;

	if (head == NULL)
		return (NULL);

	node = malloc(sizeof(listint_t));
	if (!node)
		return (NULL);
	node->n = n;
	node->next = *head;
	*head = node;
	return (node);
}
