# Python Creeper 入门

Noted by Tianlang 20/11/2024  声明：仅个人学习使用！

*参考教程:Python网络爬虫从入门到实践*

## 编写第一个爬虫程序

编写爬虫程序之前，我们先要掌握基本的Python语法，主要是基本的数据结构，面向对象的基本实例化。

### 第一步：获取页面

```python
#Date in 20/11/2024
import requests
link ="http://www.santostang.com/"
#模拟浏览器做出访问动作
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/237.84.2.178 Safari/537.36"}
r=requests.get(link,headers=headers)
print(r.text)
```

**1>首先定义link为网页目标地址**

**2>headers是伪装请求头的代理**

**3>r是request的Response回复对象**



### 第二步：提取需要的数据

使用Beautifulsoup库对页面进行解析

```python
soup=BeautifulSoup(r.text,"html.parser")#解析文章
#找到第一篇文章标题
#定位:class="post-title"的标签“H1”元素，提取A，提取A里的字符串
title=soup.find("h1",class_="post-title").a.text.strip()
#原理代码:标题超链接格式为<h1,class="post-title">
# <a href "URL"> title</a>
print(title)
```

* 进阶:使用浏览器的审查功能进行功能化解析步骤

* 例如<1>解析文章时先有第一步的获得文本操作，其中`html.parser`进行操作说明    <2>定位目标元素位置，进行标签提取、文本操作<br/>

### 第三步:存储数据

 ```python
#打开一个空白的txt写入
with open("title.txt","w",encoding="utf-8") as f:
    f.write(title)
 ```

打开一个空白的txt写入/创建在与代码相同的目录上 