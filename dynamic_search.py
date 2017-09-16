import numpy as np
from PIL import Image
import os
import scipy.misc
import sys

print(sys.getrecursionlimit())
sys.setrecursionlimit(100000)
print(sys.getrecursionlimit())

cordx = [0,0,1,-1]
cordy = [1,-1,0,0]

def check_func(x, y, cnt):
    if x<0 or y<0 or x>=width or y>=height:
        return (2*width, 0, 2*height, 0)
    if dp_table[x,y]!=0 or image_pixels[x,y][0]+image_pixels[x,y][1]+image_pixels[x,y][2]>400:
        return (2*width, 0, 2*height, 0)

    dp_table[x,y] = cnt
    mnx = 2*width
    mxx = 0
    mny = 2*height
    mxy = 0

    for i in range(4):
        s1, e1, s2, e2 = check_func(x+cordx[i], y+cordy[i], cnt)
        mnx = min(s1, mnx)
        mxx = max(e1, mxx)
        mny = min(s2, mny)
        mxy = max(e2, mxy)
    mnx = min(mnx, x)
    mxx = max(mxx, x)
    mny = min(mny, y)
    mxy = max(mxy, y)


    return (mnx, mxx, mny, mxy)


def compare(x, y):
    if x[0]<y[0]:
        return 1
    elif x[0] == y[0]:
        if x[1]>y[1]:
            return 1
        else:
            return -1
    else:
        return -1


#get text label data
path = os.getcwd()
f = open(os.path.join(path, "raw_data.txt"),'r')
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
dp_table = np.zeros((width, height))
group_num = []

cnt = 1

for i in range(width):
    for j in range(height):
        if(image_pixels[i,j][0]+image_pixels[i,j][1]+image_pixels[i,j][2]<400 and  dp_table[i,j]==0):
            s1,e1,s2,e2 = check_func(i,j, cnt)
            group_num.append([s1,e1,s2,e2,cnt])
            cnt+=1
            #print("i,j"+str(i)+str(j))


cnt-=1

print("cnt : "+str(cnt))

group_num = sorted(group_num, key = lambda x:(x[0], -x[1]))
cur = 0
for i in range(len(group_num)):
    if i<cur or cur == i:
        continue

    if group_num[i][1]<=group_num[cur][1]:

        cnt-=1
        for j in range(group_num[i][0], group_num[i][1]+1):
            for k in range(height):
                if dp_table[j,k]==group_num[i][4]:
                    dp_table[j,k] = group_num[cur][4]
        print("merged"+str(cur))
        group_num[i][4] = group_num[cur][4]

        group_num[cur][0] = min(group_num[cur][0],group_num[i][0])
        group_num[cur][1] = max(group_num[cur][1],group_num[i][1])
        group_num[cur][2] = min(group_num[cur][2],group_num[i][2])
        group_num[cur][3] = max(group_num[cur][3],group_num[i][3])



    else:
        cur = i

print("cnt : "+str(cnt))

label_num = 0
before = -1

alphabet_check = np.zeros(26)
alphabet_distance = [[[0 for i in range(0)]for j in range(26)]for k in range(26)]
cur = 0

for i in range(len(group_num)):
    if i<before or i== before:
        continue
    if(group_num[i][4]-i!=1):
        continue

    new_width = group_num[i][1]-group_num[i][0]+1
    new_height = group_num[i][3]-group_num[i][2]+1
    print(i)
    print(new_width)
    print(new_height)

    one_latter = Image.new("RGB",(new_width, new_height), "white")
    new_pixels = one_latter.load()

    for j in range(new_width):
        for k in range(new_height):
            if(dp_table[j+group_num[i][0],k+group_num[i][2]]== group_num[i][4]):
                new_pixels[j,k] = (image_pixels[j+group_num[i][0],k+group_num[i][2]][0],image_pixels[j+group_num[i][0],k+group_num[i][2]][1], image_pixels[j+group_num[i][0],k+group_num[i][2]][2])

    alphabet = ord(label_data[label_num])-97

    if label_num>0 or label_num ==0:
        before_alpa = ord(label_data[label_num-1])-97
    else:
        before_alpa = -1

    alphabet_check[alphabet] = int(alphabet_check[alphabet]+1)
    if((before>0 or before==0)and before<26):
        print("alphabet")
        print(before_alpa)
        print(alphabet)
        print(group_num[i][0])
        print(group_num[before][1])
        alphabet_distance[before_alpa][alphabet].append(group_num[i][0] - group_num[before][1])

    one_latter.save(path+"/dynamic_data/"+label_data[label_num]+str(int(alphabet_check[alphabet]))+".png")
    print(str(alphabet_check[alphabet]))
    before = i
    label_num+=1

















