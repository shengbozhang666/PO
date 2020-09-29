import yaml
class BasePage():
    # 将公共方法进行封装继承,保存页面操作的公共方法
    def __init__(self,driver):
        self.driver=driver
        eles = yaml.load(open('xiaomi.yml', encoding='UTF-8').read(), Loader=yaml.FullLoader)[self.__class__.__name__]
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