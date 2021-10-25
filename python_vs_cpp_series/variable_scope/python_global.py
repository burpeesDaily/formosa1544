# Copyright © 2021 by Shun Huang. All rights reserved.
# Licensed under MIT License.
# See LICENSE in the project root for license information.


global_variable = [1, 2, 3]  # global variable


def function1():
    print(global_variable)
    # [1, 2, 3]


def function2():
    global_variable = [2, 3, 4]  # local variable
    print(global_variable)
    # [2, 3, 4]
    print(hex(id(global_variable)))
    # 0x7f32763a4780


def function3():
    global global_variable
    global_variable = [3, 4, 5]
    print(global_variable)
    # [3, 4, 5]
    print(hex(id(global_variable)))
    # 0x7f32763a4780


def function4():
    global new_global_variable
    new_global_variable = "A new global variable"
    print(new_global_variable)
    # A new global variable
    print(hex(id(new_global_variable)))
    # 0x7f32763a25d0


if __name__ == "__main__":
    function1()
    function2()
    print(global_variable)
    # [1, 2, 3]
    print(hex(id(global_variable)))
    # 0x7f32763f7880
    function3()
    print(global_variable)
    # [3, 4, 5]
    print(hex(id(global_variable)))
    # 0x7f32763a4780
    function4()
    print(new_global_variable)
    # A new global variable
    print(hex(id(new_global_variable)))
    # 0x7f32763a25d0
