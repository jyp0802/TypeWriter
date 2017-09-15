from PIL import Image
import numpy as np
import scipy.misc

# image read
original_image = Image.open('original.png')

# pixeling, array (1470, 170)
original_array = np.array(original_image)
pixels = original_image.load()

# image with rotated (170, 1470)
rotated_array = np.rot90(original_array)
#scipy.misc.imsave('outfile.png', rotated_array)


for i in range(rotated_array.shape[0]):
    for j in range(rotated_array.shape[1]):
        if pixels[i, j][0] + pixels[i, j][1] + pixels[i, j][2] < 400:
            pixels[i, j] = (255, 0, 0)
        else:
            pixels[i, j] = (255, 255, 255)


original_image.show()