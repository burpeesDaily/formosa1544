# Copyright © 2021 by Shun Huang. All rights reserved.
# Licensed under MIT License.
# See LICENSE in the project root for license information.


# Nonlocal only enable the access to the next closest scope
x = "hello world"


def outer_nonlocal():

    x = 0

    def inner():

        x = 1

        def innermost():
            nonlocal x
            x = 2
            print(f"innermost: {x}")

        innermost()
        print(f"inner: {x}")

    inner()
    print(f"outer_nonlocal: {x}")


outer_nonlocal()
print(f"global: {x}")
# The output of x:
# innermost: 2
# inner: 2
# outer_nonlocal: 0
# global: hello world


# Global only enable the access to the global level
y = "hello world"


def outer_global():

    y = 0

    def inner():

        y = 1

        def innermost():
            global y
            y = 2
            print(f"innermost: {y}")

        innermost()
        print(f"inner: {y}")

    inner()
    print(f"outer_global: {y}")


outer_global()
print(f"global: {y}")
# The output of y:
# innermost: 2
# inner: 1
# outer_global: 0
# global: 2
