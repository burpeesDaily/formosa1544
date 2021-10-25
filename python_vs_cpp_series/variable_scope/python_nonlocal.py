# Copyright © 2021 by Shun Huang. All rights reserved.
# Licensed under MIT License.
# See LICENSE in the project root for license information.


# Nested function without using nonlocal
def outer_function1():
    variable = 1

    def inner_function1():
        variable = 2
        print(f"inner_function: {variable}")

    inner_function1()
    print(f"outer_function: {variable}")


outer_function1()
# The output of the variable:
# inner_function: 2
# outer_function: 1


# Nested function with nonlocal
def outer_function2():
    variable = 1

    def inner_function2():
        nonlocal variable
        variable = 2
        print(f"inner_function: {variable}")

    inner_function2()
    print(f"outer_function: {variable}")


outer_function2()
# The output of the variable:
# inner_function: 2
# outer_function: 2
