# Copyright © 2021 by Shun Huang. All rights reserved.
# Licensed under MIT License.
# See LICENSE in the project root for license information.

import copy


# Define a mutable object.
value = [1, 2, 3]
print(hex(id(value)))
# 0x7fc0df486380

# Copy assignment just creates binding.
value_bind = value
print(hex(id(value_bind)))
# 0x7fc0df486380

# Use copy.copy function to perform shallow copy.
value_copy = copy.copy(value)
print(hex(id(value_copy)))
# 0x7fc0df4af740

# Update the copied variable.
value_copy.append(4)
print(value_copy)
# [1, 2, 3, 4]

# The update does not affect the original variable.
print(value)
# [1, 2, 3]
