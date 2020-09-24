from selenium import webdriver
from time import sleep
class MyTestCase(object):

    def test_002(self):
        driver=webdriver.Chrome()
        driver.maximize_window()
        # driver.implicitly_wait(30)
        driver.get("http://dzqytest.cscec1b.net:8071/#/login")
        driver.find_element_by_xpath("/html/body/div[1]/div[1]/ul/div/a[2]").click()
        driver.find_element_by_xpath("/html/body/div[1]/div[1]/ul/li[1]/label/input").send_keys("liuqianghua@cscec.com")
        driver.find_element_by_xpath("/html/body/div[1]/div[1]/ul/li[2]/label/input").send_keys("csCec1b.net")
        driver.find_element_by_xpath("/html/body/div[1]/div[1]/a[2]").click()
        driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/a").click()


a=MyTestCase()
a.test_002()