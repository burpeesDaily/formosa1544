# Copyright © 2021 by Shun Huang. All rights reserved.
# Licensed under MIT License.
# See LICENSE in the project root for license information.
from typing import List, Optional


# Use an empty list as the default value.
def my_function_1(parameter: List = []) -> None:
    parameter.append(10)
    print(parameter)


# Use None as the default value. And use Optional for type checking
def my_function_2(parameter: Optional[List] = None) -> None:
    if parameter:
        parameter.append(10)
    else:
        parameter = [10]
    print(parameter)


if __name__ == "__main__":
    my_function_1()
    # [10]
    my_function_1()
    # [10, 10]
    my_function_1()
    # [10, 10, 10]

    my_function_2()
    # [10]
    my_function_2()
    # [10]
