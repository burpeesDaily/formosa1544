# Copyright © 2019 by Shun Huang. All rights reserved.
# Licensed under MIT License.
# See LICENSE in the project root for license information.

"""A simple queue implementation.
"""

from typing import Any, NoReturn # For type hints

from my_package.my_data_structure import _common

class _QueueNode(_common.MyNode):
    """A private class derived from `_common.MyNode`. The class provide
    type checking when assing a next or previous node.
    """

    def __init__(self, data: Any):
        """Constructor for `_QueueNode`.

        Parameters
        ----------
        data: Any
            data to be hold in this data structure.
        """
        _common.MyNode.__init__(self, data=data)

    @property
    def previous(self):
        """Return the previous node

        Returns
        -------
        _QueueNode or None
            Return the previous node. `None` will be returned if there
            is no previous node.
        """
        return self.my_previous

    @previous.setter
    def previous(self, node) -> NoReturn:
        """Assing the previous node

        Parameters
        ----------
        node: _QueueNode or None
            The node to be assigned as the previous node.

        Raises
        ------
        ValueError
            If the input type is invalid.
        """
        if node is None:
            self.my_previous = None
        else:
            if type(node) == type(_QueueNode(0)):
                self.my_previous = node
            else:
                raise ValueError("Invalid type")

    @property
    def next(self):
        """Return the next node

        Returns
        -------
        _QueueNode or None
            Return the next node. `None` will be returned if there is
            no next node.
        """
        return self.my_next

    @next.setter
    def next(self, node):
        """Assing the next node

        Parameters
        ----------
        node: _QueueNode or None
            The node to be assigned as the next node.

        Raises
        ------
        ValueError
            If the input type is invalid.
        """
        if node is None:
            self.my_next = None
        else:
            if type(node) == type(_QueueNode(0)):
                self.my_next = node
            else:
                raise ValueError("Invalid type")

class Queue:
    """A simple queue data structure with basic operations.

    Attributes
    ----------
    size: int
        The size of the queue.

    Methods
    -------
    enqueue(data: int)
        Adds an item onto the end of the queue.
    dequeue() -> int
        Removes the item from the front of the queue. And return the
        value of the removed item.
    dump()
        Print all the data from the queue.

    Notes
    -----
    This queue implementation only support `int` type.

    Examples
    --------
    >>> from my_package.my_data_structure import my_queue
    >>> queue = my_queue.Queue()
    >>> queue.enqueue(10)
    >>> queue.enqueue(3)
    >>> queue.enqueue(14)
    >>> queue.dump()
    14 3 10
    >>> queue.size
    >>> 3
    >>> queue.dequeue()
    >>> 10
    >>> queue.dump()
    14 3
    >>> queue.size
    2
    """
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def enqueue(self, data: int) -> NoReturn:
        """Adds an item onto the end of the queue.

        Parameters
        ----------
        data: int
            The data to be inserted into the queue.

        Raises
        ------
        ValueError
            The queue only support `int` type. If the input type is not
            `int`, ValueError will be thrown.
        """
        if type(data) is not int:
            raise ValueError("Invalid type")

        new_node = _QueueNode(data=data)
        if self._head is None:
            self._head = new_node
            self._tail = self._head
        else:
            temp = self._head
            self._head = new_node
            new_node._next = temp
            temp._previous = new_node
        self._size += 1

    def dequeue(self) -> int:
        """Removes the item from the front of the queue. And return the
        value of the removed item.

        Returns
        -------
        int or None
            The value of the removed item. If the queue is empty,
            `None` will be returned.
        """
        if self._tail:
            temp = self._tail
            self._tail = temp._previous
            self._tail.next = None
            self._size -= 1
            return temp.data
        return None

    def dump(self) -> NoReturn:
        """Print all the data from the queue without removing any item.
        """
        index = self._head
        while index:
            print(index.data, end=" ")
            index = index.next

    @property
    def size(self) -> int:
        return self._size
