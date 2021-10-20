# Copyright © 2021 by Shun Huang. All rights reserved.
# Licensed under MIT License.
# See LICENSE in the project root for license information.

import copy

# Create an object with an mutable object,
# and print out its memory address.
compound_object = {"key1": 123, "key2": [1, 2, 3]}
print(hex(id(compound_object)))
# 0x7fbd2b61d480

# Use copy.copy to create a copy of the compound_object.
# and print out its memory address.
compound_object_copy = copy.copy(compound_object)
print(hex(id(compound_object_copy)))
# 0x7fbd2b61d540

# The address shows compound_object_copy is a different object
# from compound_object.
# However, if we print out the address of the key2 value
# from both compound_object and compound_object_copy,
# we will see they are the same object.
print(hex(id(compound_object["key2"])))
# 0x7fbd2b5561c0
print(hex(id(compound_object_copy["key2"])))
# 0x7fbd2b5561c0

# Since key2 is shared, if we update it, the change will
# affect both compound_object and compound_object_copy.
compound_object_copy["key2"].append(4)
print(compound_object_copy)
# {'key1': 123, 'key2': [1, 2, 3, 4]}
print(compound_object)
# {'key1': 123, 'key2': [1, 2, 3, 4]}
