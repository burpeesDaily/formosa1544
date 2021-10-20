# Copyright © 2021 by Shun Huang. All rights reserved.
# Licensed under MIT License.
# See LICENSE in the project root for license information.

import copy

# Create an object with an mutable object,
# and print out its memory address.
compound_object = {"key1": 123, "key2": [1, 2, 3]}
print(hex(id(compound_object)))
# 0x7fbba9d11480

# Use copy.deepcopy to create a copy of the compound_object.
# and print out its memory address.
compound_object_copy = copy.deepcopy(compound_object)
print(hex(id(compound_object_copy)))
# 0x7fbba9c3b600

# Also print out the address of the key2 value from both
# compound_object and compound_object_copy, and they are
# different objects.
print(hex(id(compound_object["key2"])))
# 0x7fbba9c4a180
print(hex(id(compound_object_copy["key2"])))
# 0x7fbba9c6d9c0

# Therefore, if we update the key2 value from compound_object_copy,
# it does not affect compound_object.
compound_object_copy["key2"].append(4)
print(compound_object_copy)
# {'key1': 123, 'key2': [1, 2, 3, 4]}
print(compound_object)
# {'key1': 123, 'key2': [1, 2, 3]}
