#include "lists.h"

/**
 * int check_cycle - function in C that checks if a
 * singly linked list has a cycle in it.
 * @listint_t: linklist to check if it has cycle
 * @list: pointer to the listint_t
 * Return: 0 if there is no cylce, 1 if there is a cyle.
 */
int check_cycle(listint_t *list)
{
	listint_t *snail, *chetar;

	if (list == NULL || list->next == NULL)
		return (0);
	snail = list->next;
	chetar = list->next->next;

	while (snail && chetar && chetar->next)
	{
		if (snail == chetar)
			return (1);
		snail = snail->next;
		chetar = chetar->next->next;
	}

	return (0);
}
