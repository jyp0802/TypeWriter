from PIL import Image
import os
import numpy as np

# image array with alphabet
files = [Image] * 26

# read data files with input string
path = os.getcwd()
f = open(os.path.join(path, "data.txt"),'r')
data = f.read()
f.close()
data = list(data)

# basic parameters (image width, height, space width, starting point)
antiheight = 40  #g의 가장 윗부분 높이
width_of_image = 1024
height_of_image = 1024
width_of_space = 30
word_coord_x = int(width_of_image / 15)
word_coord_y = int(height_of_image / 15)

# making new sketchbook (1024 * 1024)
im = Image.new("RGB",(width_of_image,height_of_image), "white")
pixels = im.load()

# writing a hand-written alphabet
for i in data:

    #data의 charactor값
    val = ord(i)
    val = val-97

    # if it is not a alphabet
    if val < 0 or val > 25:
        word_coord_x = word_coord_x + width_of_space
        continue

    # image open each alphabet
    image = Image.open((os.path.join(path, i+".png")))
    image_array = np.array(image)
    image_pixel = image.load()

    # each alphabet's width, height
    width = image_array.shape[1]
    height = image_array.shape[0]

    # alphabet "gpqy"
    if(val == 6 or val==15 or val==16 or val==24):
        for j in range(width):
            for k in range(height):
                if image_pixel[j, k][0] + image_pixel[j, k][1] + image_pixel[j, k][2] < 360:
                    pixels[word_coord_x+j, word_coord_y+k] = (0, 0, 0)

    # alphabet "j" (adjusted height)
    elif(val == 9):
        for j in range(width):
            for k in range(height):
                if image_pixel[j, k][0] + image_pixel[j, k][1] + image_pixel[j, k][2] < 360:
                    pixels[word_coord_x+j, word_coord_y+k-10] = (0, 0, 0)

    # a to z except "gpqjy"
    else:
        for j in range(width):
            for k in range(height):
                if image_pixel[j, k][0] + image_pixel[j, k][1] + image_pixel[j, k][2] < 360:
                    pixels[word_coord_x + j, word_coord_y-height+antiheight+ k] = (0, 0, 0)


    # width plus for next alphabet
    word_coord_x+= width

    # new line rules
    if(word_coord_x>width_of_image-int(width_of_image / 15)):
        print ("new line")
        word_coord_x = int(width_of_image / 15)
        word_coord_y += int(height_of_image / 8)


im.save("result.png")

