import pytest as pytest
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
        sleep(2)
        driver.find_element_by_css_selector(".fa-icon-document").click()
        driver.find_element_by_xpath("/html/body/div[1]/div[4]/div[1]/div[2]/div[2]/div/table/tbody/tr[7]/td[7]/a[1]").click()
        sleep(10)

if __name__ == '__main__':
    pytest.main(['test001.py','-s'])