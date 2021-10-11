# Copyright © 2021 by Shun Huang. All rights reserved.
# Licensed under MIT License.
# See LICENSE in the project root for license information.


import abc

from typing import Optional
from dataclasses import dataclass


@dataclass
class Node:
    """Basic binary tree node definition."""

    key: int
    left: Optional["Node"] = None
    right: Optional["Node"] = None
    parent: Optional["Node"] = None


class BasicBinaryTree(abc.ABC):
    """An abstract base class defines the interface for any type of binary trees.

    The derived class should implement the abstract method defined in the abstract
    base class.
    """

    @abc.abstractmethod
    def insert(self, key: int) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def delete(self, key: int) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def search(self, key: int) -> Node:
        raise NotImplementedError()


class BinarySearchTree(BasicBinaryTree):
    """Binary Search Tree."""

    def insert(self, key: int) -> None:
        # The BST implementation
        pass

    def delete(self, key: int) -> None:
        # The BST implementation
        pass

    def search(self, key: int) -> Node:
        # The BST implementation
        pass


@dataclass
class AVLNode(Node):
    """AVL Tree node definition. Derived from Node."""

    left: Optional["AVLNode"] = None
    right: Optional["AVLNode"] = None
    parent: Optional["AVLNode"] = None
    height: int = 0


class AVLTree(BasicBinaryTree):
    """AVL Tree implementation."""

    def insert(self, key: int) -> None:
        # The AVL Tree implementation
        pass

    def delete(self, key: int) -> None:
        # The AVL Tree implementation
        pass

    def search(self, key: int) -> AVLNode:
        # The AVL Tree implementation
        pass
