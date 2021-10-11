# Copyright © 2021 by Shun Huang. All rights reserved.
# Licensed under MIT License.
# See LICENSE in the project root for license information.

def my_function(parameter):

    if type(parameter) is str:
        print("Do something when the type is string")

    elif type(parameter) is int:
        print("Do something when the type is integer")

    else:
        raise TypeError("Invalid type")


if __name__ == "__main__":

    # Valid
    my_function(10)
    my_function("hello")

    # TypeError exception will be thrown
    my_function(2.3)
