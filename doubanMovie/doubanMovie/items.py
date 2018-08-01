# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanmovieItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class doubanMovieItem(scrapy.Item):
    title = scrapy.Field()
    category = scrapy.Field()
    runtime = scrapy.Field()
    actor = scrapy.Field()
    rank = scrapy.Field()
    year = scrapy.Field()
    score = scrapy.Field()
