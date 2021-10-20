# Copyright © 2021 by Shun Huang. All rights reserved.
# Licensed under MIT License.
# See LICENSE in the project root for license information.

import copy


# Copy an immutable object
my_string = "hello"
my_string_copy = my_string
# They both bind to the same object.
print(my_string is my_string_copy)
# True

# After we update one variable, they bind to two different objects.
my_string_copy += " world"
print(my_string is my_string_copy)
# False

# Of course, their values are different.
print(f"my_string: {my_string}")
# my_string: hello
print(f"my_string_copy: {my_string_copy}")
# my_string_copy: hello world
