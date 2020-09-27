import time

from selenium import webdriver
i="小米10至尊纪念版"
driver = webdriver.Chrome()
driver.get("https://www.mi.com/index.html")
driver.find_element_by_css_selector(".search-text").send_keys(i)
driver.find_element_by_css_selector("[type='submit']").click()
time.sleep(1)
t=driver.find_element_by_css_selector(" div:nth-child(1) > h2").text
print(t)
if i in t:
    print('搜索成功')
else:
    print('搜索失败')
driver.quit()