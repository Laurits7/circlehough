from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize


extensions = [
    Extension(
        'hough_transformation', ['hough_transformation.pyx'],
    )
]


setup(
    name="circlehough",
    version='0.0.1',
    description='Perform Hough transformation for circle',
    url='https://github.com/Laurits7/circlehough',
    author='Laurits Tani',
    author_email='laurits.tani@gmail.com',
    licence='MIT',
    install_requires=[
        'cython',
        'numpy',
    ],
    ext_modules=cythonize(extensions),
)