import scrapy
from di81.items import Di81Item


class meiziSpider(scrapy.Spider):
    name = "meizi"
    base_url = 'http://di81.com/PicList?typeid=6&pageindex='
    page = 1
    start_urls = [base_url + str(page), ]

    def parse(self, response):
        # http://di81.com/upload//warehouse/6/379.jpg
        # response.css('ul#pins img::attr(src)').extract()
        def get_title():
            for title in response.css('ul#pins img::attr(alt)').extract():
                yield title
        g = get_title()
        for link in response.css('ul#pins img::attr(src)').extract():
            item = Di81Item()
            url = 'http://di81.com/' + link
            tit = next(g)
            item['image_urls'] = [url]
            item['title'] = tit
            yield item

        # if self.page < 10:
        #     self.page += 1
        #     yield scrapy.Request(self.base_url + str(self.page), self.parse)
