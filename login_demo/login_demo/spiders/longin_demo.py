import scrapy
import json
import re
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from scrapy import FormRequest, Request

# 具体流程
# 先从start_request开始建立请求，request的解析返回的是给login处理
# login填表处理，而后将response和表格一起提交，回调是交给了parse_login
# par_login判断是否登录成功，成功之后，就调用父类的请求，用的是start_urls 和 parse
#


class ExampleLoginSpider(scrapy.Spider):
    name = 'login'

    def __init__(self):
        self.browser = webdriver.Chrome()

    start_urls = ['https://user.qzone.qq.com/']

    def start_requests(self):
        self.login()

    def parse(self, response):
        pass

    def login(self):
        self.browser.get('https://user.qzone.qq.com/')
        # 登录表单在页面的框架中，所以要切换到该框架
        self.browser.switch_to_frame('login_frame')
        self.browser.find_element_by_id('switcher_plogin').click()
        self.browser.find_element_by_id('u').clear()
        qq = input('请输入你的qq号码')
        self.browser.find_element_by_id('u').send_keys(qq)
        psw = input('请输入你的密码')
        self.browser.find_element_by_id('p').send_keys(psw)
        self.browser.find_element_by_id('login_button').click()
        time.sleep(5)
        self.browser.close()


class BlogLoginSpider(scrapy.Spider):
    # 账号密码模拟登录
    name = "loginblog"
    allowed_domains = ["www.pipicat.top"]
    start_urls = ['http://www.pipicat.top/account']
    login_url = 'http://www.pipicat.top/login'

    def parse(self, response):
        print(response.text)

    def start_requests(self):
        print('开始建立请求')
        yield scrapy.Request(self.login_url, callback=self.login)

    def login(self, response):
        print('login处理填表')
        formdata = {
            'email': '736659711@qq.com', 'password': 'wozhiai0'}
        yield FormRequest.from_response(response, formdata=formdata,
                                        callback=self.parse_login)

    def parse_login(self, response):
        # print('>>>>>>>>'+response.text)
        if 'Account' in response.text:
            print('登录成功')
            yield from super().start_requests()
