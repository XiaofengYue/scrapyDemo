# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class SaikrItem(scrapy.Item):
    title = scrapy.Field()  # 标题
    image_url = scrapy.Field() # 图片地址
    com_content = scrapy.Field()  # 内容
    team_category = scrapy.Field()  # 组队还是个人
    com_url = scrapy.Field()  # 比赛的官网
    source_url = scrapy.Field()  # 来源的网站 赛氪
    charge = scrapy.Field()  # 报名费
    com_level = scrapy.Field()  # 比赛级别
    com_object = scrapy.Field()  # 参赛对象
    signup_start_date = scrapy.Field()  # 报名开始时间
    signip_end_date = scrapy.Field()  # 报名结束时间
    com_start_date = scrapy.Field()  # 比赛开始时间
    com_end_date = scrapy.Field()  # 比赛结束时间
    com_orginaziton = scrapy.Field() #比赛的举办方
    com_category = scrapy.Field() #比赛的类型
