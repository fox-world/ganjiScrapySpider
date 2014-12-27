# -*- coding: utf-8 -*-

from scrapy.spider import Spider
from scrapy.selector import Selector

from ganjiScrapySpider.items import HouseItem

class GanjiSpider(Spider):

	name="ganjiSpider"
	allowed_domains=['ganji.com']
	start_urls=['http://bj.ganji.com/fang1/']

	def parse(self,response):
		sel=Selector(response)
		houses=sel.xpath('//li[@class="list-img clearfix"]')
		houseItems=[]
		for house in houses:
			hItem=HouseItem()
			hItem['title']=house.select('div[@class="list-mod4"]/div[@class="info-title"]/a/text()').extract()[0]
			hItem['name']=house.select('div[@class="list-mod4"]/div[@class="list-mod2"]/div[@class="list-word"]/span[@class="list-word-col"]/a/text()').extract()[0]
			hItem['price']=house.select('div[@class="list-mod4"]/div[@class="list-mod3 clearfix"]/p[@class="list-part"]/em[@class="sale-price"]/text()').extract()[0]
			houseItems.append(hItem)
		return houseItems
