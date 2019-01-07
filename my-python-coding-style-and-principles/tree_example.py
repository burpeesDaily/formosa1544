from my_package.my_data_structure import my_tree


if __name__ == "__main__":

    tree = my_tree.BinaryTree(data=30)
    tree.insert(10)
    tree.insert(20)
    tree.insert(40)
    tree.insert(50)


    print("In-Order")
    tree.traverse(traversal_type=my_tree.TraversalType.IN_ORDER)

    print("\nPre-Order")
    tree.traverse(traversal_type=my_tree.TraversalType.PRE_ORDER)

    print("\nPost-Order")
    tree.traverse(traversal_type=my_tree.TraversalType.POST_ORDER)

    print("\nLevel-Order")
    tree.traverse(traversal_type=my_tree.TraversalType.LEVEL_ORDER)

