#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import find_packages, setup

import pyci


setup(
    name='pyci',
    version=pyci.__version__,
    description='Minimalistic CI server',
    author='Koen Dercksen',
    author_email='mail@koendercksen.com',
    url='http://github.com/KDercksen/pyci',
    packages=find_packages(exclude=['tests']),
    test_suite='tests',
)
