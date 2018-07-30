# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Di81Item(scrapy.Item):
    title = scrapy.Field()
    image_urls = scrapy.Field()
    # 文件路径 + 名
    image_paths = scrapy.Field()
