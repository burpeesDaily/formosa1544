# Copyright © 2021 by Shun Huang. All rights reserved.
# Licensed under MIT License.
# See LICENSE in the project root for license information.

from typing import List


class MyClass:

    def __init__(self) -> None:
        self.my_value: int = 0
        self.my_list: List = []


class1 = MyClass()
class2 = class1

class1.my_value = 10

print(class1 is class2)
