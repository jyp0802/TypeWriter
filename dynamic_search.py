import numpy as np
from PIL import Image
import os
import scipy.misc


cordx = [0,0,1,-1]
cordy = [1,-1,0,0]

def check_func(x, y, cnt):
    if x<0 or y<0 or x>=width or y>=height:
        return (2*width,0,2*height,0)
    if dp_table[x,y]!=0 or image_pixels[x,y][0]==255:
        return (2*width, 0,2*height,0)

    dp_table[x,y] = cnt
    mnx = 2*width
    mxx = 0
    mny = 2*height
    mxy = 0

    for i in range(4):
        s1, e2, s2, e2 = check_func(x+cordx[i], y+cordy[i])
        mnx = min(s1, mnx)
        mxx = max(e1, mxx)
        mny = min(s2, mny)
        mxy = max(e2, mxy)

    return (mnx, mxx, mny, mxy)


def compare(x, y):
    if x[0]<y[0]:
        return 1
    elif x[0] == y[0]:
        if x[1]>y[1]:
            return 1
        else:
            return 0
    else:
        return 0


#get text label data
path = os.getcwd()
f = open(os.path.join(path, "data.txt"),'r')
label_data = f.read()
f.close()
label_data = list(label_data)


#open raw image
name = "raw_image"
raw_image = Image.open((os.path.join(path, name+".png")))

image_pixels = raw_image.load()

image_array = np.array(raw_image)
width = image_array.shape[1]
height = image_array.shape[0]

#make dynamic promgamming table
dp_table = np.zeros[width, height]
group_num = []

cnt = 1

for i in range(width):
    for j in range(height):
        if(image_pixels[i,j][0]>0 and (not dp_table[i,j]==0)):
            s1,e1,s2,e2 = check_func(i,j, cnt)
            group_num.append([s1,e1,s2,e2,cnt])
            cnt+=1


cnt-=1

group_num = sorted(group_num, cmp = compare)

cur = 0
for i in range(len(group_num)):
    if cur <i or cur == i:
        continue

    if group_num[i][1]<group_num[cur][1]:

        cnt-=1
        for j in range(group_num[i][0], group_num[i][1]+1):
            for k in range(height):
                if dp_table[j,k]==group_num[i][4]:
                    dp_table[j,k] = group_num[cur][4]

        group_num[i][4] = group_num[cur][4]

    else:
        cur = i



label_num = 0
before = -1

alphabet_check = np.zeros[26]
alphabet_distance = [[0 for i in range(26)]for j in range(26)]
cur = 0

for i in range(len(group_num)):
    if i<before or i== before:
        continue
    if(group_num[i][4]-i!=1):
        continue

    one_latter = Image.new("RGB",(group_num[1]-group_num[0]+1,group_num[3]-group_num[2]+1), "white")
    new_pixels = one_latter.load()

    for j in range(group_num[i][0], group_num[i][1]+1):
        for k in range(height):
            if(dp_table[j,k]== group_num[i][4]):
                new_pixels[j,k] = (image_pixels[j,k][0],image_pixels[j,k][1], image_pixels[j,k][2])

    alphabet = ord(label_data[label_num])-97

    if label_num>0 or label_num ==0:
        before_alpa = ord(label_data[label_num-1])
    else:
        before_alpa = -1

    alphabet_check[alphabet] +=1
    if((before>0 or before==0)and before<26):
        alphabet_check[before_alpa][alphabet].append(group_num[i][0] - group_num[before][1])

    one_latter.save(label_data[label_num]+str(alphabet_check[alphabet])+".png")

    before = i
    label_num+=1

















