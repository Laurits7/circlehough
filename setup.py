from distutils.core import setup
from Cython.Build import cythonize

setup(
    name="houghTransform_circle",
    version='0.0.1',
    description='Perform Hough transformation for circle',
    url='https://github.com/Laurits7/Hough_transform_for_circles',
    author='Laurits Tani',
    author_email='laurits.tani@gmail.com',
    licence='MIT',
    install_requires=[
        'cython',
        'numpy',
    ],
    ext_modules=cythonize('hough_transformation.pyx'),
)