import requests
from bs4 import BeautifulSoup # 从bs4这个库中导入BeautifulSoup

link = "http://www.santostang.com/"
headers = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
r = requests.get(link, headers= headers)

soup = BeautifulSoup(r.text, "html.parser") # 使用BeautifulSoup解析  html.parser：网页解析器

# 找到第一篇文章标题，定位到class是“post-title”的h1元素，提取a，提取a里面的字符串，strip()去除左右空格
title = soup.find("h1", class_="post-title").a.text.strip()
print(title)

# 打开一个空白的txt，然后使用f.write写入刚刚的字符串title
with open('../title_test.txt', "a+") as f:
    f.write(title + "\n")