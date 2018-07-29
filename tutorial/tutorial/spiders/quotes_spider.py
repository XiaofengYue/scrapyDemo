import scrapy
import re
from tutorial.items import SaikrItem


class SaikrSpider(scrapy.Spider):
    name = "saikr"
    start_urls = [
        'https://www.saikr.com/vs/0/4/1?page=1',
        'https://www.saikr.com/vs/0/4/1?page=2',
        'https://www.saikr.com/vs/0/4/1?page=3',
        'https://www.saikr.com/vs/0/4/1?page=4',
        'https://www.saikr.com/vs/0/4/1?page=5',
        'https://www.saikr.com/vs/0/4/1?page=6',
        'https://www.saikr.com/vs/0/4/1?page=7',
        'https://www.saikr.com/vs/0/4/1?page=8',
        'https://www.saikr.com/vs/0/4/1?page=9',
        'https://www.saikr.com/vs/0/4/1?page=10',
    ]

    def parse(self, response):
        # 爬取一页
        for url in response.css('h3.tit a::attr(href)').extract():
            self.log('url = %s' % url)
            yield scrapy.Request(url, callback=self.parse_url)

    def parse_url(self, response):
        def css_with_extract(query, response=response):
            return response.css(query).extract_first().strip()

        item = SaikrItem()
        item['title'] = css_with_extract('div.sk-event4-1-detail-banner img::attr(alt)')
        item['source_url'] = response.url
        item['image_url'] = css_with_extract('div.sk-event4-1-detail-banner img::attr(src)')
        com_url = response.css('div.sk-event-detail-nav div.fr')
        if com_url.css('a[href^=http]').extract_first() is not None:
            item['com_url'] = css_with_extract('a::attr(href)', com_url)
        else:
            item['com_url'] = ''

        for sidebar in response.css('.sidebar-b-con'):
            if css_with_extract('h3.title::text', sidebar) == '类型':
                item['team_category'] = css_with_extract('span.title-desc::text', sidebar)

            if css_with_extract('h3.title::text', sidebar) == '报名费':
                item['charge'] = css_with_extract('span.title-desc::text', sidebar)

            if css_with_extract('h3.title::text', sidebar) == '级别':
                item['com_level'] = css_with_extract('span.title-desc::text', sidebar)

            if css_with_extract('h3.title::text', sidebar) == '参赛对象':
                item['com_object'] = css_with_extract('span.title-desc::text', sidebar)

            if '报名时间' in css_with_extract('h3.title::text', sidebar):
                timeStr = css_with_extract('div.info-content::text', sidebar)
                timegroup = re.search('(\d.*? \d\d:\d\d).*?(2.*)', timeStr, re.M)
                if timegroup is not None:
                    item['signup_start_date'] = timegroup[1]
                    item['signip_end_date'] = timegroup[2]

            if '比赛时间' in css_with_extract('h3.title::text', sidebar):
                timeStr = css_with_extract('div.info-content::text', sidebar)
                timegroup = re.search('(\d.*? \d\d:\d\d).*?(2.*)', timeStr, re.M)
                if timegroup is not None:
                    item['com_start_date'] = timegroup[1]
                    item['com_end_date'] = timegroup[2]

            if css_with_extract('h3.title::text', sidebar) == '主办方':
                li = sidebar.css('div.info-content::text').extract()
                s = ''
                for i in li:
                    s = s + ' ' + i.strip()
                item['com_orginaziton'] = s

            if css_with_extract('h3.title::text', sidebar) == '竞赛类别':
                str = ''
                for span in sidebar.css('span::text').extract():
                    str = str + ' ' + span.strip()
                item['com_category'] = str

        yield item


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
