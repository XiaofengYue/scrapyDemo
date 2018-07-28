import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').extract_first(),
                'author': quote.css('small.author::text').extract_first(),
                'tags': quote.css('div.tags a.tag::text').extract(),
            }

        # # Version-1
        # next_page = response.css('li.next a::attr(href)').extract_first()
        # if next_page is not None:
        #     next_page = response.urljoin(next_page)
        #     yield scrapy.Request(next_page, callback=self.parse)

        # # Version-2
        # for href in response.css('li.next a::attr(href)'):
        #   yield response.follow(href, callback=self.parse)

        # Version-3
        for a in response.css('li.next a'):
            yield response.follow(a, callback=self.parse)


# 蜘蛛会筛选重复的网页
class AuthorSpider(scrapy.Spider):
    name = 'author'

    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        # follow links to author pages
        for href in response.css('.author + a::attr(href)').extract():
            yield response.follow(href, self.parse_author)

        # follow pagination links
        for href in response.css('li.next a::attr(href)'):
            yield response.follow(href, self.parse)

    def parse_author(self, response):
        def extract_with_css(query):
            return response.css(query).extract_first().strip()

        yield {
            'name': extract_with_css('h3.author-title::text'),
            'birthdate': extract_with_css('.author-born-date::text'),
            'bio': extract_with_css('.author-description::text'),
        }

# 爬取赛氪上的资料


class saikrSpider(scrapy.Spider):
    name = 'saikr_contury'
    start_urls = ['https://www.saikr.com/vs/0/4/1/']

    # 爬取一页每条的数据
    def parse(self, response):
        for detail_url in response.css('div.event4-1-detail-box a::attr(href)').extract():
            self.log('detail_url: %s' % detail_url)
            yield scrapy.Request(detail_url, self.parser_detail)

    def parser_detail(self, response):
        # 工具
        def extract_with_css(query, response=response):
            return response.css(query).extract_first().strip()

        l = response.css('span.title-desc::text').extract()

        s = response.css('li.new-event4-1-info-item')

        yield{
            # 图片地址
            'image_url': extract_with_css('div.sk-event4-1-detail-banner img::attr(src)'),
            # 标题
            'title': extract_with_css('div.sk-event4-1-detail-banner img::attr(alt)'),
            # 内容
            # 'content':extract_with_css('div.event4-1-detail-text-box')
            # 发布者
            'publisher': extract_with_css('div.event-user-list-box dd.item-desc::text'),
            #
            # 观看量
            'watch': l[0].strip(),
            # 种类
            'team_category': l[1].strip(),
            # 费用
            'charge': l[2].strip(),
            # 级别
            'level': l[3].strip(),
            # 参赛对象
            'object': l[4].strip(),
            # 举办者
            'organizationer': extract_with_css('div.info-content::text', response=s[0]),
            # 报名时间
            'apply_time': extract_with_css('div.info-content::text', response=s[1]),
            # 开始时间
            'competitiontime': extract_with_css('div.info-content::text', response=s[2]),
            # 比赛类别
            'com_category': extract_with_css('div.info-content span::text', response=s[3]),
        }
