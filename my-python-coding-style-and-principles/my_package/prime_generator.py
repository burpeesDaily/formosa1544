# Copyright © 2019 by Shun Huang. All rights reserved.
# Licensed under MIT License.
# See LICENSE in the project root for license information.

"""A simple prime number generator.

Routines
--------
get_prime(base: int)
    Return a generator for producing a prime number.
is_prime(number: int) -> bool
    Check if a number is a prime number or not.
"""

import math # Standard math library for calculating prime number

def get_prime(base: int):
    """Return a generator for producing a prime number.

    Parameters
    ----------
    base: int
        The starting number for generating a prime number.

    Yields
    ------
    int
        Yields the next prime number it finds.

    Examples
    --------
    >>> from my_package import prime_generator
    >>> prime = prime_generator.get_prime(base=10)
    >>> next(prime)
    11
    >>> next(prime)
    13
    """
    number = base
    while True:
        if is_prime(number):
            yield number
        number += 1

def is_prime(number: int) -> bool:
    """Check if a number is a prime number.

    Parameters
    ----------
    number: int
        The number to check if it is a prime number.

    Returns
    -------
    bool
        True if the number is a prime number; False, otherwise.

    Examples
    --------
    >>> from my_package import prime_generator
    >>> prime_generator.is_prime(11)
    True
    >>> prime_generator.is_prime(12)
    False
    """
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True
