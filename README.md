# Circle Hough Transform


Here you find the tools to perform [Hough transform](https://en.wikipedia.org/wiki/Hough_transform) that detects circles from a 2D point cloud. In contrast with the implementation done by [Astropy](http://docs.astropy.org/en/stable/api/astropy.modeling.functional_models.Ring2D.html), this one uses triangular weighing function.


![Triangular weighing function](/images/triangular_weighing.png)
![Heavyside weighing used by astropy](/images/heavyside.png)

## Features 

- **Triangular weighing function**: To increase accuracy of the transform instead of Heavyside function with a width epsilon a triangular weighing was used. This reduces the amount of votes given to photons that reside inside the range epsilon, but the further away they are the less they will contribute to the overall votes.

- **Iterative Hough**: Also this feature increases the accuracy of the transform by iterating several times through the accumulator, each time reducing the range and bin size (although the number of bins stays the same). In each iteration the results of last interation are taken into account.

- **Initial guess**: To reduce the amount of time required for computation, an initial guess can be given to the transformation together with the total uncertainty. In case when no initial guess is available, just increase uncertainty accordingly so the whole accumulator is filled.

- **Cython implementation**: Likewise this feature reduces computational time required. This will give the code C-like performance although code is mostly written in Python. In some test-runs speedup was increased roughly 400 times (not taking into account possibility to write everything using numpy etc.)


