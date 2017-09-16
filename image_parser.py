from PIL import Image
import numpy as np
import scipy.misc

# image read
original_image = Image.open('original5.png')

# pixeling, array
original_array = np.array(original_image)
original_pixels = original_image.load()

# divide image to top and bottom row -> abc.. & ABC..
firstRow = False
noBlack = True
middle = -1;

# background color with white, alphabet with red
for j in range(original_array.shape[0]):
    for i in range(original_array.shape[1]):
        if original_pixels[i, j][0] + original_pixels[i, j][1] + original_pixels[i, j][2] < 360:
            original_pixels[i, j] = (0, 0, 0)
            firstRow = True
            noBlack = False
        else:
            original_pixels[i, j] = (255, 255, 255)
    if (middle < 0 and firstRow and noBlack):
    	middle = j+1
    noBlack = True


print (original_array.shape[0])

# modified image with black, white background
scipy.misc.imsave("modified.png", original_image)
modified_image = Image.open("modified.png")
modified_array = np.array(modified_image)
modified_pixels = modified_image.load()

# alphabet parsing
print (modified_array.shape[0])
print (modified_array.shape[1])
print (middle)

isDetected = False

height = [0,middle,modified_array.shape[0]]
width = modified_array.shape[1]

capital_or_not = ['0', 'c']

for t in range(2):
    num_of_white = 0
    ver_min = 10000
    ver_max = 0
    horizontal_min = 10000
    horizontal_max = 0
    index = 0
    for i in range(width):
        for j in range(height[t],height[t+1]):
            if modified_pixels[i, j][1] == 0:
                isDetected = True
                ver_min = min(ver_min, j)
                ver_max = max(ver_max, j)
                horizontal_min = min(horizontal_min, i)
                horizontal_max = max(horizontal_max, i)
            else:
                num_of_white = num_of_white + 1

        if (num_of_white == height[t+1]-height[t]) and isDetected:
            img = modified_array[ver_min:ver_max, horizontal_min:horizontal_max]
            scipy.misc.imsave(chr(97+index)+capital_or_not[t]+'.png', img)
            index = index + 1
            isDetected = False
            num_of_white = 0
            ver_min = 10000
            ver_max = 0
            horizontal_min = 10000
            horizontal_max = 0
        num_of_white = 0
