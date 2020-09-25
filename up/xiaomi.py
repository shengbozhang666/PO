from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
class huoqu(object):
    def shouye(self):
        qianzhi = ["小米10尊纪念版", "小米10 Pro", "小米10", "小米10 青春版 5G", "小米MIX Alpha", ]
        self.driver=webdriver.Chrome()
        self.driver.get("https://www.mi.com/index.html")
        mouse=self.driver.find_element_by_xpath("//*[@id='app']/div[1]/div/div[3]/div[1]/div[2]/ul/li[2]")
        ActionChains(self.driver).move_to_element(mouse).perform()
        time.sleep(1)
        i=1
        j=[]
        for i in range(5):
            i+=1
            f=self.driver.find_element_by_xpath("//*[@id='J_navMenu']/div/ul/li["+str(i)+"]/a/div[2]").text
            j.append(f)
        print(j)
        if qianzhi == j:
            print("成功")
        else:print("错误")
        time.sleep(10)


c=huoqu()
c.shouye()