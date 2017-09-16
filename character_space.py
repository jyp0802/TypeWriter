#-*- coding: utf-8 -*-

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
    prev_file = open('res', 'r')
    prev_data = prev_file.read();
    prev_data = prev_data.split();
    data = []
    for i in range(26):
        data.append([])
        for j in range(26):
            data[i].append([int(prev_data[(3*j)+(3*26*i)]),int(prev_data[(3*j)+(3*26*i)+1]),int(prev_data[(3*j)+(3*26*i)+2])])
    prev_file.close()
else:
    data = []  # [hor dist, ver dist, cnt]
    for i in range(26):
        data.append([])
        for j in range(26):
            data[i].append([0, 0, 0])

for pic in range(len(txt)):
    path = "./input_data/in" + str(pic + 1) + ".png"
    img = Image.open(path)
    w, h = img.size

    p_img = img.load()

    char_cnt = 0
    on_letter = False
    exist_black = False

    letter_data = [] #[hor start, hor end, ver start, ver end]
    for j in range(len(txt[pic])):
        letter_data.append([0,0,0,0])

    for i in range(w):
        exist_black = False
        for j in range(h):
            P = p_img[i,j]
            if (P[0]+P[1]+P[2]<400):
                if (not on_letter):
                    on_letter = True
                    letter_data[char_cnt][0] = i
                    letter_data[char_cnt][2] = j
                    letter_data[char_cnt][3] = j
                exist_black = True
                if (j > letter_data[char_cnt][2]):
                    letter_data[char_cnt][2] = j
                elif (j < letter_data[char_cnt][3]):
                    letter_data[char_cnt][3] = j
            elif ((j == h-1) and (not exist_black) and on_letter):
                on_letter = False
                letter_data[char_cnt][1] = i-1
                char_cnt += 1


    for c in range(1,len(txt[pic])):
        x = ord(txt[pic][c-1]) - ord('a')
        y = ord(txt[pic][c]) - ord('a')
        data[x][y][0] += letter_data[c][0] - letter_data[c-1][1]
        #data[x][y][1] += letter_data[c][0] - letter_data[c-1][1]
        data[x][y][2] += 1

result_file = open('res', 'w')

for i in range(26):
    for j in range(26):
        result_file.write(str(data[i][j][0]) + " " + str(data[i][j][1]) + " " + str(data[i][j][2]) + " ")

result_file.close()