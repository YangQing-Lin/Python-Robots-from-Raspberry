import requests
import re
import os

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0'
}
url = 'https://www.14sxsx.com/pic/689716_7.html'
response = requests.get(url, headers=header)
response.encoding = 'utf-8'
html = response.text
print(html)
dir_name = re.findall('<h1>(.*?)</h1>', html)[-1]
dir_name = dir_name.split("</ a>")[-1]
if not os.path.exists(dir_name):
    os.makedirs(dir_name)
    urls = re.findall('< img .*? data-original=(.*?)>', html)
for picurl in urls:
    file_name = picurl.split('/')[-1]
    picurl = picurl.split('"')[1]
    res = requests.get(picurl, headers=header)
    f = open(dir_name + '/' + file_name, 'wb')
    f.write(res.content)
