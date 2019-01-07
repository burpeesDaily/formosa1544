# Copyright © 2018 by Shun Huang. All rights reserved.
# Licensed under MIT License.
# See LICENSE in the project root for license information.

"""A binary tree example to demonstrate different tree traversal,
including in-order, pre-order, post-order, and level-order.
"""

import enum # Enum to define traversal types.

from typing import NoReturn # For type hints

class TraversalType(enum.Enum):
    IN_ORDER = enum.auto()
    PRE_ORDER = enum.auto()
    POST_ORDER = enum.auto()
    LEVEL_ORDER = enum.auto()

class _Node:
    """Basic data structure to build a binary tree. This is a private
    class should be used within this module.
    
    Attributes
    ----------
    left: _Node or None
        A pointer points to the left child. If there is no child on the
        left, the value is `None`.
    right: _Node or None
        A pointer points to the right child. If there is no child on
        the right, the value is `None`.
    data: int
        Data of the node.
    """
    def __init__(self, data: int):
        self.left = None
        self.right = None
        self.data = data

class BinaryTree:
    """A binary tree with different types of tree traversal.

    Methods
    -------
    insert(data: int)
        Inset an item into a binary tree.
    traverse(traversal_type: TraversalType)
        Traverse the tree based on different tree traversals.

    Examples
    --------
    >>> from my_package.my_data_structure import my_tree
    >>> tree = my_tree.BinaryTree(data=30)
    >>> tree.insert(10)
    >>> tree.insert(20)
    >>> tree.insert(40)
    >>> tree.insert(50)
    >>> tree.traverse(traversal_type=my_tree.TraversalType.IN_ORDER)
    10 20 30 40 50
    >>> tree.traverse(traversal_type=my_tree.TraversalType.PRE_ORDER)
    30 10 20 40 50
    >>> tree.traverse(traversal_type=my_tree.TraversalType.POST_ORDER)
    20 10 50 40 30
    >>> tree.traverse(traversal_type=my_tree.TraversalType.LEVEL_ORDER)
    30 10 40 20 50
    """
    def __init__(self, data: int):
        self._root = _Node(data=data)

    def _insert(self, data: int, node: _Node) -> NoReturn:
        """The real implementation of tree insertion.

        Parameters
        ----------
        data: int
            The data to be inserted into the tree.
        node: _Node
            The parent node of the input data.

        Raises
        ------
        ValueError
            If the input data has existed in the tree, `ValueError`
            will be thrown.
        """
        if data == node.data:
            raise ValueError("Duplicate value")
        elif data < node.data:
            if node.left != None:
                self._insert(data=data, node=node.left)
            else:
                node.left = _Node(data=data)
        elif data > node.data:
            if node.right != None:
                self._insert(data=data, node=node.right)
            else:
                node.right = _Node(data=data)

    def _inorder_traverse(self, node: _Node):
        """In-order traversal.

        Parameters
        ----------
        node: _Node
            The parent node of the inseration node.

        Notes
        -----
        In-order means Left subtree, current node, right subtree (LDR)
        """
        if node:
            self._inorder_traverse(node.left)
            print(node.data, end=" ")
            self._inorder_traverse(node.right)

    def _preorder_traverse(self, node: _Node):
        """Pre-order traversal.

        Parameters
        ----------
        node: _Node
            The parent node of the inseration node.

        Notes
        -----
        Pre-order means Current node, left subtree, right subtree (DLR)
        """
        if node:
            print(node.data, end=" ")
            self._preorder_traverse(node.left)
            self._preorder_traverse(node.right)


    def _postorder_traverse(self, node: _Node):
        """Post-order traversal.

        Parameters
        ----------
        node: _Node
            The parent node of the inseration node.

        Notes
        -----
        Post-order means Left subtree, right subtree, current node
        (LRD)
        """
        if node:
            self._postorder_traverse(node.left)
            self._postorder_traverse(node.right)
            print(node.data, end=" ")

    def _levelorder_traverse(self):
        """Level-order traversal.

        Parameters
        ----------
        node: _Node
            The parent node of the inseration node.

        Notes
        -----
        In-order means Level by level, from left to right, starting
        from the root node.
        """
        queue = [self._root]

        while len(queue) > 0:

            temp = queue.pop(0)
            print(temp.data, end=" ")

            if temp.left:
                queue.append(temp.left)

            if temp.right:
                queue.append(temp.right)

    def insert(self, data: int) -> NoReturn:
        """Insert an item into a binary tree.

        Parameters
        ----------
        data: int
            The data to be inserted into the tree.

        Raises
        ------
        ValueError
            If the input data has existed in the tree, `ValueError`
            will be thrown.
        """
        self._insert(data=data, node=self._root)

    def traverse(self, traversal_type: TraversalType) -> NoReturn:
        """Traverse the tree based on traversal types.

        Parameters
        ----------
        traversal_type: TraversalType
            The type of traversals.
        
        See Also
        --------
        TraversalType : The definition of traversal type
        """
        if traversal_type == TraversalType.IN_ORDER:
            self._inorder_traverse(self._root)
        elif traversal_type == TraversalType.PRE_ORDER:
            self._preorder_traverse(self._root)
        elif traversal_type == TraversalType.POST_ORDER:
            self._postorder_traverse(self._root)
        elif traversal_type == TraversalType.LEVEL_ORDER:
            self._levelorder_traverse()
        else:
            raise ValueError(f"{traversal_type} is invalid")
