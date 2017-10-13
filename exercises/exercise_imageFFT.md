### The exercise: 

1a) load an image (Cookie.jpg, Coffee.jpg, or Cardinal) as a black and white image

1b) Do the fourier transform of the image, display the (shifted) fourier spectrum in log10 

    yshift = scipy.fftpack.fftshift(y_random)
    plt.imshow(np.log10(abs(yshift)+1) ,cmap='gray')
	
1d) do the inverse fourier transform, display inversed image
	
2a) Create a random boolean mask with a parameter for the ratio

2b) Apply the boolean mask to frequency spectrum of image, setting masked values to zero, and show spectrum and inversed image after applying mask
	
3a) Create a boolean mask, masking the lowest absolute values. Again use a parameter to set the ratio. 

3b) Agauin apply the boolean mask to frequency spectrum of image, setting masked values to zero, and show spectrum and inversed image after applying mask
