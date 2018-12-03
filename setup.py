from setuptools import setup
from distutils.extension import Extension
import numpy as np
try:
    from Cython.Build import cythonize
    USE_CYTHON = True
except ImportError:
    USE_CYTHON = False

print('using cython', USE_CYTHON)

ext = '.pyx' if USE_CYTHON else '.c'


extensions = [
    Extension(
        'circlehough.hough_transformation',
        sources=['circlehough/hough_transformation'+ext],
    ),
]

if USE_CYTHON:
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
