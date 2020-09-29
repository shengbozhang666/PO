from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
driver = webdriver.Chrome()
driver.get("https://www.mi.com/index.html")
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element_by_css_selector("#J_siteUserInfo>a:nth-child(1)").click() #点击登录按钮
time.sleep(0.5)
btn=driver.find_elements_by_css_selector(".btn-primary").click()
if btn:
    btn[0].click()
driver.find_element_by_id("username").send_keys('17679296697')
driver.find_element_by_id("pwd").send_keys('z741612870')
driver.find_element_by_id("login-button").click()
time.sleep(0.5)
driver.find_element_by_id("search").send_keys("小米10\n")
time.sleep(0.5)
driver.find_element_by_css_selector(".goods-list-box > div > div:nth-child(1) > h2").click()
time.sleep(1)
#切换到手机窗口
for handle in driver.window_handles:
    driver.switch_to.window(handle)
    #判断切换到目标窗口，判断窗口的标题
    if driver.title=="小米10至尊纪念版立即购买-小米商城":
        print("切换到目标窗口")
        break

# driver.window.scrollBy(0,2000)
time.sleep(1)

driver.find_element_by_css_selector(".btn-box >div a").click()

d=driver.find_element_by_css_selector(".goods-info>h3").text
print(d)
assert "成功" in d
driver.quit()

