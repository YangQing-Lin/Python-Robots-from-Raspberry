import time
TimeTuple = time.localtime(time.time())  # 当前时间戳
print('当前时间戳：', TimeTuple)

fmt = '%Y-%m-%d %a %H:%M:%S'  # 格式化时间
test = time.strftime(fmt, TimeTuple)  # 把传入的元组按照格式，输出字符串
print('获取当前的时间(字符串)：[', test, ']')
temp = '[' + test + ']'
print(temp)
