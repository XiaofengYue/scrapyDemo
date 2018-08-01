# -*- coding: utf-8 -*-
import scrapy
import time
from selenium import webdriver
from scrapy import FormRequest


class TaobaoSpider(scrapy.Spider):

    def __init__(self):
        self.browser = webdriver.Chrome()
    name = 'flaskBlog'
    allowed_domains = ['www.taobao.com']
    start_urls = ['http://www.pipicat.top/account']

    def start_requests(self):
        self.login()
        yield scrapy.Request(url=self.start_urls[0], cookies=self.cookies, callback=self.parse)

    def login(self):
        self.browser.get('http://www.pipicat.top/login')
        email = self.browser.find_element_by_xpath('//*[@id="email"]')
        email.clear()
        email_str = input('请输入你的账号')
        email.send_keys(email_str)
        psw = self.browser.find_element_by_xpath('//*[@id="password"]')
        psw.clear()
        psw_str = input('请输入你的密码')
        psw.send_keys(psw_str)
        btn = self.browser.find_element_by_xpath('//*[@id="submit"]')
        btn.click()
        time.sleep(2)
        self.cookies = self.browser.get_cookies()
        self.browser.close()

    def parse(self, response):
        print(response.text)
