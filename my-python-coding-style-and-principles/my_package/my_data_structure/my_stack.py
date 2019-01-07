# Copyright © 2019 by Shun Huang. All rights reserved.
# Licensed under MIT License.
# See LICENSE in the project root for license information.

"""A simple stack implementation.
"""

from typing import Any, NoReturn # For type hints

from my_package.my_data_structure import _common

class Stack:
    """A simple stack data structure with basic operations.

    Attributes
    ----------
    size: int
        The size of the stack.

    Methods
    -------
    push(data: Any)
        Adds an item onto the stack.
    pop() -> Any
        Removes the top item from the stack. And return the value of
        the removed item.
    dump()
        Print all the data from the stack.

    Examples
    --------
    >>> from my_package.my_data_structure import my_stack
    >>> stack = my_stack.Stack()
    >>> stack.push(10)
    >>> stack.push(3)
    >>> stack.push(14)
    >>> stack.dump()
    14 3 10
    >>> stack.size
    >>> 3
    >>> stack.pop()
    >>> 14
    >>> stack.dump()
    3 10
    >>> stack.size
    2
    """
    def __init__(self):
        self.top = None
        self._size = 0

    def push(self, data: Any) -> NoReturn:
        """Adds an item onto the stack.

        Parameters
        ----------
        data: Any
            The data to be pushed onto the stack.
        """
        new_node = _common.MyNode(data=data)
        if self.top is None:
            self.top = new_node
        else:
            new_node.my_next = self.top
            self.top = new_node
        self._size += 1

    def pop(self) -> Any:
        """Removes the top item from the stack. And return the value of
        the removed item.

        Returns
        -------
        Any or None
            Return the value of the removed item. If the stack is
            empty, `None` will be returned.
        """
        if self.top:
            temp = self.top
            self.top = temp.my_next
            self._size -= 1
            return temp.data
        return None

    def dump(self) -> NoReturn:
        """Print all the data from the stack without removing any item.
        """
        index = self.top
        while index:
            print(index.data, end=" ")
            index = index.my_next

    @property
    def size(self):
        return self._size