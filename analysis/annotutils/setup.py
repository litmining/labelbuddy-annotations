#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name="annotutils",
    packages=find_packages("src"),
    package_data={"annotutils": ["data/*"]},
    install_requires=[
        "pandas",
        "matplotlib",
        "seaborn",
    ],
    python_requires=">=3.6"
)