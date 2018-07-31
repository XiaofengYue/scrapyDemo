# -*- coding: utf-8 -*-
import scrapy
import time
from selenium import webdriver


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
        email.send_keys('736659711@qq.com')
        psw = self.browser.find_element_by_xpath('//*[@id="password"]')
        psw.clear()
        psw.send_keys('wozhiai0')
        btn = self.browser.find_element_by_xpath('//*[@id="submit"]')
        btn.click()
        time.sleep(2)
        self.cookies = self.browser.get_cookies()
        self.browser.close()

    def parse(self, response):
        print(response.text)
