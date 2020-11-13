from selenium import webdriver
driver = webdriver.Firefox(executable_path=r'D:\DATA\Desktop\geckodriver.exe')
# 电脑中geckodriver.exe的位置（python_work文件夹里也放了一个）
driver.get("http://www.santostang.com/2018/07/04/hello-world/")
