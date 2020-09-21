from common.base import Base
import allure

class ArticledetailPage(Base):
    #文章列表
    loc_1=("css",'#left-side > ul.well.nav.nav-pills.nav-stacked.nav-sitemenu.hide-sm > li:nth-child(9) > a')
    #增加文章列表
    loc_2=("xpath",'//*[@id="content-block"]/div[1]/div[2]/div/a')
    #标题
    loc_3=("name",'title')
    #文章分类
    loc_4=("xpath",'//*[@id="id_classify_wrap_container"]/div/div[1]')
    #选取下拉框option
    loc_5=("css",'#id_classify_wrap_container > div > div.selectize-dropdown.single.adminselectwidget.form-control > div > div:nth-child(3)')
    #正文
    loc_6=('xpath','//*[@id="id_body"]')
    #备注
    loc_7=('xpath','//*[@id="id_detail"]')
    #保存
    loc_8=('xpath','//*[@id="articledetail_form"]/div[2]/button')
    #获取添加成功
    loc_9=('xpath','//*[@id="content-block"]/div[2]')

    @allure.step("点左侧文章列表")
    #点击文章列表
    def click_Articlelist(self):
        self.click(self.loc_1)
    @allure.step("点增加文章")
    #点击增加文章
    def click_add_article(self):
        self.click(self.loc_2)
    @allure.step("清空文本框")
    #清空文本框
    def cleartitle(self):
        self.clear(self.loc_3)
    @allure.step("输入标题")
    #输入标题
    def input_title(self,text=''):
        self.send(self.loc_3,text)
    @allure.step("点击文章分类选择框")
    #点击文章分类选择框
    def click_selector(self):
        self.click(self.loc_4)
    @allure.step("选择选项")
    #选择选项
    def choose_selector(self):
        self.click(self.loc_5)
    @allure.step("清空正文文本框")
    #清空正文文本框
    def clearzhengwen(self):
        self.clear(self.loc_6)
    @allure.step("输入正文文本")
    #输入正文文本
    def input_zhengwen(self,text=''):
        self.send(self.loc_6,text)
    @allure.step("清空备注文本框")
    #清空备注文本框
    def clearbeizhu(self):
        self.clear(self.loc_7)
    @allure.step("输入备注文本")
    #输入备注文本
    def input_beizhu(self,text=''):
        self.send(self.loc_7,text)
    @allure.step("点击保存")
    #点击保存
    def save(self):
        self.click(self.loc_8)
    def is_add_success(self,expect=''):
        get_result=self.get_text(self.loc_9)
        print("%s"%get_result)
        return expect in get_result

if __name__ == '__main__':
    from selenium import webdriver
    from pages.login_page import LoginPage
    driver=webdriver.Chrome()
    driver.maximize_window()
    web=LoginPage(driver)
    web.login()

    articledetail=ArticledetailPage(driver)
    articledetail.click_Articlelist()
    articledetail.click_add_article()
    articledetail.cleartitle()
    articledetail.input_title(text="标题")
    articledetail.click_selector()
    articledetail.choose_selector()
    articledetail.clearzhengwen()
    articledetail.input_zhengwen(text="随便输入正文")
    articledetail.clearbeizhu()
    articledetail.input_beizhu(text="随便输入备注")
    articledetail.save()
    result=articledetail.is_add_success(expect="添加成功")
    assert result

