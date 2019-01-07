from my_package.my_data_structure import my_stack


if __name__ == "__main__":

    stack = my_stack.Stack()

    stack.push(10)
    stack.push(3)
    stack.push(14)

    print(f"size of the stack: {stack.size}")

    stack.dump()

    print()
    temp = stack.pop()
    print(temp)

    stack.dump()
    print(f"size of the stack: {stack.size}")
