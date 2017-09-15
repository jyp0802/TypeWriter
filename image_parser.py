from PIL import Image
import numpy as np
import scipy.misc

# image read
original_image = Image.open('original.png')

# pixeling, array
original_array = np.array(original_image)
pixels = original_image.load()

# background color with white, alphabet with red
for i in range(original_array.shape[1]):
    for j in range(original_array.shape[0]):
        if pixels[i, j][0] + pixels[i, j][1] + pixels[i, j][2] < 400:
            pixels[i, j] = (255, 0, 0)
        else:
            pixels[i, j] = (255, 255, 255)

# alphabet parsing
print (original_array.shape[0])
print (original_array.shape[1])

isDetected = False
num_of_white = 0
ver_min = 10000
ver_max = 0
horizontal_min = 10000
horizontal_max = 0
index = 0


for i in range(original_array.shape[1]):
    for j in range(original_array.shape[0]):
        if pixels[i, j][1] == 0:
            isDetected = True
            ver_min = min(ver_min, j)
            ver_max = max(ver_max, j)
            horizontal_min = min(horizontal_min, i)
            horizontal_max = max(horizontal_max, i)
        else:
            num_of_white = num_of_white + 1


    if (num_of_white == original_array.shape[0]) and isDetected:
        #print (ver_min, ver_max, horizontal_min, horizontal_max)
        img = original_array[ver_min:ver_max, horizontal_min:horizontal_max]
        scipy.misc.imsave(chr(97+index)+'.png', img)
        index = index + 1
        isDetected = False
        num_of_white = 0
        ver_min = 10000
        ver_max = 0
        horizontal_min = 10000
        horizontal_max = 0
    num_of_white = 0

#original_image.show()