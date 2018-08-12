import scrapy
from bookPDF.items import BookpdfItem


class PDFSpider(scrapy.Spider):
    name = 'pdf'

    start_urls = ['http://pages.cs.wisc.edu/~remzi/OSTEP/']

    def parse(self, response):

        trs = response.css('tr td')

        for link in trs:
            title = str(link.css('small::text').extract_first()).strip()
            if title.isdigit():
                url = 'http://pages.cs.wisc.edu/~remzi/OSTEP/' + link.css('a::attr(href)').extract_first()
                item = BookpdfItem()
                item['title'] = title
                item['file_urls'] = [url]
                yield item
