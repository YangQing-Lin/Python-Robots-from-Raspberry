import requests


def get_movies():
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/'
                      '537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
        'Host': 'movie.douban.com'
    }
    for i in range(0, 10):
        link = 'https://movie.douban.com/top250?start=' + str(i * 25)
        r = requests.get(link, headers=headers, timeoput=10)
        print(str(i+1), "页响应状态码：", r.status_code)
        print(r.text)


get_movies()
