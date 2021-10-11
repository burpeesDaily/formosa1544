# Copyright © 2021 by Shun Huang. All rights reserved.
# Licensed under MIT License.
# See LICENSE in the project root for license information.

from typing import Dict, Optional, Union


class MyClass:

    def my_method_1(self, parameter1: int, parameter2: str) -> None:
        pass

    def my_method_2(self, parameter: Union[int, str]) -> Dict:
        pass


def my_function(parameter: Optional[MyClass]):
    pass
