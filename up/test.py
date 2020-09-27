import time

from selenium import webdriver
i="小米10"
driver = webdriver.Chrome()
driver.get("https://www.mi.com/index.html")
driver.find_element_by_css_selector(".search-text").send_keys(i)
time.sleep(0.5)
driver.find_element_by_css_selector("[type='submit']").click()
replytext=[]
t = driver.find_elements_by_css_selector(".goods-list .title")
for j in t:
    replytext.append(j.text)
print(replytext)
assert i in replytext
driver.quit()
