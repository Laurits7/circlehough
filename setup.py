from setuptools import setup
from distutils.extension import Extension
from distutils.core import Command
from Cython.Build import cythonize
import os
import numpy as np



class ChooseVersion(Command):
    description = "Choose the version to install"
    user_options = [
        ('version=', None, 'Choose version to install'),
    ]
    def initialize_options(self):
        self.version = None
    def finalize_options(self):
        assert self.foo in (None, 'dev', 'user'), 'Invalid foo!'
    def run(self):
        if self.version == 'dev':
            extensions = [
                Extension(
                    'circlehough.hough_transformation',
                    sources=[os.path.join('circlehough','hough_transformation.pyx')],
                    language="c",
                ),
            ]            
            cythonize(extensions)
        else:
            extensions = [
                Extension(
                    'circlehough.hough_transformation',
                    sources=[os.path.join('circlehough','hough_transformation.c')],
                    language="c",
                ),
            ]
    self.initialize_options()
    self.finalize_options()
    self.run()


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
        'numpy',
    ],
    cmdclass={
        'install': InstallCommand,
    }
    ext_modules=extensions,
    include_dirs=[np.get_include()],
)
