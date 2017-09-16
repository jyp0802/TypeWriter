from PIL import Image
import os

txt = ["aabacadaeagahaiajakalamanaoapaqarasa","tauavawaxayaza",
       "abbcbdbebfbgbhbibjbkblbmbnbobqbrbsbtbubvbwbx","xbybzb",
       "bccdcecfcgchcicjckclcmcncocpcqcrcsctcucvcw","cxcyczc",
       "cddedfdgdhdidjdkdldmdndodpdqdrdsdtdudvdwd","xdydzd",
       "deefegeheiejekelemeneoepeqereseteuevewexe","effgfhfifjfkflmfnfofpfqfrfsftfufvfwfxfyf",
       "zf","fgghgigjgkglgmgngogpgqgrgsgtgugvgwgxgygzg",
       "hiijikiliminioipiqirisitiuiviwixiyizi","ijjkjljmjnjojpjqjrjsjtjujvjwjxjyjzj",
       "yeze","jkklkmknkokpkqkrksktkukvkwkxkykzk",
       "kllmlnlolplqlrlsltlulvlwlxlylzl","lmmnmompmqmrmsmtmumvmwmxmymzm",
       "mnnonpnqnrnsntnunvnwnxnynzn","noopoqorosotouovowoxoyozo",
       "oppqprpsptpupvpwpxpypzp","pqqrqsqtquqvqwqxqyqzq",
       "qrrsrtrurvrwrxryrzr","rsstsusvswsxsyszs",
       "sttutvtwtxtytzt","tuuvwuxuyuzu",
       "vwwxwywzw","wxxyxzxyyzyzz",
       "ghhihjhkhlhmhnhohphqhrhshthuhvhwhxhyhzh"]

if (os.path.isfile('res')):
    print "ASD"
    afile = open('res', 'r')
    adata = afile.read();
    adata = adata.split();
    data = []
    for i in range(26):
        data.append([])
        for j in range(26):
            data[i].append([int(adata[(3*j)+(26*i)]),int(adata[(3*j)+(26*i)+1]),int(adata[(3*j)+(26*i)+2])])
else:
    data = []  # [hor dist, ver dist, cnt]
    for i in range(26):
        data.append([])
        for j in range(26):
            data[i].append([0, 0, 0])

for pic in range(len(txt)):
    path = "in" + str(pic + 1) + ".png"
    img = Image.open(path)
    w, h = img.size

    p_img = img.load()

    cc = 0
    tmp = False
    ht = False

    dt = [] #[hor start, hor end, ver start, ver end]
    for j in range(len(txt[pic])):
        dt.append([0,0,0,0])

    for i in range(w):
        ht = False
        for j in range(h):
            P = p_img[i,j]
            if (P[0]+P[1]+P[2]<400):
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
    if (not (cc ==len(txt[pic]))):
        print "ERROR " + str(cc) + " " +str(len(txt[pic]))
        for a in range(h):
            for b in range(w):
                P = p_img[b, a]
                if (P[0] + P[1] + P[2] < 400):
                    print 0,
                else:
                    print " ",
            print ""
        break


    for c in range(1,len(txt[pic])):
        x = ord(txt[pic][c-1]) - ord('a')
        y = ord(txt[pic][c]) - ord('a')
        data[x][y][0] += dt[c][0] - dt[c-1][1]
        #data[x][y][1] += dt[c][0] - dt[c-1][1]
        data[x][y][2] += 1

bfile = open('res', 'w')

for i in range(26):
    for j in range(26):
        # if (data[i][j][2] > 0):
        #     data[i][j][0] = data[i][j][0] / data[i][j][2]
        bfile.write(str(data[i][j][0]) + " " + str(data[i][j][1]) + " " + str(data[i][j][2]) + " ")

bfile.close()