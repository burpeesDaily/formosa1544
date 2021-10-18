# Copyright © 2021 by Shun Huang. All rights reserved.
# Licensed under MIT License.
# See LICENSE in the project root for license information.


from typing import List


class MyClass:
    # Mutable class variable. Shared by all instances
    mutable_member: List = []

    # Immutable class variable.
    # Shared by all instances unless an instance binds this variable to something else.
    immutable_member: int = 0

    def __init__(self) -> None:
        # Instance variables are unique to each instance.
        self.immutable_instance_variable: int = 0
        self.mutable_instance_variable: List = []


if __name__ == "__main__":

    print(f"MyClass.mutable_member: {MyClass.mutable_member}")
    # MyClass.mutable_member: []
    print(f"MyClass.mutable_member address: {hex(id(MyClass.mutable_member))}")
    # MyClass.mutable_member address: 0x7f0f7092fe40
    print(f"MyClass.immutable_member address: {hex(id(MyClass.immutable_member))}")
    # MyClass.immutable_member address: 0x7f0f70b34910

    class1 = MyClass()
    print(f"class1.mutable_member: {class1.mutable_member}")
    # class1.mutable_member: []
    print(f"class1.mutable_member address: {hex(id(class1.mutable_member))}")
    # class1.mutable_member address: 0x7f0f7092fe40
    print(f"class1.immutable_member address: {hex(id(class1.immutable_member))}")
    # class1.immutable_member address: 0x7f0f70b34910

    class2 = MyClass()
    print(f"class2.mutable_member: {class2.mutable_member}")
    # class2.mutable_member: []
    print(f"class2.mutable_member address: {hex(id(class2.mutable_member))}")
    # class2.mutable_member address: 0x7f0f7092fe40
    print(f"class2.immutable_member address: {hex(id(class2.immutable_member))}")
    # class2.immutable_member address: 0x7f0f70b34910

    # Update the mutable class variable
    class1.mutable_member.append(10)
    print(f"class1.mutable_member: {class1.mutable_member}")
    # class1.mutable_member: [10]
    print(f"class2.mutable_member: {class2.mutable_member}")
    # class2.mutable_member: [10]

    # Update the immutable class variable
    class1.immutable_member = 20
    print(f"class1.immutable_member: {class1.immutable_member}")
    # class1.immutable_member: 20
    print(f"class1.immutable_member address: {hex(id(class1.immutable_member))}")
    # class1.immutable_member address: 0x7f0f70b34b90
    print(f"class2.immutable_member: {class2.immutable_member}")
    # class2.immutable_member: 0
    print(f"class2.immutable_member address: {hex(id(class2.immutable_member))}")
    # class2.immutable_member address: 0x7f0f70b34910

    class3 = MyClass()
    print(f"class3.immutable_member: {class3.immutable_member}")
    # class3.immutable_member: 0
    print(f"class3.immutable_member address: {hex(id(class3.immutable_member))}")
    # class3.immutable_member address: 0x7f0f70b34910
    print(f"MyClass.immutable_member address: {hex(id(MyClass.immutable_member))}")
    # MyClass.immutable_member address: 0x7f0f70b34910

    # Instance variables are unique to each instance
    class1.mutable_instance_variable.append(30)
    print(f"class1.mutable_instance_variable: {class1.mutable_instance_variable}")
    # class1.mutable_instance_variable: [30]
    print(
        f"class1.mutable_instance_variable address: "
        f"{hex(id(class1.mutable_instance_variable))}"
    )
    # class1.mutable_instance_variable address: 0x7f0f709e6140
    print(f"class2.mutable_instance_variable: {class2.mutable_instance_variable}")
    # class2.mutable_instance_variable: []
    print(
        f"class2.mutable_instance_variable address: "
        f"{hex(id(class2.mutable_instance_variable))}"
    )
    # class2.mutable_instance_variable address: 0x7f0f709e6180
