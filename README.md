# Circle Hough Transform

## Overview of general Hough Transform

Hough transform is a technique used in computer vision to extract features from a set of data. This technique finds imperfect instances of objects that lie within a certain class. The best candidate is chosen via a voting procedure that is carried out in a parameter space. Collecting all votes from the parameter space (also called Hough space or accumulator) we obtain the local maxima, whose coordinates in this accumulator correspond to the best fit of the sought-after object (be it a corner, line, circle or something else).


## Circle Hough Transform

In this repository you will find the tools to perform Hough transformation that detects circles from a 2D point cloud. In the current implementation several improvements have been made to reduce computational time and to increase accuracy of the transform. 


## Features 

- **Triangular distribution**: To increase accuracy of the transform instead of delta function with a width epsilon a triangular distribution was used. This reduces the amount of votes given to photons that reside inside the range epsilon, but the further away they are the less they will contribute to the overall votes.

- **Iterative Hough**: Also this feature increases the accuracy of the transform by taking iterating several times through Hough accumulator, each time reducing the range and having a finer grid (bin size). In each iteration the results of last interation are taken into account.

- **Initial guess**: To reduce the amount of time required for computation, an initial guess can be given to the Hough transformation together with the total uncertainty. In case when no initial guess is available, just increase uncertainty accordingly so the whole Hough accumulator is filled.

- **Cython implementation**: Likewise this feature reduces computational time required. This will give the code C-like performance although code is mostly written in Python. In some test-runs speedup was increased roughly 400 times (not taking into account possibility to write everything using numpy etc.)


