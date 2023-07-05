#!/usr/bin/python3
# 100-singly_linked_list
# AbdulTechX
"""Define a data class"""


class Node:
    """Represent Node in singlylinkedlist"""
    def __init__(self, data, next_node=None):
        """Initialize a new Node.

        Args:
            data (int): The data of the new Node.
            next_node (Node): The next node of the new Node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get/Set the data of the Node"""
        return(self.__data)

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Get/set the next_node of the Node"""
        return(self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if (value is not None and not isinstance(value, Node)):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Represent a new Singlylinkedlist"""

    def __init__(self):
        """Ïnitialize a new SinglyLinkedList"""

        self.head = None

    def sorted_insert(self, value):
        """Insert a new Node to the SinglyLinkedList.

        The node is inserted into the list at the correct
        ordered numerical position.

        Args:
            value (Node): The new Node to insert.
        """
        new = Node(value)
        if self.head is None:
            new_next_node = None
            self.head = new
        elif self.head.data > value:
            new_next_node = self.head
            self.head = new
        else:
            tmp = self.head
            while (tmp.next_node is not None and
                    tmp.next_node.data < value):
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new

    def __str__(self):
        """Define the print() representation of a SinglyLinkedList."""
        values = []
        tmp = self.head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return ('\n'.join(values))
