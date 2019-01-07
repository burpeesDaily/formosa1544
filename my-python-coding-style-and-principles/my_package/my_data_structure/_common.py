# Copyright © 2019 by Shun Huang. All rights reserved.
# Licensed under MIT License.
# See LICENSE in the project root for license information.

"""A private module provides common functionalities which can be used
by other modules. This module and should be used inside
`my_data_structure` only.

"""

from typing import Any

class MyNode:
    """The basic data structure can be used to build stack and queue.

    Attributes
    ----------
    my_next: MyNode or derived type
        A pointer points to the next node. `None` is there is no next
        node.
    my_previous: MyNode or derived type
        A pointer points to the previous node. `None` is there is no
        previous node.

    Notes
    -----
    When use `MyNode` to build linked list or other data structure,
    all the nodes must be the same node type, i.e., `MyNode` or other
    node type derived from `MyNode`
    """

    def __init__(self, data: Any):
        """Initializer of `MyNode`.

        Parameters
        ----------
        data: Any
            The data to be sotred in the node.
        """
        self.data = data
        self.my_next = None
        self.my_previous = None

