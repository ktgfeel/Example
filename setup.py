# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 21:07:10 2023

@author: user
"""

from setuptools import setup, find_packages

setup(
      name='helper',
      version='0.0.1',
      description = "Hi"
      url = "https://github.com/ktgfeel/Example.git"
      author='KTG',
      author_email = 'Test@gmail.com',
      license = 'KSOE',
      packages = find_packages(),
      install_requires=['pandas']
      )