# Extracting dominant colors from a photo

This exercise is to pull out the 3 dominant colors from a photo using [k-means clustering](https://home.deib.polimi.it/matteucc/Clustering/tutorial_html/kmeans.html). This might be useful if you wanted to extract objects from an image based on color, but didn't know ahead of time which colors to use. 

Generally, this should involve reading in the image as a matrix of tuples (R, G, B values for each pixel), and then running some kind of k-means cluster analysis on the 3D matrix. 

For example, running your code on the two test images (`./data/cardinal.jpg` & `./data/mountain.jpg`) should return something like this. 

![clustering answers](./exercises/answers/kmeans_answers.jpg)

*Note: k-means is not deterministic so you may end up with a slightly different result. But the answers shouldn't be drastically different.*

### Hints

The cluster analysis should be under 10 lines of code if using the OpenCV library. If OpenCV is causing issues, you can use a different machine learning library or implement k-means by hand: 

1. Pick 3 random pixel data points as the starting cluster centroids
2. Calculate the straight-line distance between each centroid and every single other pixel
3. Assign each pixel to one of the 3 clusters by picking its nearest centroid
4. Take the mean values of each cluster as the new set of 3 centroids
5. Repeat this process ~10 times to refine centroid locations ()
6. Return the final 3 centroid pixels

Common issues with image processing: 
1. OpenCV uses `(B, G, R)` as the default color system, and matplotlib uses `(R, G, B)`. You'll probably need to convert colorspaces if using both libraries. 
2. Matplotlib doesn't automatically garbage collect figures, so figures will indefinitely build up in your computer and cause a memory leak. To fix this you can manually close a figure (`fig = plt.figure()`) with `plt.close(fig)` or `plf.close('all')`. `del fig` doesn't work, and neither does assigning `fig` to a different variable, because of reasons.