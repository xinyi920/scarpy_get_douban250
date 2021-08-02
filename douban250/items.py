# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    ranking = scrapy.Field()  # 排名
    name = scrapy.Field()  # 电影名
    introduce = scrapy.Field()  # 简介
    star = scrapy.Field()  # 星级
    comments = scrapy.Field()  # 评论数
    describe = scrapy.Field()  # 描述
    img_url = scrapy.Field()    # 电影图片
