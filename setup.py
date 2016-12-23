#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2011-2013 Spotify AB

from setuptools import setup

setup(name='sparkey-python',
      version='0.1.0',
      author=u'Kristofer Karlsson',
      author_email='krka@spotify.com',
      description='Python bindings for Sparkey',
      license='Apache Software License 2.0',
     classifiers=[
          'Topic :: Database',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: Apache Software License',
      ],
      packages=['sparkey'],
      package_data={'sparkey': ['sparkey.cdef']},
      install_requires=["cffi>=1.0.0"],
      setup_requires=["cffi>=1.0.0"],
      cffi_modules=["sparkey/sparkey_build.py:ffi"]
 )
