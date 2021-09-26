# Copyright © 2021 by Shun Huang. All rights reserved.
# Licensed under MIT License.
# See LICENSE in the project root for license information.

import re

from typing import Optional


class Contact:
    def __init__(self, first_name: str, last_name: str) -> None:
        self._first_name = first_name
        self._last_name = last_name
        self._email: Optional[str] = None

    @property
    def name(self) -> str:
        # The @property decorator turns the name() method into a getter
        # for a read-only attribute with the same name, so a client can
        # access it by doing c.name if c is an instance of Contact.
        return f"{self._first_name} {self._last_name}"

    @property
    def email(self) -> str:
        # The @property docorator turns the email() method into a getter.
        if self._email:
            return self._email
        else:
            return "No associated email"

    @email.setter
    def email(self, email_address) -> None:
        # A property object has also a setter method usable as decorator that
        # create a copy of the property with the corresponding accessor
        # function set to the decorated function. Therefore, the setter
        # decorator for email is @email.setter. And a client can access it
        # by doing c.email = email@email.com if c is an instance of Contact.
        if re.fullmatch(r"^\S+@\S+$", email_address):
            self._email = email_address
        else:
            raise ValueError(f"{email_address} is invalid.")


if __name__ == "__main__":

    contact = Contact(first_name="John", last_name="Wick")
    contact.email = "john.wick@email.com"
    print(f"Name: {contact.name}")
    print(f"Email: {contact.email}")
