# 抓取多页评论
import requests
import json
# 获取 json 的 string


def single_page_comment(link):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}
    r = requests.get(link, headers=headers)
    json_string = r.text
    json_string = json_string[json_string.find('{'):-2]
    # 从第一个左大括号提取，最后的两个字符-括号和分号不取
    json_data = json.loads(json_string)
    comment_list = json_data['results']['parents']
    for eachone in comment_list:
        message = eachone['content']
        print(message)


for page in range(1, 4):
    link1 = "https://api-zero.livere.com/v1/comments/list?callback=jQuery11240373649123312193_1589628623958&limit=10&offset="
    link2 = "&repSeq=4272904&requestPath=%2Fv1%2Fcomments%2Flist&consumerSeq=1020&livereSeq=28583&smartloginSeq=5154&code=&_=1589628623960"
    page_str = str(page)
    link = link1 + page_str + link2
    print(link)
    single_page_comment(link)
    # single_page_comment()是个自定义函数
