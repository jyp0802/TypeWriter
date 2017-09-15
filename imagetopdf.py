from PIL import Image

#파일 경로, 수정필요
path = "/"
files = []

#각 이미지 파일 로드
for i in range(0,25):
    filename = chr(i+97)
    files[i] = Image.open(path+"/"+filename+".png")
    files[i] = files[i].convert('RGB')

f = open(path+"/data.txt",'r')
data = f.read()
f.close()



#시작점 설정
x = 20
y = 20

antiheight = 30  #g의 가장 윗부분 높이
data = list(data)

im = Image.new("RGB",(256,256), "white")#255크기
pixels = im.load()

for i in data:
    val = ord(i)

    #data의 charactor값

    val = val-97
    width, height = files[val].size

    #gpqjy
    if(val == 7 or val == 10 or val==16 or val==17 or val==25):
        for j in range(0,width):
            for k in range(0,height):
                r,g,b = files[i].getpixel((j,k))
                if(r+g+b<100):
                    pixels[x+j,y+k] = (0,0,0)

    else:
        if( val>=0 ):
            width, height  = files[val].size
            for j in range(0, width):
                for k in range(0, height):
                    r, g, b = files[i].getpixel((j, k))
                    if (r + g + b < 100):
                        pixels[x + j, y-height+antiheight+ k] = (0, 0, 0)


        #공백
        else:
            x+=10


    x+= width

    #줄바꿈
    if(x>236):
        x = 20
        y+= 100



#im.show
im.save("reasult.png")

