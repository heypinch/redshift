#!/usr/bin/env python

from distutils.core import setup
from distutils.extension import Extension
import os
import os.path
import numpy

import Cython.Distutils

pwd = os.path.dirname(__file__)
virtual_env = os.environ.get('VIRTUAL_ENV', '')

ext = Extension(
    "hashes",                 # name of extension
    ["hashes.pyx", "MurmurHash3.cpp"],           # filename of our Pyrex/Cython source
    language="c++",              # this causes Pyrex/Cython to create C++ source
    include_dirs=[numpy.get_include(), os.path.join(virtual_env, 'include')]
    )

setup(
  name = 'Hash table wrappers',
  cmdclass = {'build_ext': Cython.Distutils.build_ext},
  ext_modules = [ext]
)
