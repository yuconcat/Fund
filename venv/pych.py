# -*- coding = utf-8 -*-
# @Time : 2021/4/21 22:06
# @Author : xxx
# @File : pych.py
# @Software : PyCharm
import re
import requests

from bs4 import BeautifulSoup
from tqdm import trange
import time
#头部伪装
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
}
url = "http://m.qidian.com/book/showbook.aspx?bookid=1209977"
req = requests.get(url,headers=headers)
req.encoding = 'utf-8'
html = req.text
data = BeautifulSoup(html,"html.parser")
req.encoding = 'utf-8'
section_name = data.title.string
print(section_name)