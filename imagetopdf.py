from PIL import Image
import os
import numpy as np
#파일 경로, 수정필요

path = os.getcwd()
file_path = [''] * 26
files = [Image] * 26

#각 이미지 파일 로드
for i in range(0,26):
    filename = chr(i+97)
    #file_path.append((os.path.join(path, filename+".png")))
    #image = Image.open((os.path.join(path, filename+".png")))
    #files.append(image.getdata())
    #print (files[i])

    #files += [Image.open((os.path.join(path, filename+".png")))]
    #print (os.path.join(path, filename+".png"))
    #files[i] = files[i].convert('RGB')

f = open(os.path.join(path, "data.txt"),'r')

data = f.read()
f.close()


#시작점 설정
x = 20
y = 20

antiheight = 70  #g의 가장 윗부분 높이
data = list(data)
width_of_image = 1024
height_of_image = 1024
space = 30

im = Image.new("RGB",(width_of_image,height_of_image), "white")#255크기
pixels = im.load()


for i in data:
    val = ord(i)

    #data의 charactor값
    val = val-97

    if val < 0 or val > 25:
        x = x + space
        continue

    #files[val] = Image.open(file_path[val])


    image = Image.open((os.path.join(path, i+".png")))
    image_array = np.array(image)
    image_pixel = image.load()

    width = image_array.shape[1]
    height = image_array.shape[0]


    #gpqjy
    if(val == 6 or val == 9 or val==15 or val==16 or val==24):
        for j in range(width):
            for k in range(height):
                #rgb = files[i].load()
                #print (image_pixel[j, k])
                if image_pixel[j, k][0] + image_pixel[j, k][1] + image_pixel[j, k][2] < 400:
                    pixels[x+j, y+k] = (0, 0, 0)

            #r,g,b = files[i].getpixel((j,k))
                #if(r+g+b<100):
                    #pixels[x+j,y+k] = (0,0,0)


    # 나머지 a~
    else:
        if( val>=0 ):
            for j in range(width):
                for k in range(height):
                    if image_pixel[j, k][0] + image_pixel[j, k][1] + image_pixel[j, k][2] < 400:
                        print (x + j)
                        print ("a")
                        print (y+k)
                        print (height)

                        print (y-height+antiheight+ k)
                        pixels[x + j, y-height+antiheight+ k] = (0, 0, 0)


        #공백
        else:
            x+=10


    x+= width

    #줄바꿈
    if(x>width_of_image-50):
        print ("new line")
        x = 20
        y+= 100



#im.show
im.save("result.png")

