import os

import pytest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
qianzhi = ['小米10至尊纪念版', '小米10 Pro', '小米10', '小米10 青春版 5G', '小米MIX Alpha']
def setup_module():
    #测试之前的环境准备
    global driver
    driver = webdriver.Chrome()
    driver.get("https://www.mi.com/index.html")
    driver.maximize_window()



def test_shouye():
    global driver

    mouse=driver.find_element_by_xpath("//*[@id='app']/div[1]/div/div[3]/div[1]/div[2]/ul/li[2]")
    ActionChains(driver).move_to_element(mouse).perform()
    time.sleep(2)
    i=1
    j=[]
    for i in range(5):
        i+=1
        f=driver.find_element_by_xpath("//*[@id='J_navMenu']/div/ul/li["+str(i)+"]/a/div[2]").text
        time.sleep(0.5)
        # j.append(f)
    print(j)
    if qianzhi == j:
        print("成功")
    else:
        print("错误")
    time.sleep(0.7)


def test_radmi():
    global driver
    for i in qianzhi:
        driver.find_element_by_css_selector(".search-text").send_keys(i)
        time.sleep(0.5)
        driver.find_element_by_css_selector("[type='submit']").click()
        time.sleep(1)
        t=driver.find_element_by_css_selector(" div:nth-child(1) > h2").text
        time.sleep(0.5)
        driver.find_element_by_css_selector(".search-text").clear()
        # print(t, i)
        if i in t:
            print('搜索成功')
        else:
            print('搜索失败')

    driver.quit()


# def teardowm_module():
#     #测试之后清除环境
#     global driver


if __name__ == '__main__':
    pytest.main(['xiaomi.py','-s','--alluredir=tmp/my_allure_results'])
    os.system("allure serve C:\\Users\\ASUS\\PycharmProjects\\TEST_0\\up\\tmp\\my_allure_results")

