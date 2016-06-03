#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pip.req import parse_requirements
from setuptools import find_packages, setup

import pyci


reqs = [str(r.req) for r in parse_requirements('requirements.txt')]


setup(
    name='pyci',
    version=pyci.__version__,
    description='Minimalistic CI server',
    author='Koen Dercksen',
    author_email='mail@koendercksen.com',
    url='http://github.com/KDercksen/pyci',
    packages=find_packages(exclude=['tests']),
    install_requires=reqs,
    test_suite='tests',
)
