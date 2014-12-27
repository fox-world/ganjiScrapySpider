# -*- coding: utf-8 -*-

# Scrapy settings for ganji project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'ganjiScrapySpider'

SPIDER_MODULES = ['ganjiScrapySpider.spiders']
NEWSPIDER_MODULE = 'ganjiScrapySpider.spiders'

ITEM_PIPELINES={
    'ganjiScrapySpider.pipelines.JSONPipeline':800
}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'ganjiScrapySpider (+http://www.yourdomain.com)'
