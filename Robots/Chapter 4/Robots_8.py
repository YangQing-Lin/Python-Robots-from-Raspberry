from selenium import webdriver
driver = webdriver.Firefox(executable_path=r'D:\DATA\Desktop\geckodriver.exe')
# 电脑中geckodriver.exe的位置（python_work文件夹里也放了一个）
driver.get("http://www.santostang.com/2018/07/04/hello-world/")

driver.switch_to.frame(driver.find_element_by_css_selector("iframe[title='livere']"))
comment = driver.find_element_by_css_selector('div.reply-content')
content = comment.find_element_by_tag_name('p')
print(content.text)
