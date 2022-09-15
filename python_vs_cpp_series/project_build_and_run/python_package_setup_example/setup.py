"""Setup file for mypackage."""

import pathlib
import setuptools

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# This call to setup() does all the work
setuptools.setup(
    name="my-package",
    version="0.0.1",
    description="A Python package example",
    packages=setuptools.find_packages(),
    python_requires=">=3.7",
)
