# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
from scrapy.pipelines.files import FilesPipeline
from scrapy.utils.project import get_project_settings


class BookpdfPipeline(FilesPipeline):
    FILES_STORE = get_project_settings().get("FILES_STORE")

    def item_completed(self, results, item, info):
        files = [x['path'] for ok, x in results if ok]
        os.rename(self.FILES_STORE + "/" + files[0], self.FILES_STORE + "/full/" + item['title'] + ".pdf")
        item['files'] = self.FILES_STORE + "/full/" + item['title']
        return item
