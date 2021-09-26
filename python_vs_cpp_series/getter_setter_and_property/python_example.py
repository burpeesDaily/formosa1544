# Copyright © 2021 by Shun Huang. All rights reserved.
# Licensed under MIT License.
# See LICENSE in the project root for license information.

class MyClass:

    def __init__(self) -> None:
        # this variable starts with an underscore (_),
        # it indicates it is supposed to be used internally only
        self._my_data: int = 0

        # Name mangling
        self.__my_member = 0

    def get_my_data(self) -> int:
        return self._my_data

    def set_my_data(self, value: int) -> None:
        self._my_data = value

    # A method starts with an underscore (_), also means private.
    def _private_method(self) -> None:
        pass


if __name__ == "__main__":
    my_class = MyClass()

    # Valid, but not recommended
    my_class._my_data = 10

    # Valid, but not recommended
    my_class._MyClass__my_member = 10
