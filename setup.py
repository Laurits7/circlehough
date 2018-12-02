from setuptools import setup
from distutils.extension import Extension
import os
import numpy as np
import sys

version = sys.argv[1]
if version=='dev':
    ext = '.pyx'
    from Cython.Build import cythonize
elif version=='user' or version==None:
    ext = '.c'
else:
    assert version not in ['dev', None, 'user'], 'Please choose a correct version'


extensions = [
    Extension(
        'circlehough.hough_transformation',
        sources=[os.path.join('circlehough','hough_transformation' + ext)],
        language="c",
    ),
]

if version == 'dev':
    extensions = cythonize(extensions)

setup(
    name="circlehough",
    version='0.0.1',
    description='Perform Hough transformation for circle',
    url='https://github.com/Laurits7/circlehough',
    author='Laurits Tani',
    author_email='laurits.tani@gmail.com',
    licence='MIT',
    packages=['circlehough'],
    install_requires=[
        'Cython',
        'numpy',
    ],
    ext_modules=extensions,
    include_dirs=[np.get_include()],
)
