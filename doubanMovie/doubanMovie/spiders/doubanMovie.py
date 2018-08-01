import scrapy
from scrapy import FormRequest
from urllib import request
from doubanMovie.items import doubanMovieItem
from PIL import Image


class doubanSpider(scrapy.Spider):
    name = "douban"
    login_url = 'https://www.douban.com/login'
    start_urls = [
        'https://movie.douban.com/top250?start=0&filter=',
        'https://movie.douban.com/top250?start=25&filter=',
        'https://movie.douban.com/top250?start=50&filter=',
        'https://movie.douban.com/top250?start=75&filter=',
        'https://movie.douban.com/top250?start=100&filter=',
        'https://movie.douban.com/top250?start=125&filter=',
        'https://movie.douban.com/top250?start=150&filter=',
        'https://movie.douban.com/top250?start=175&filter=',
        'https://movie.douban.com/top250?start=200&filter=',
        'https://movie.douban.com/top250?start=225&filter='
    ]

    def start_requests(self):
        yield scrapy.Request(self.login_url, callback=self.login)

    def login(self, response):
        email_str = input('请输入你的账号')
        password_str = input('请输入你的密码')
        formdata = {
            'email': email_str,
            'password': password_str
        }
        yield FormRequest.from_response(response, formdata=formdata, callback=self.after)

    def after(self, response):
        print('有没有登录成功呢 ')
        yield from super().start_requests()

    def parse(self, response):
        for movie in response.css('.info .hd a::attr(href)').extract():
            yield scrapy.Request(url=movie, callback=self.movie_parse)

    def movie_parse(self, response):
        item = doubanMovieItem()
        item['title'] = response.xpath('/html/body/div[3]/div[1]/h1/span[1]/text()').extract_first()
        item['rank'] = response.xpath('/html/body/div[3]/div[1]/div[1]/span[1]/text()').extract_first()
        item['year'] = response.xpath('/html/body/div[3]/div[1]/h1/span[2]/text()').extract_first()
        item['score'] = response.xpath('/html/body/div[3]/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/strong/text()').extract_first()
        category = ''
        runtime = ''
        tempStr = ''
        for span in response.css('#info span::text').extract():
            if span == '类型:':
                tempStr = category
            elif span == '制片国家/地区:':
                category = tempStr
            elif span == '片长:':
                tempStr = runtime
            elif span == '又名:':
                runtime = tempStr
            else:
                tempStr += span

        item['category'] = category
        item['runtime'] = runtime
        yield item


class doubanCookie(scrapy.Spider):
    name = "doubanlogin"

    start_urls = ['https://www.douban.com/login']

    def start_requests(self):
        yield scrapy.FormRequest(url=self.start_urls[0], meta={"cookiejar": 1}, callback=self.parse)

    def parse(self, response):
        captcha_id = response.xpath('//input[@name="captcha-id"]/@value').extract_first()
        cap_link = response.xpath('//img[@id="captcha_image"]/@src').extract_first()
        print('验证码链接咯' + cap_link)
        if cap_link is None:
            email_str = input('请输入你的账号')
            password_str = input('请输入你的密码')
            formdata = {
                'form_email': email_str,
                'form_password': password_str
            }
            yield FormRequest.from_response(response, meta={"cookiejar": response.meta["cookiejar"]}, formdata=formdata, callback=self.after)
        else:
            request.urlretrieve(cap_link, '11.jpg')
            email_str = input('请输入你的账号')
            password_str = input('请输入你的密码')
            try:
                im = Image.open('11.jpg')
                im.show()
            except:
                pass
            cap_str = input('请输入验证码')
            formdata = {
                "form_email": email_str,
                "form_password": password_str,
                "captcha-solution": cap_str,
                "captcha-id": captcha_id,
            }
            print("正在登录")
            yield scrapy.FormRequest.from_response(response, meta={"cookiejar": response.meta["cookiejar"]}, formdata=formdata, callback=self.after)

    def after(self, response):
        account = response.xpath('//a[@class="bn-more"]/span/text()').extract_first()
        if account is None:
            print('登录失败')
        else:
            print('登录成功')
        yield scrapy.Request(url='https://www.douban.com/people/121600284/', meta={"cookiejar": response.meta["cookiejar"]}, callback=self.person)

    def person(self, response):
        print(response.text)
