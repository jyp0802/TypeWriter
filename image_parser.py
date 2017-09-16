from PIL import Image
import numpy as np
import scipy.misc

# image read
original_image = Image.open('original4.png')

# pixeling, array
original_array = np.array(original_image)
original_pixels = original_image.load()

# background color with white, alphabet with red
for i in range(original_array.shape[1]):
    for j in range(original_array.shape[0]):
        if original_pixels[i, j][0] + original_pixels[i, j][1] + original_pixels[i, j][2] < 360:
            original_pixels[i, j] = (0, 0, 0)
        else:
            original_pixels[i, j] = (255, 255, 255)


# modified image with black, white background
scipy.misc.imsave("modified.png", original_image)
modified_image = Image.open("modified.png")
modified_array = np.array(modified_image)
modified_pixels = modified_image.load()

# alphabet parsing
print (modified_array.shape[0])
print (modified_array.shape[1])

isDetected = False
num_of_white = 0
ver_min = 10000
ver_max = 0
horizontal_min = 10000
horizontal_max = 0
index = 0


for i in range(modified_array.shape[1]):
    for j in range(modified_array.shape[0]):
        if modified_pixels[i, j][1] == 0:
            isDetected = True
            ver_min = min(ver_min, j)
            ver_max = max(ver_max, j)
            horizontal_min = min(horizontal_min, i)
            horizontal_max = max(horizontal_max, i)
        else:
            num_of_white = num_of_white + 1


    if (num_of_white == modified_array.shape[0]) and isDetected:
        #print (ver_min, ver_max, horizontal_min, horizontal_max)
        img = modified_array[ver_min:ver_max, horizontal_min:horizontal_max]
        scipy.misc.imsave(chr(97+index)+'.png', img)
        index = index + 1
        isDetected = False
        num_of_white = 0
        ver_min = 10000
        ver_max = 0
        horizontal_min = 10000
        horizontal_max = 0
    num_of_white = 0

