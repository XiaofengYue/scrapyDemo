# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class DoubanmoviePipeline(object):
    def process_item(self, item, spider):
        return item


class doubanPipeline(object):
    def process_item(self, item, spider):
        with open('douban.txt', 'a', encoding='utf-8') as f:
            f.write('rank   :' + item['rank'] + '\n')
            f.write('score  :' + item['score'] + '\n')
            f.write('title  :' + item['title'] + '\n')
            f.write('category   :' + item['category'] + '\n')
            f.write('runtime    :' + item['runtime'] + '\n')
            f.write('year   :' + item['year'] + '\n\n')

        return item
