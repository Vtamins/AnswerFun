# -*- coding:utf-8 -*-

from PIL import ImageGrab
from aip import AipOcr
import subprocess
import urllib

""" 你的 百度文字识别 APPID AK SK """
APP_ID = ''
API_KEY = ''
SECRET_KEY = ''
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

# 截屏
bbox =(52,337,640,481)
im = ImageGrab.grab(bbox)
im.save("./test.png",'png')
image = get_file_content('/Users/liruopeng/PycharmProjects/TopShowCheater/test.png')
result = client.basicGeneral(image)
problem = u''
for word in result[u'words_result']:
    problem += word[u'words']
problems = problem.split(".")
print problems
if len(problems) == 1:
    while problem[0] in '0123456789':
        problem = problem[1:]
else:
     problem = problems[1]
print problem.encode('utf8')
subprocess.call(["open","https://www.baidu.com/s?wd="+urllib.quote(problem.encode('utf-8')) ])