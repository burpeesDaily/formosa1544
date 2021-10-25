# Copyright © 2021 by Shun Huang. All rights reserved.
# Licensed under MIT License.
# See LICENSE in the project root for license information.


# if-statement does not define a scope
condition = True
if condition:
    result = 1
else:
    result = 2

print(result)
# 1


# for-loop does not define a scope
for i in range(10):
    x = 1 + i

print(x)
# 10


# with-statement does not define a scope
with open("example.txt") as file:
    data = file.read()

print(data)
# Hello World


# try-except does not define a scope
try:
    raise ValueError("Test exception")

except ValueError:
    message = "Catch an exception"

print(message)
# Catch an exception
