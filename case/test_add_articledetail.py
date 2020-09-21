from selenium import webdriver
from pages.articledetail_page import ArticledetailPage
import allure
@allure.feature("添加文章列表")
@allure.story("用户故事2")
class Testaddarticle():
    @allure.title("添加文章列表功能用例名称")
    def test_add_articledetail(self,login):
        driver=login
        articledetail = ArticledetailPage(driver)
        with allure.step("step1:点击文章列表"):
            articledetail.click_Articlelist()
        with allure.step("step2:点击文章列表按钮"):
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
        result = articledetail.is_add_success(expect="添加成功")
        assert result
