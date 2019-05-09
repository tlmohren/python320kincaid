# Working with Image Sequences
This is an exercise in working with images that are related to each other in some way (e.g. multiple images in time or acquired at different depths).

### Useful package: `pims`
Often images are stored in a sequence of separate images, and other times images sequences are stored in a single multi-page file (usually TIFF format).

This can lead to writing a lot of boiler-plate code to open a sequence of images saved in a particular format. 

I've found the [pims package](http://soft-matter.github.io/pims/v0.4.1/)
(for 'Python Image Sequence') to be quite useful. This package provides utilities for loading images on-the-fly, as a python iterator type--especially handy for large data sets!

It has a lot of other useful features for customization that I have not had need to play around with yet. 

It works with Anaconda or `pip`, the 
[installation instructions](http://soft-matter.github.io/pims/v0.4.1/install.html) are helpful.

Though this package may be helpful, there are many ways to load many images
in Python, please share your own method if you have one you like!

#### The dataset
I have sent a Dropbox link to a folder that contains a 3D image of 
fluorescently labeled skin cells in a zebrafish larvae (the field of
view is ~350µm);
I have wounded
the larvae, causing a tear in the skin top right corner of the image. The
skin almost instantly begins to heal, and the larvae easily recovers from
this injury and can even fully regenerate.

## Exercise: Projecting 3D images into 2D
  1. Download the test image sequence from the Dropbox link in the email. It is available as a single-page TIFF file or a folder of individual images, whichever you find might be more relevant to work with. 
  2. Load the image sequence into Python. Figure out how many images are in the sequence (you can check by looking at the folder of individual images!).Also figure out the x/y dimensions of the image.
  3. Perform a maximum intensity projection: for each pixel, find the maximum intensity value across all the images in the sequence. There is a `MaxZ.tif` file in the Dropbox folder so you can check your work.
  4. Perform a median intensity projection (i.e. calculate the median pixel-wise). There is a `medianZ.tif` file in the Dropbox folder to check your work.
  5. Extension task (if that was boring): Apply some filters to the data, e.g. a Gaussian low-pass filter or an edge-detection filter. `scikit-image` is a good resource for high-level functions like this (do you know of others?).
