import yaml
class BasePage():
    # 将公共方法进行封装继承,保存页面操作的公共方法
    def __init__(self,driver):
        self.driver=driver
        #通过yaml获取元素字典，根据class名字作为key，获取value。通过.__setattr__遍历字典，给到子类使用
        eles = yaml.load(open('../element/xiaomi.yml', encoding='UTF-8').read(), Loader=yaml.FullLoader)[self.__class__.__name__]
        for ele in  eles:
            self.__setattr__(ele,eles[ele])
    #点击元素
    def click(self,*locaor):
        self.driver.find_element(*locaor).click()
    # 输入文本
    def input_text(self,text,*locaor):
        self.driver.find_element(*locaor).send_keys(text)
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
