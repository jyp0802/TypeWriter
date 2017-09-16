#-*- coding: utf-8 -*-

from PIL import Image
import os
import numpy as np


image = Image.open((os.path.join("a_ipad.png")))
image_array = np.array(image)
image_pixel = image.load()

width = image_array.shape[1]
height = image_array.shape[0]

im = Image.new("RGB",(width,height), "white")
pixels = im.load()

##########rgb thresholding#######
'''
threshold = 10
for ii in range(10):
    im = Image.new("RGB", (width, height), "white")
    pixels = im.load()

    for i in range(width):
        for j in range(height):
            if(image_pixel[i,j][0]+image_pixel[i,j][1]+image_pixel[i,j][2]<threshold):
                pixels[i,j] = (0,0,0)




    im.save("ipad_transfromed_"+str(threshold)+".png")
    threshold+=20
'''


####resize#####
'''
rewidth = 100
reheight = 300
#reheight = int(float(height)*float(rewidth)/float(width))

image = Image.open((os.path.join("a_ipad.png")))

image = image.resize((rewidth, reheight), Image.ANTIALIAS)
image.save(str(rewidth)+"_"+str(reheight)+".png")

'''




