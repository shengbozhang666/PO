import os

import pytest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
def setup_module():
    #测试之前的环境准备
    global driver
    driver = webdriver.Chrome()
    driver.get("https://www.mi.com/index.html")
    # driver.maximize_window()

def teardowm_module():
    #测试之后清除环境
    global driver
    driver.quit()

def test_shouye():
    global driver
    qianzhi = ['小米10至尊纪念版', '小米10 Pro', '小米10', '小米10 青春版 5G', '小米MIX Alpha']
    mouse=driver.find_element_by_xpath("//*[@id='app']/div[1]/div/div[3]/div[1]/div[2]/ul/li[2]")
    ActionChains(driver).move_to_element(mouse).perform()
    time.sleep(2)
    i=1
    j=[]
    for i in range(5):
        i+=1
        f=driver.find_element_by_xpath("//*[@id='J_navMenu']/div/ul/li["+str(i)+"]/a/div[2]").text
        j.append(f)
    print(j)
    if qianzhi == j:
        print("成功")
    else:
        print("错误")

def test_radmi():
    global driver
    print("执行第二个用例")



if __name__ == '__main__':
    pytest.main(['xiaomi.py','-s','--alluredir=tmp/my_allure_results'])
    os.system("allure serve C:\\Users\\ASUS\\PycharmProjects\\TEST_0\\up\\tmp\\my_allure_results")

