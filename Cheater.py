# -*- coding:utf-8 -*-
import subprocess
import urllib

from PIL import ImageGrab
from aip import AipOcr


""" 你的 百度文字识别 APPID AK SK """
APP_ID = '10685137'
API_KEY = 'P0djNf97VhhhCGPmDBgDffyO'
SECRET_KEY = 'boz0UYdkDCYeiGxVDxTG60GgtDSiYhNa'
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

# 截屏
bbox =(52,337,640,481)  # 设置 x0 y0 x1 y1
im = ImageGrab.grab(bbox)
im.save("./test.png",'png') # 设置的图片路径

""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()
image = get_file_content('./test.png')
result = client.basicGeneral(image)
problem = u''
for word in result[u'words_result']:
    problem += word[u'words']
problems = problem.split(".")
print problems
if len(problems) == 1:
    while problem[0] in '0123456789': # 去除识别结果的问题编号，否则会影响搜索结果
        problem = problem[1:]
else:
     problem = problems[1]
print problem.encode('utf8')
subprocess.call(["open","https://www.baidu.com/s?wd="+urllib.quote(problem.encode('utf-8')) ])


