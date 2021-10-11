# Copyright © 2021 by Shun Huang. All rights reserved.
# Licensed under MIT License.
# See LICENSE in the project root for license information.


def my_function(parameter1, parameter2=None, parameter3="hello"):
    print(parameter1)
    if parameter2:
        print(parameter2)
    print(parameter3)


if __name__ == "__main__":
    # Use default parameter2 and parameter3; parameter 1 does not
    # have default value, so it cannot be omitted.
    my_function(10)

    # Use default parameter2
    my_function(parameter1=1, parameter3=5)

    # Use default parameter3; also notice that the order does not matter
    # when using keyword arguments.
    my_function(parameter2="world", parameter1=1)
