import numpy as np
from PIL import Image
import os
import scipy.misc

#using example
#Thin = thinning_function_class_ver.Thinning("raw_image")
#Thin.thinning("thinned",100)

class Thinning:

    def __init__(self, filename):
        path = os.getcwd()
        self.cordX = [0, 1, 1, 1, 0, -1, -1, -1]
        self.cordY = [-1, -1, 0, 1, 1, 1, 0, -1]

        self.name = filename
        self.raw_image = Image.open((os.path.join(path, self.name + ".png")))

        self.image_pixels = self.raw_image.load()

        self.image_array = np.array(self.raw_image)
        self.width = self.image_array.shape[1]
        self.height = self.image_array.shape[0]

        self.check_array = np.zeros((self.width, self.height))

        for i in range(self.width):
            for j in range(self.height):
                if (self.image_pixels[i, j][0] + self.image_pixels[i, j][1] + self.image_pixels[i, j][2] < 350):
                    self.image_pixels[i, j] = (0, 0, 0)
                else:
                    self.image_pixels[i, j] = (255, 255, 255)

    def S(self, x,y):
        cnt = 0
        for i in range(0,8):
            if(self.image_pixels[x+self.cordX[i], y+self.cordY[i]][0]==0):
                bef_val = 1
            else:
                 bef_val =0
            if(self.image_pixels[x+self.cordX[int(i+1)%8],y+self.cordY[int(i+1)%8]][0]==0):
                cur_val = 1
            else:
                cur_val = 0

            if(bef_val==0 and cur_val ==1):
                cnt+=1


        return int(cnt)


    def N(self, x,y):
        cnt = 0
        for i in range(8):
            if(self.image_pixels[x+self.cordX[i], y+self.cordY[i]][0]==0):
                cnt+=1

        return int(cnt)


    def M(self, x,y,a,b,c):
        a-=2
        b-=2
        c-=2
        if(self.image_pixels[x+self.cordX[a],y+self.cordY[a]][0]==0 and self.image_pixels[x+self.cordX[b],y+self.cordY[b]][0]==0 and self.image_pixels[x+self.cordX[c],y+self.cordY[c]][0]==0):
            return 1
        else:
            return 0


    def thinning(self, name,threshold):
        cnt = 1
        self.threshold = 0
        while (cnt > 0 and self.threshold < threshold):
            cnt = 0
            self.threshold += 1
            for i in range(self.width):
                for j in range(self.height):
                    if (self.image_pixels[i, j][0] == 0 and i > 0 and j > 0 and i < self.width - 1 and j < self.height - 1):
                        n = self.N(i, j)
                        s = self.S(i, j)
                        # print('n:'+str(n)+", s:"+str(s))
                        if (2 <= n and n <= 6 and s == 1):
                            print("1 " + str(i) + " " + str(j))
                            m1 = self.M(i, j, 2, 4, 6)
                            m2 = self.M(i, j, 4, 6, 8)
                            if (m1 == 0 and m2 == 0):
                                self.check_array[i, j] = 1
                                print(str(i) + " " + str(j))
                                cnt += 1

            for i in range(self.width):
                for j in range(self.height):
                    if (self.check_array[i, j] != 0):
                        self.image_pixels[i, j] = (255, 255, 255)
                        self.check_array[i, j] = 0

            for i in range(self.width):
                for j in range(self.height):
                    if (self.image_pixels[i, j][0] == 0 and i > 0 and j > 0 and i < self.width - 1 and j < self.height - 1):
                        n = self.N(i, j)
                        s = self.S(i, j)
                        # print('n:' + str(n) + ", s:" + str(s))
                        if (2 <= n and n <= 6 and s == 1):
                            print("1 " + str(i) + " " + str(j))
                            m1 = self.M(i, j, 2, 4, 8)
                            m2 = self.M(i, j, 2, 6, 8)
                            if (m1 == 0 and m2 == 0):
                                self.check_array[i, j] = 1
                                print(str(i) + " " + str(j))
                                cnt += 1

            for i in range(self.width):
                for j in range(self.height):
                    if (self.check_array[i, j] != 0):
                        self.image_pixels[i, j] = (255, 255, 255)
                        self.check_array[i, j] = 0

        self.raw_image.save(name + ".png")




