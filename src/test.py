#Date in 20/11/2024
import requests
from bs4 import BeautifulSoup

link ="http://www.santostang.com/"
#模拟浏览器做出访问动作
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/237.84.2.178 Safari/537.36"}
r=requests.get(link,headers=headers)
#print(r.text)

soup=BeautifulSoup(r.text,"html.parser")#解析文章
#找到第一篇文章标题
#定位:class="post-title"的标签“H1”元素，提取A，提取A里的字符串
title=soup.find("h1",class_="post-title").a.text.strip()
#原理代码:标题超链接格式为<h1,class="post-title">
# <a href "URL"> title</a>
print(title)

#打开一个空白的txt写入
with open("title.txt","w",encoding="utf-8") as f:
    f.write(title)