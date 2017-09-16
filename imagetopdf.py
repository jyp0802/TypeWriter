#-*- coding: utf-8 -*-

from PIL import Image
import os
import numpy as np
from random import randint

# image array with alphabet
files = [Image] * 26

# read data files with input string
path = os.getcwd()
f = open(os.path.join(path, "data.txt"), 'r')
data = f.read()
f.close()
data = list(data)

# resizing a image with standards
# a b c d e f  g  h  i    j  k  l m n o p q r s t u v w x y z
# 1 2 1 2 1 2  2  2 1.5  2.5 2  2 1 1 1 2 2 1 1 2 1 1 1 1 2 1
# 0 1 2 3 4 5  6  7  8    9  10 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5
# 1 means 40


def resize_with_formal_style(standard_height = None):
    for image_index in range(26):
        img = Image.open((os.path.join(path, chr(image_index+97)+"0.png")))

        if (image_index == 1 or image_index == 3 or image_index == 5 or image_index == 6 or image_index == 7 or
                    image_index == 10 or image_index == 11 or image_index == 15 or image_index == 16 or image_index == 19 or image_index == 24):
            standard_height = 80
        elif image_index == 8:
            standard_height = 60
        elif image_index == 9:
            standard_height = 100
        else:
            standard_height = 40

        height_ratio = (standard_height / float(img.size[1]))
        width_size = int((float(img.size[0]) * float(height_ratio)))
        img = img.resize((width_size, standard_height), Image.ANTIALIAS)
        dir = chr(image_index+97)+"0.png"
        img.save(dir.lower())

    for image_index in range(26):
        standard_height = 80
        img = Image.open((os.path.join(path, chr(image_index+97)+"c.png")))
        height_ratio = (standard_height / float(img.size[1]))
        width_size = int((float(img.size[0]) * float(height_ratio)))
        img = img.resize((width_size, standard_height), Image.ANTIALIAS)
        dir = chr(image_index+97)+"c.png"
        img.save(dir.lower())


def resize_with_casual_style(standard_height = None):
    # lower case

    for image_index in range(26):
        rand_num = randint(-7, 2)
        standard_height = 46 + rand_num
        img = Image.open((os.path.join(path, chr(image_index+97)+"0.png")))
        # standard "A"
        if image_index == 0:
            height_ratio = (standard_height / float(img.size[1]))
            width_size = int((float(img.size[0]) * float(height_ratio)))
            img = img.resize((width_size, standard_height), Image.ANTIALIAS)

        else:
            width_size = int((float(img.size[0]) * float(height_ratio)))
            height_size = int((float(img.size[1]) * float(height_ratio)))
            img = img.resize((width_size + rand_num, height_size + rand_num), Image.ANTIALIAS)

        dir = chr(image_index+97)+"0.png"
        img.save(dir.lower())


    # upper case
    for image_index in range(26):
        rand_num = randint(-15, -6)
        standard_height = 78 + rand_num
        img = Image.open((os.path.join(path, chr(image_index+97)+"c.png")))
        height_ratio = (standard_height / float(img.size[1]))
        width_size = int((float(img.size[0]) * float(height_ratio)))
        img = img.resize((width_size + rand_num, standard_height + rand_num), Image.ANTIALIAS)
        dir = chr(image_index+97)+"c.png"
        img.save(dir.lower())

resize_with_casual_style()
is_casual=True
#resize_with_formal_style()

# distance between alphabet (x axis)
afile = open('res', 'r')
adata = afile.read();
adata = adata.split();
array = []
for i in range(26):
    array.append([])
    for j in range(26):
        if (int(adata[(3 * j) + (3 * 26 * i) + 2]) > 0):
            array[i].append(int(int(adata[(3 * j) + (3 * 26 * i)]) / int(adata[(3 * j) + (3 * 26 * i) + 2])))
        else:
            array[i].append(0)


# basic parameters (image width, height, space width, starting point)
width_of_image = 2048
height_of_image = 2048
antiheight = int(height_of_image / 60)  #g의 가장 윗부분 높이
width_of_space = int(width_of_image / 30)
word_coord_x = int(width_of_image / 10)
word_coord_y = int(height_of_image / 10)

pred_word = None
current_word = None

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
        # space
        if val == -65:
            word_coord_x = word_coord_x + width_of_space
        # enter(carriage return)
        elif val == -87:
            print("new line")
            word_coord_x = int(width_of_image / 15)
            word_coord_y += int(height_of_image / 8)

        # capital word
        elif (val > -33) and (val < -6):
            capital_image = Image.open((os.path.join(path, i + "c.png")))
            capital_image_array = np.array(capital_image)
            capital_image_pixel = capital_image.load()

            width = capital_image_array.shape[1]
            height = capital_image_array.shape[0]
            rand_num = randint(-5, 5)

            for j in range(width):
                for k in range(height):
                    if capital_image_pixel[j, k][0] + capital_image_pixel[j, k][1] + capital_image_pixel[j, k][2] < 360:
                        if is_casual:
                            pixels[word_coord_x + j + 5, word_coord_y-height+antiheight+ k + rand_num] = (0, 0, 0)
                        else:
                            pixels[word_coord_x + j + 5, word_coord_y-height+antiheight+ k] = (0, 0, 0)

            word_coord_x += (width + 5)
            if (word_coord_x > width_of_image - int(width_of_image / 15)):
                print("new line")
                word_coord_x = int(width_of_image / 15)
                word_coord_y += int(height_of_image / 8)


        pred_word = None
        continue

    # image open each alphabet
    image = Image.open((os.path.join(path, i+"0.png")))
    image_array = np.array(image)
    image_pixel = image.load()

    # each alphabet's width, height
    width = image_array.shape[1]
    height = image_array.shape[0]
    current_word = val
    rand_num = randint(-7, 7)

    if pred_word is None:
        shift = 0

    else:
        shift = array[pred_word][current_word]

    # alphabet "gpqy"
    if(val == 6 or val==15 or val==16 or val==24):
        for j in range(width):
            for k in range(height):
                if image_pixel[j, k][0] + image_pixel[j, k][1] + image_pixel[j, k][2] < 360:
                    if is_casual:
                        pixels[word_coord_x + j + shift, word_coord_y + k + rand_num] = (0, 0, 0)
                    else:
                        pixels[word_coord_x + j + shift, word_coord_y+k] = (0, 0, 0)


    # alphabet "j" (adjusted height)
    elif(val == 9):
        for j in range(width):
            for k in range(height):
                if image_pixel[j, k][0] + image_pixel[j, k][1] + image_pixel[j, k][2] < 360:
                    if is_casual:
                        pixels[word_coord_x + j + shift, word_coord_y + k - 10 + rand_num] = (0, 0, 0)
                    else:
                        pixels[word_coord_x + j + shift, word_coord_y+k-10] = (0, 0, 0)

    # a to z except "gpqjy"
    else:
        for j in range(width):
            for k in range(height):
                if image_pixel[j, k][0] + image_pixel[j, k][1] + image_pixel[j, k][2] < 360:
                    if is_casual:
                        pixels[word_coord_x + j + shift, word_coord_y - height + antiheight + k+ rand_num] = (0, 0, 0)
                    else:
                        pixels[word_coord_x + j + shift, word_coord_y-height+antiheight+ k] = (0, 0, 0)


    # width plus for next alphabet
    word_coord_x+= (width+shift)

    # new line rules
    if(word_coord_x>width_of_image-int(width_of_image / 15)):
        print ("new line")
        word_coord_x = int(width_of_image / 15)
        word_coord_y += int(height_of_image / 8)

    pred_word = current_word

im.save("result.png")

