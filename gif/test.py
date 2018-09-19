# -*- coding: utf-8 -*-

import os
from PIL import Image

# files = os.popen('ls | grep 萌宠 |  grep -v json | sed "s:^:`pwd`/:"')
play = Image.open(('../test.gif'))
play = play.convert('RGBA')
play = play.resize((150, 150))

img = Image.open('../test.gif')
img.save('./check.gif')
