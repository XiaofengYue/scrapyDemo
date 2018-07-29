# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class TutorialPipeline(object):
    def process_item(self, item, spider):
        return item


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
            signip_end_dates = item['signip_end_date']
            f.write('signip_end_date: ' + signip_end_dates + '\n')
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
