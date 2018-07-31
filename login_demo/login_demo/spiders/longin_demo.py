import scrapy
import json
from scrapy import FormRequest, Request

# 具体流程
# 先从start_request开始建立请求，request的解析返回的是给login处理
# login填表处理，而后将response和表格一起提交，回调是交给了parse_login
# par_login判断是否登录成功，成功之后，就调用父类的请求，用的是start_urls 和 parse
#


class ExampleLoginSpider(scrapy.Spider):

    # #账号密码模拟登录
    # name = "login_"
    # allowed_domains = ["www.pipicat.top"]
    # start_urls = ['http://www.pipicat.top/account']
    # login_url = 'http://www.pipicat.top/login'

    # def parse(self, response):
    #     print(response.text)

    # def start_requests(self):
    #     print('开始建立请求')
    #     yield scrapy.Request(self.login_url, callback=self.login)

    # def login(self, response):
    #     print('login处理填表')
    #     formdata = {
    #         'email': '736659711@qq.com', 'password': 'wozhiai0'}
    #     yield FormRequest.from_response(response, formdata=formdata,
    #                                     callback=self.parse_login)

    # def parse_login(self, response):
    #     # print('>>>>>>>>'+response.text)
    #     if 'Account' in response.text:
    #         print('登录成功')
    #         yield from super().start_requests()

    name = "cook_"
    allowed_domains = ['user.qzone.qq.com']
    start_urls = ["https://user.qzone.qq.com/proxy/domain/m.qzone.qq.com/cgi-bin/new/get_msgb?uin=736659711&hostUin=760712977&num=10&start=10&hostword=0&essence=1&r=0.23593002637621185&iNotice=0&inCharset=utf-8&outCharset=utf-8&format=jsonp&ref=qzone&g_tk=1529261733&qzonetoken=89da150f90603fca240ecf617a2a5b52f4d34291df47f3da9dbdcc68fc7fa5d23eb006688324153751b2&g_tk=1529261733"]
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
    }
    # 获取cookie
    cook = {
        'cookie': '736659711_todaycount=0; 736659711_totalcount=128896; zzpaneluin=; zzpanelkey=; pgv_pvi=1478516736; pgv_si=s9108037632; pgv_pvid=6428897214; pgv_info=ssid=s4140346560; ptui_loginuin=736659711; pt2gguin=o0736659711; RK=zDy0b0YlZW; ptcz=430719143c2779f5f38397340e98de2ef075886dbe4cd933550bd0c6379c5013; __Q_w_s_hat_seed=1; midas_openid=736659711; midas_openkey=@bSZcMRtkp; __Q_w_s__QZN_TodoMsgCnt=1; rv2=80E532AF95AFF5A314263064B8C151CC21D672A2501A412B33; property20=D2799CB63FE025771222B7DD429E1C3FC3786BDB37880BB889DE1D8309586BFE90D26D13892733F1; Loading=Yes; ptisp=cm; qz_screen=1280x800; QZ_FE_WEBP_SUPPORT=1; 736659711_todaycount=0; 736659711_totalcount=128896; uin=o0736659711; skey=@Mt5Uw79ri; p_uin=o0736659711; cpu_performance_v8=1; pt4_token=atral3Of0iH8S4kc2SiBzsUmwYBmGu13J7s7DQZ7jZc_; p_skey=V1uD8I8ts88U9bxzwcI6kUm17-DHVFk9c6m8RmqN4WA_'
    }
    # 获取g_tk

    def get_g_tk(cookie):
    hashes = 5381
    for letter in cookie['p_skey']:
        hashes += (hashes << 5) + ord(letter)  # ord()是用来返回字符的ascii码
    return hashes & 0x7fffffff

    def start_requests(self):
        yield scrapy.Request('https://user.qzone.qq.com', cookies=self.cook,
                             callback=self.after, headers=self.headers)

    def after(self, response):
        print("登录成功")
        yield from super().start_requests()

    def parse(self, response):
        print("进入空间成功？")
        print(response.text)
