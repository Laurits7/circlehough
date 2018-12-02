from setuptools import setup
from distutils.extension import Extension
from Cython.Build import cythonize
import os
import numpy as np
from setuptools import Command


class ChooseVersion(Command):
    description='Choose install version. For developer choose "dev", default:"user"'
    user_options=[
        ('version="user"', 'v', 'package version')
    ]
    def __init__(self):
        if self.version=='dev':
            ext = '.pyx'
            from Cython.Build import cythonize
            extensions = cythonize(extensions)
        else:
            ext='.c'
    

extensions = [
    Extension(
        'circlehough.hough_transformation',
        sources=[os.path.join('circlehough','hough_transformation'+ext)],
        language="c",
    ),
]


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
