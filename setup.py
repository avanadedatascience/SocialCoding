#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


setup(name='operations',
      version='0.1.0',
      description='An operations Python package',
      long_description='',

      author='dian kang@avanade',

      # Give one email only, the maintainer's email
      author_email='dian.kang@avanade.com',

      license='file LICENSE.txt',

      packages=find_packages(exclude=['docs', 'tests*']),


      install_requires=[
          'scikit-learn>=0.19.1',
          'numpy',
          'scipy',
          'pandas',
		  'xgboost',
		  'lightgbm'
      ],
   
      zip_safe=False
)