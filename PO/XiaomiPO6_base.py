# 首页
import time
import yaml     #解析5.1版本之后要加Loader=yaml.FullLoader
from PO import BasePage

class IndexPage(BasePage.BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get("https://www.mi.com/index.html")

    def To_Login(self):
        self.click(*self.denglu) # 点击登录按钮
        time.sleep(0.5)
        self.click(*self.tongyi)
        return LoginPage(self.driver)
    #搜索商品
    def sousshangping(self):
        self.input_text("小米10\n",*self.search)
        time.sleep(0.5)
        return CommodityPage(self.driver)
#登录页
class LoginPage(BasePage.BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        #登录操作
    def Login(self):
        time.sleep(1)
        self.input_text('17679296697',*self.uaer)
        self.input_text('z741612870',*self.pawd)
        self.click(*self.login)
        time.sleep(0.5)
        return IndexPage(self.driver)


#选择商品页
class CommodityPage(BasePage.BasePage):
    def __init__(self, driver):
        super().__init__(driver)
    #选择商品
    def xze(self):
        self.click(*self.firtsp)
        time.sleep(1)
        if self.switch_window("小米10至尊纪念版立即购买-小米商城"):
            return ProductPage(self.driver)

#商品详情页
class ProductPage(BasePage.BasePage):
    def __init__(self, driver):
        super().__init__(driver)
    #加入购物车
    def add_cat(self):
        time.sleep(1)
        self.click(*self.add)
        return SubmitPage(self.driver)


#提交成功页
class SubmitPage(BasePage.BasePage):
    def __init__(self, driver):
        super().__init__(driver)
    #判断提交成功
    def Submit(self):
        d = self.get_text(*self.su)
        print(d)
        assert "成功" in d

if __name__ == '__main__':
    #首页-进入登录-登录-首页-搜索商品-商品列表-选择商品-商品详情-添加购物车-判断是否成功
    from selenium import webdriver
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    IndexPage(driver).To_Login().Login().sousshangping().xze().add_cat().Submit()
    driver.quit()


