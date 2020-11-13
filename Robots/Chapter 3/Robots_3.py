# import requests
# key_dict = {'key1': 'value1', 'key2': 'value2'}
# r = requests.get('http://httpbin.org/get', params=key_dict)
# print('URL 已经正确编码：', r.url)
# print("字符串方式的响应体：\n", r.text)


import requests
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
    'Host': 'www.santostang.com'
}
r = requests.get('http://www.santostang.com', headers=headers)
print('响应状态码：', r.status_code)


# 体验超时抛出异常
# import requests
# link = "http://www.santostang.com"
# r = requests.get(link, timeout=3)
