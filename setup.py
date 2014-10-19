#!/usr/bin/env python
from setuptools import setup, find_packages

setup(name='mysiteLL',
      version='0.1',
      packages=find_packages(),
      package_data={'mysiteLL': ['bin/*.*', 'static/*.*', 'templates/*.*']},
      exclude_package_data={'mysiteLL': ['bin/*.pyc']},
      scripts=['mysiteLL/bin/manage.py'])
