from requests import *
import time

headers = {
        'Referer': 'https://space.bilibili.com/19658621/fans/fans',
        'Sec-Fetch-Mode': 'no-cors',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'
    }


# 根据url获取content
def get_by_url(url):
    res = get(url, headers=headers).content.decode()
    return res


# 获取粉丝数
def get_followers(mid, pn, ps):
    url_following = 'https://api.bilibili.com/x/relation/followers?vmid=' + mid + '&pn=' + pn + '&ps=' + ps + '&order=desc&jsonp=jsonp&callback=__jp23'
    res = get_by_url(url_following)
    json_string = res
    total = json_string.find('"total":', 7000)
    re_version = json_string.find('"re_version":', 7000)
    json_string = "粉丝数:" + json_string[total + 8:-3] + "  访问量:" + json_string[re_version + 13:total - 1]
    return json_string


def format_string(r):
    timetuple = time.localtime(time.time())  # 当前时间戳
    fmt = '%Y-%m-%d %a %H:%M:%S'  # 格式化时间
    temp = '[' + time.strftime(fmt, timetuple) + '] ' + r  # 把传入的元组按照格式，输出字符串
    return temp


# main
Str = format_string(get_followers('19658621', '1', '20'))
print(Str)
File = open('D:/Project/数据库/frank粉丝数据.txt', 'a')
File.write('\n' + Str)
File.close()
