# Circle Hough Transform[![Build Status](https://travis-ci.org/Laurits7/circlehough.svg?branch=master)](https://travis-ci.org/Laurits7/circlehough)



Here you find the tools to perform [Hough transform](https://en.wikipedia.org/wiki/Hough_transform) that detects circles from a 2D point cloud. In contrast with the implementation done by [Astropy](http://docs.astropy.org/en/stable/api/astropy.modeling.functional_models.Ring2D.html), this one uses triangular weighing function.

### Triangular weighing function
![Triangular weighing function](/images/triangular_weighing.png)
### Heavyside weighing used by astropy
![Heavyside weighing used by astropy](/images/heavyside.png)


## Installation

```bash
pip install git+https://github.com/Laurits7/circlehough
```

## Usage

```python
# import hough transformation. Importing numpy here only for creating the point cloud.
from circlehough.hough import main
import numpy as np
# point cloud where circle needs to be found
point_cloud  = np.array([
    [2, 0], [0, 2], [-2, 0], [0, -2],
    [np.sqrt(2), np.sqrt(2)], [np.sqrt(2), -np.sqrt(2)],
    [-np.sqrt(2), np.sqrt(2)], [-np.sqrt(2), -np.sqrt(2)],
])

# initial guess for the ring center and radius (if no previous info about those, increase uncertainty accordingly)
guessed_cx = 0.1
guessed_cy = 0.1
guessed_r = 1.9

# uncertainty of the initial guess
uncertainty = 0.2

# width where points can still be counted to be part of the ring
epsilon = 0.1

# perform the transformation
hough_cx, hough_cy, hough_r = main(
    guessed_cx, guessed_cy, guessed_r, point_cloud,
    uncertainty, epsilon
)

#return found ring center and its radius
return hough_cx, hough_cy, hough_r
```

## Example results
(Ring points are made fuzzy on purpose)
### Full circle fit
![Full circle result](/images/full_ring.png)
### Incomplete ring fit
![Incomplete ring fit](/images/half_circle.png)
## Features 

- **Triangular weighing function**: To increase accuracy of the transform instead of Heavyside function with a width epsilon a triangular weighing was used. This reduces the amount of votes given to photons that reside inside the range epsilon, but the further away they are the less they will contribute to the overall votes.

- **Iterative Hough**: Also this feature increases the accuracy of the transform by iterating several times through the accumulator, each time reducing the range and bin size (although the number of bins stays the same). In each iteration the results of last interation are taken into account.

- **Initial guess**: To reduce the amount of time required for computation, an initial guess can be given to the transformation together with the total uncertainty. In case when no initial guess is available, just increase uncertainty accordingly so the whole accumulator is filled.

- **Cython implementation**: Likewise this feature reduces computational time required. This will give the code C-like performance although code is mostly written in Python. In some test-runs speedup was increased roughly 400 times (not taking into account possibility to write everything using numpy etc.)


