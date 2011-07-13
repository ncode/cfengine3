#!/usr/bin/python

from setuptools import setup, find_packages

setup(name='cfengine3',
      version='0.0.3',
      description='A simple way to extend your cfengine3 using python',
      author='Juliano Martinez',
      author_email='juliano@martinez.io',
      url='https://github.com/ncode/cfengine3',
      packages=find_packages(exclude=["tests"]),
     )
