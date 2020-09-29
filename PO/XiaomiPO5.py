# 首页
import time
import yaml     #解析5.1版本之后要加Loader=yaml.FullLoader

class BasePage():
    # 将公共方法进行封装继承,保存页面操作的公共方法
    def __init__(self,driver):
        self.driver=driver
        eles = yaml.load(open('../element/xiaomi.yml', encoding='UTF-8').read(), Loader=yaml.FullLoader)[self.__class__.__name__]
        for ele in  eles:
            self.__setattr__(ele,eles[ele])
        #点击元素
    def click(self,*locaor):
        self.driver.find_element(*locaor).click()
    # 输入文本
    def input_text(self,text,*locaor):
        self.driver.find_element(*locaor).send_keys(text)
    # 输入文本并点击
    def input_text_dianji(self,*locaor,text):
        self.driver.find_element(*locaor).send_keys(text+',''\n')
    #切换窗口
    def switch_window(self,tartge_title):
        for handle in self.driver.window_handles:
            self.driver.switch_to.window(handle)
            # 判断切换到目标窗口，判断窗口的标题
            if self.driver.title == tartge_title:
                print("切换到目标窗口")
                return True
    # 获取文本
    def get_text(self,*locaor):
        return self.driver.find_element(*locaor).text

class IndexPage(BasePage):
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
class LoginPage(BasePage):
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
class CommodityPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
    #选择商品
    def xze(self):
        self.click(*self.firtsp)
        time.sleep(1)
        if self.switch_window("小米10至尊纪念版立即购买-小米商城"):
            return ProductPage(self.driver)

#商品详情页
class ProductPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
    #加入购物车
    def add_cat(self):
        time.sleep(1)
        self.click(*self.add)
        return SubmitPage(self.driver)


#提交成功页
class SubmitPage(BasePage):
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
    # from selenium import webdriver
    # driver=webdriver.Chrome()
    # driver.maximize_window()
    # driver.implicitly_wait(10)
    # indexPage=IndexPage(driver)
    # LoginPage=indexPage.To_Login()
    # indexPage=LoginPage.Login()
    # CommodityPage=indexPage.sousshangping()
    # ProductPage=CommodityPage.xze()
    # SubmitPage=ProductPage.add_cat()
    # SubmitPage.Submit()
    # driver.quit()

