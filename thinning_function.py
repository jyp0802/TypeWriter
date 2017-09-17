import numpy as np
from PIL import Image
import os
import scipy.misc


path = os.getcwd()

cordX = [0,1,1,1,0,-1,-1,-1]
cordY = [-1,-1,0,1,1,1,0,-1]

def S(x,y):
    cnt = 0
    for i in range(0,8):
        if(image_pixels[x+cordX[i], y+cordY[i]][0]==0):
            bef_val = 1
        else:
             bef_val =0
        if(image_pixels[x+cordX[int(i+1)%8],y+cordY[int(i+1)%8]][0]==0):
            cur_val = 1
        else:
            cur_val = 0

        if(bef_val==0 and cur_val ==1):
            cnt+=1


    return int(cnt)


def N(x,y):
    cnt = 0
    for i in range(8):
        if(image_pixels[x+cordX[i], y+cordY[i]][0]==0):
            cnt+=1

    return int(cnt)


def M(x,y,a,b,c):
    a-=2
    b-=2
    c-=2
    if(image_pixels[x+cordX[a],y+cordY[a]][0]==0 and image_pixels[x+cordX[b],y+cordY[b]][0]==0 and image_pixels[x+cordX[c],y+cordY[c]][0]==0):
        return 1
    else:
        return 0



#open raw image
name = "raw_image"
raw_image = Image.open((os.path.join(path, name+".png")))

image_pixels = raw_image.load()

image_array = np.array(raw_image)
width = image_array.shape[1]
height = image_array.shape[0]

check_array = np.zeros((width, height))

for i in range(width):
    for j in range(height):
        if(image_pixels[i,j][0]+image_pixels[i,j][1]+image_pixels[i,j][2]<350):
            image_pixels[i,j] = (0,0,0)
        else:
            image_pixels[i,j] = (255,255,255)

cnt = 1
while(cnt>0):
    cnt =0
    for i in range(width):
        for j in range(height):
            if(image_pixels[i,j][0]==0 and i>0 and j>0 and i<width-1 and j<height-1):
                n = N(i,j)
                s = S(i,j)
                #print('n:'+str(n)+", s:"+str(s))
                if(2<=n and n<=6 and s==1):
                    print("1 " + str(i) + " " + str(j))
                    m1 = M(i,j,2,4,6)
                    m2 = M(i,j,4,6,8)
                    if(m1==0 and m2 ==0):
                        check_array[i,j] = 1
                        print(str(i)+" "+str(j))
                        cnt+=1



    for i in range(width):
        for j in range(height):
            if(check_array[i,j]!=0):
                image_pixels[i,j] = (255,255,255)
                check_array[i,j] = 0


    for i in range(width):
         for j in range(height):
             if (image_pixels[i, j][0] == 0 and i > 0 and j > 0 and i < width - 1 and j < height - 1):
                 n = N(i, j)
                 s = S(i, j)
                 #print('n:' + str(n) + ", s:" + str(s))
                 if (2 <= n and n <= 6 and s == 1):
                     print("1 "+str(i) + " " + str(j))
                     m1 = M(i, j, 2, 4, 8)
                     m2 = M(i, j, 2, 6, 8)
                     if (m1 == 0 and m2 == 0):
                         check_array[i, j] = 1
                         print(str(i) + " " + str(j))
                         cnt+=1



    for i in range(width):
        for j in range(height):
            if(check_array[i,j]!=0):
                image_pixels[i,j] = (255,255,255)
                check_array[i,j] = 0



raw_image.save("Thinning"+".png")
