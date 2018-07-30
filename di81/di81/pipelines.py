# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
import os
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
from scrapy.utils.project import get_project_settings


class Di81Pipeline(object):
    def process_item(self, item, spider):
        return item


class Di81ImagePipeline(ImagesPipeline):
    IMAGES_STORE = get_project_settings().get("IMAGES_STORE")

    def get_media_requests(self, item, info):
        for image_url in item['image_urls']:
            yield scrapy.Request(image_url)

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        os.rename(self.IMAGES_STORE + "/" + image_paths[0], self.IMAGES_STORE + "/full/" + item['title'] + ".jpg")
        item['image_paths'] = self.IMAGES_STORE + "/full/" + item['title']
        return item
