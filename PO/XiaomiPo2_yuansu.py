#将元素以对象属性保存，元素定位方法

# 首页
import time
from selenium.webdriver.common import by


class IndexPage():
    def __init__(self,driver):
        self.driver=driver
        self.driver.get("https://www.mi.com/index.html")
        #设置页面元素变量
        self.denglu=["css selector","#J_siteUserInfo>a:nth-child(1)"] #登录按钮
        self.tongyi=["css selector",".btn-primary"] # 同意弹出
        self.search=["id","search"]  #搜索
    #进入登录页
    def To_Login(self):
            self.driver.find_element(*self.denglu).click()  # 点击登录按钮
            time.sleep(0.5)
            self.driver.find_element(*self.tongyi).click()
            return LoginPage(self.driver)
    #搜索商品
    def sousshangping(self):
        self.driver.find_element(*self.search).send_keys("小米10\n")
        time.sleep(0.5)
        return CommodityPage(self.driver)
#登录页
class LoginPage():
    def __init__(self,driver):
        self.driver=driver
        self.uaer=['id','username']
        self.pawd=['id','pwd']
        self.login=['id','login-button']
        #登录操作
    def Login(self):
        time.sleep(1)
        self.driver.find_element(*self.uaer).send_keys('17679296697')
        self.driver.find_element(*self.pawd).send_keys('z741612870')
        self.driver.find_element(*self.login).click()
        time.sleep(0.5)
        return IndexPage(self.driver)


#选择商品页
class CommodityPage():
    def __init__(self, driver):
        self.driver = driver
        self.firtsp=['css selector','.goods-list-box > div > div:nth-child(1) > h2']
    #选择商品
    def xze(self):
        self.driver.find_element(*self.firtsp).click()
        time.sleep(1)
        for handle in self.driver.window_handles:
            self.driver.switch_to.window(handle)
            # 判断切换到目标窗口，判断窗口的标题
            if self.driver.title == "小米10至尊纪念版立即购买-小米商城":
                print("切换到目标窗口")
                return ProductPage(self.driver)

#商品详情页
class ProductPage():
    def __init__(self, driver):
        self.driver = driver
        self.add=['css selector','.btn-box >div a']
    #加入购物车
    def add_cat(self):
        time.sleep(1)
        self.driver.find_element(*self.add).click()
        return SubmitPage(self.driver)


#提交成功页
class SubmitPage():
    def __init__(self, driver):
        self.driver = driver
        self.su=['css selector','.goods-info>h3']
    #判断提交成功
    def Submit(self):
        d = self.driver.find_element(*self.su).text
        print(d)
        assert "成功" in d

if __name__ == '__main__':
    #首页-进入登录-登录-首页-搜索商品-商品列表-选择商品-商品详情-添加购物车-判断是否成功
    from selenium import webdriver
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    indexPage=IndexPage(driver)
    LoginPage=indexPage.To_Login()
    indexPage=LoginPage.Login()
    CommodityPage=indexPage.sousshangping()
    ProductPage=CommodityPage.xze()
    SubmitPage=ProductPage.add_cat()
    SubmitPage.Submit()
    driver.quit()