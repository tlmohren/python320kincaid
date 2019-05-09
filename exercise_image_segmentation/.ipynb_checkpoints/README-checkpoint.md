## Image segmentation

This Python exercise is about how to work with discrete interesting sections of images after reading in the photograph. For example, extracting specific cell clusters / brain regions or segmenting an aerial photograph by foliage color.

**Note:** I haven't actually tried these exercises yet so it's possible some of them are very hard or too easy. For Python Club please try one (or more, if you want!) of the tasks, and we can talk about the process even if the code didn't work. I intentionally made a lot of problems, so hopefully there's at least one that's interesting to you or relevant to your work.

[Contour finding](https://scikit-image.org/docs/stable/auto_examples/edges/plot_contours.html#sphx-glr-auto-examples-edges-plot-contours-py) in Scikit-image might be helpful for all of the tasks (we talked about this briefly during our image analysis week). The [Shapely](https://pypi.org/project/Shapely/) library might also be helpful for shape manipulation.

Here is the fake "image" to work on:
![](./blob1.jpg)

#### Edge detection problem
1. Extract the outer edge of the large light blue blob as a vector path.
2. Extract the edges of each of the smaller inner blobs as separate vector paths.

#### Distance problem
1. How far away is the centroid of each inner blob from the nearest edge of the large light blue blob?

#### Smoothing problem
1. The small dark blue blob is very bumpy. Extract the vector outline of this path and make it smoother.

#### Concentric circles problem
1. Using the vector shape of one of the orange blobs, create 10 concentric circles that radiate inward toward the center (like this):
![](./concentric_blobs_example.jpg)

#### Area problem
1. How much area in this image is covered by orange?
