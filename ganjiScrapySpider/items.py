# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field  

class HouseItem(Item):
    # define the fields for your item here like:
    title = Field() #标题
    community = Field() #名称
    price = Field() #价格
    area = Field()  #面积
    houseType = Field() #户型
    layer = Field() #楼层
    direction = Field() #朝向
