# -*- coding: utf-8 -*-

import os
from PIL import Image

# files = os.popen('ls | grep 萌宠 |  grep -v json | sed "s:^:`pwd`/:"')
play = Image.open(('../play.png'))
play = play.convert('RGBA')
play = play.resize((150, 150))
# failed = []
#
# for file in files:
#     file = file.replace('\n', '')
#     imgs = os.listdir(file)
#     for im in imgs:
#         print 'work on ' + file + '/' + im
#         img
#         try:
#             img = Image.open(file + '/' + im)
#         except Exception as e:
#             print 'failed: ' + e
#             failed.append(file + '/' + im)
#         diff = img.size[0] - img.size[1]
#         p1 = (0, diff / -2) if diff <= 0 else (diff / 2, 0)
#         p2 = tuple(a + b for a, b in zip((min(img.size),) * 2, p1))
#         img = img.crop(p1 + p2)
#         img = img.convert('RGBA')
#         area = tuple(a + b for a, b in zip((((img.size[0] - play.size[0]) / 2),) * 4, (0, 0) + play.size))
#         img.paste(play, area, play)
#         img.save('./static/' + im[:-4] + '.png')
# print 'failed files: ' + str(len(failed))
# print failed

img = Image.open('../test.gif')
diff = img.size[0] - img.size[1] * 5 / 4
p1 = (0, diff * 2 / -5) if diff <= 0 else (diff / 2, 0)
p2 = (img.size[0], diff * 2 / -5 + img.size[1] * 4 / 5) if diff <= 0 else (diff / 2 + img.size[1] * 5 / 4, img.size[1])
img = img.crop(p1 + p2)
img = img.convert('RGBA')
img = img.resize((500, 400))
area = ((175, 125, 325, 275))
img.paste(play, area, play)
img.show()
img.save('./check.png')
