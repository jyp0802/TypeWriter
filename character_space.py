from PIL import Image
img = Image.open("inp.png")
txt = "aabacadaeafagahaiajakalamanaoapaqarasa"
w, h = img.size

p_img = img.load()

data = [] #[hor dist, ver dist, cnt]
for i in range(26):
    data.append([])
    for j in range(26):
        data[i].append([0,0,0])

cc = 0
tmp = False
ht = False

dt = [] #[hor start, hor end, ver start, ver end]
for j in range(len(txt)):
    dt.append([0,0,0,0])

for i in range(w):
    ht = False
    for j in range(h):
        r,g,v = p_img[i,j]
        if (r+g+v<200):
            if (not tmp):
                tmp = True
                dt[cc][0] = i
                dt[cc][2] = j
                dt[cc][3] = j
            ht = True
            if (j > dt[cc][2]):
                dt[cc][2] = j
            elif (j < dt[cc][3]):
                dt[cc][3] = j
        elif ((j == h-1) and (not ht) and tmp):
            tmp = False
            dt[cc][1] = i-1
            cc += 1


for c in range(1,len(txt)):
    x = ord(txt[c-1]) - ord('a')
    y = ord(txt[c]) - ord('a')
    data[x][y][0] += dt[c][0] - dt[c-1][1]
    #data[x][y][1] += dt[c][0] - dt[c-1][1]
    data[x][y][2] += 1

print dt
print data[0]