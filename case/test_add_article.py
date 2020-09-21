from selenium import webdriver
from pages.articleclassify_page import ArticleclassifyPage
import allure
@allure.feature("添加文章分类")
@allure.story("用户故事1")
class Testaddarticle():
    @allure.title("添加文章分类功能用例名称")
    def test_add_article(self,login):

        # 添加文章分类
        article = ArticleclassifyPage(login)
        article.click_articleclassify()
        article.click_add_articleclassify()
        article.input_articleclassify("yoyo233")
        article.save_articleclassify()

        # 断言
        result = article.is_add_success(expect="添加成功")
        assert result