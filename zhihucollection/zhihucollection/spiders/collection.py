import scrapy
from scrapy import FormRequest


class ZhihuCollectionSpider(scrapy.Spider):
    name = 'collection'

    def start_requests(self):
        yield scrapy.FormRequest(url='https://www.zhihu.com/signin', meta={'cookiejar': 1}, callback=self.login_before)

    def login_before(self, response):
        u_str = input('请输入您的账号')
        p_str = input('请输入您的密码')
        formdata = {
            'username': u_str,
            'password': p_str,
        }
        print('正在登录')
        yield FormRequest.from_response(response, meta={'cookiejar': response.meta['cookiejar']}, formdata=formdata, callback=self.login_after)

    def login_after(self, response):
        print(response.text)
        yield scrapy.Request('https://www.zhihu.com/collections', meta={'cookiejar': response.meta['cookiejar']}, callback=self.parse)

    def parse(self, response):
        print(response.text)
