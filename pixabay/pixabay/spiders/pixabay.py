import scrapy
import re
from pixabay.items import PixabayItem


class PixabaySpider(scrapy.Spider):
    name = 'pixabay'

    baseurl = 'https://pixabay.com/en/editors_choice/?media_type=photo&pagi='
    start_urls = []
    # website ten pages
    for i in range(1, 6):
        start_urls.append(baseurl + str(i))

    def parse(self, response):
        imageUrls = response.css('div.flex_grid div.item img::attr(srcset)').extract()
        print(imageUrls)
        x = '(.*jpg)'
        for imagesUrl in imageUrls:
            images = imagesUrl.split(',')
            item = PixabayItem()
            imageurl = re.match(x, images[0]).group()
            item['image_urls'] = [imageurl]
            yield item
