# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql


class TutorialPipeline(object):
    def process_item(self, item, spider):
        return item


class yangjialinPipeline(object):
    def process_item(self, item, spider):
        return item


class SaikrMysqlPipeline(object):
    saikr_name = 'saikr'
    saikrInsert = '''
        insert into saikr(title,image_url,team_category,com_url,source_url,charge,com_level,com_object,signup_start_date,signup_end_date,com_start_date,com_end_date,com_orginaziton,com_category)
        values('{title}','{image_url}','{team_category}','{com_url}','{source_url}','{charge}','{com_level}','{com_object}','{signup_start_date}','{signup_end_date}','{com_start_date}','{com_end_date}','{com_orginaziton}','{com_category}')
    '''

    def __init__(self, settings):
        self.settings = settings

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings)

    def open_spider(self, spider):
        # 连接数据库
        self.connect = pymysql.connect(
            host=self.settings.get('MYSQL_HOST'),
            port=self.settings.get('MYSQL_PORT'),
            db=self.settings.get('MYSQL_DBNAME'),
            user=self.settings.get('MYSQL_USER'),
            passwd=self.settings.get('MYSQL_PASSWD'),
            charset='utf8',
            use_unicode=True
        )
        self.cursor = self.connect.cursor()
        self.connect.autocommit(True)

    def process_item(self, item, spider):
        if spider.name == "saikr":
            sqltext = self.saikrInsert.format(
                title=pymysql.escape_string(item['title']),
                image_url=pymysql.escape_string(item['image_url']),
                team_category=pymysql.escape_string(item['team_category']),
                com_url=pymysql.escape_string(item['com_url']),
                source_url=pymysql.escape_string(item['source_url']),
                charge=pymysql.escape_string(item['charge']),
                com_level=pymysql.escape_string(item['com_level']),
                com_object=pymysql.escape_string(item['com_object']),
                signup_start_date=pymysql.escape_string(item['signup_start_date']),
                signup_end_date=pymysql.escape_string(item['signup_end_date']),
                com_start_date=pymysql.escape_string(item['com_start_date']),
                com_end_date=pymysql.escape_string(item['com_end_date']),
                com_orginaziton=pymysql.escape_string(item['com_orginaziton']),
                com_category=pymysql.escape_string(item['com_category']))
            self.cursor.execute(sqltext)
        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.connect.close()


class SaikrPipeline(object):
    def process_item(self, item, spider):
        with open('saikr.txt', 'a', encoding='utf-8') as f:
            titles = item['title']
            f.write('title: ' + titles + '\n')
            com_urls = item['com_url']
            f.write('com_url: ' + com_urls + '\n')
            source_urls = item['source_url']
            f.write('source_url: ' + source_urls + '\n')
            images_urls = item['image_url']
            f.write('image_url: ' + images_urls + '\n')
            team_categorys = item['team_category']
            f.write('team_category: ' + team_categorys + '\n')
            charges = item['charge']
            f.write('charge: ' + charges + '\n')
            com_levels = item['com_level']
            f.write('com_level: ' + com_levels + '\n')
            signup_start_dates = item['signup_start_date']
            f.write('signup_start_date: ' + signup_start_dates + '\n')
            signup_end_dates = item['signup_end_date']
            f.write('signup_end_date: ' + signup_end_dates + '\n')
            com_start_dates = item['com_start_date']
            f.write('com_start_date: ' + com_start_dates + '\n')
            com_end_dates = item['com_end_date']
            f.write('com_end_date: ' + com_end_dates + '\n')
            com_categorys = item['com_category']
            f.write('com_category: ' + com_categorys + '\n')

            orginazitions = item['com_orginaziton']
            f.write('organizition: ' + orginazitions + '\n')

            com_objects = item['com_object']
            f.write('com_object: ' + com_objects + '\n\n')
        return item
