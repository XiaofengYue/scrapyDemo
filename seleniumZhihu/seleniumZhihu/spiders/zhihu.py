# -*- coding: utf-8 -*-
import scrapy
import time
from selenium import webdriver


class zhihucook(scrapy.Spider):
    name = "zhihu"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36'
    }

    def __init__(self):
        self.browser = webdriver.Chrome()
    start_urls = ['https://www.zhihu.com/people/yue-xiao-feng-75/following/questions']

    def start_requests(self):
        self.login()
        yield scrapy.Request(url=self.start_urls[0], cookies=self.cookies, callback=self.parse, headers=self.headers)

    def login(self):
        self.browser.get('https://www.zhihu.com/signin')
        self.browser.find_element_by_xpath('/html/body/div[1]/div/main/div/div/div/div[2]/div[1]/form/div[1]/div[2]/div[1]/input').clear()

        email = input('请输入你的账号')
        password = input('请输入你的密码')
        self.browser.find_element_by_xpath('/html/body/div[1]/div/main/div/div/div/div[2]/div[1]/form/div[1]/div[2]/div[1]/input').send_keys(email)
        self.browser.find_element_by_xpath('/html/body/div[1]/div/main/div/div/div/div[2]/div[1]/form/div[2]/div/div[1]/input').clear()
        self.browser.find_element_by_xpath('/html/body/div[1]/div/main/div/div/div/div[2]/div[1]/form/div[2]/div/div[1]/input').send_keys(password)
        self.browser.find_element_by_xpath('/html/body/div[1]/div/main/div/div/div/div[2]/div[1]/form/button').click()
        self.cookies = self.browser.get_cookies()
        print('我们的cookie %s ' % self.cookies)
        time.sleep(2)
        self.browser.close()

    def parse(self, response):
        print("登录成功")
        print(response.text)
