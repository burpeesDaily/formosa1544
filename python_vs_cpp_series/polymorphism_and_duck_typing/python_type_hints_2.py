# Copyright © 2021 by Shun Huang. All rights reserved.
# Licensed under MIT License.
# See LICENSE in the project root for license information.


def my_function(parameter1: int, parameter2: str) -> None:
    print(f"Parameter 1: {parameter1}")
    print(f"Parameter 2: {parameter2}")


if __name__ == "__main__":
    my_function(parameter1="Hello", parameter2=3.5)
