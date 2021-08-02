# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import json
import scrapy
from scrapy.pipelines.images import ImagesPipeline


class MoviePipeline(object):
    def __init__(self):
        # 打开文件
        self.file = open('data.json', 'w', encoding='utf-8')

    # 该方法用于处理数据
    def process_item(self, item, spider):
        # 读取item中的数据
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        # 写入文件
        self.file.write(line)
        # 返回item
        return item

    # 该方法在spider被开启时被调用。
    def open_spider(self, spider):
        pass

    # 该方法在spider被关闭时被调用。
    def close_spider(self, spider):
        self.file.close()


class ImgsPipeline(ImagesPipeline):
    # 主要重写下面三个父类方法
    def get_media_requests(self, item, info):
        yield scrapy.Request(item['img_url'], meta={'item': item})

    def file_path(self, request, response=None, info=None):
        image_name = request.meta['item']['name']
        return './%s.jpg' % image_name

    def item_completed(self, results, item, info):
        return item  # 返回给下一个即将被执行的管道类
