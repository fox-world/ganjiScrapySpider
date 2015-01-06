# -*- coding: utf-8 -*-

# Scrapy settings for ganji project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'ganjiScrapySpider'

DOWNLOAD_DELAY = 0.25

SPIDER_MODULES = ['ganjiScrapySpider.spiders']
NEWSPIDER_MODULE = 'ganjiScrapySpider.spiders'

ITEM_PIPELINES={
    'ganjiScrapySpider.pipelines.JSONPipeline':800
}

DOWNLOADER_MIDDLEWARES = {
    'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 110,
    'ganjiScrapySpider.middlewares.ProxyMiddleware': 100,
}

PROXY_LIST=[
'120.83.5.164:18000',
'222.73.233.135:80',
'112.45.184.151:8123',
'192.99.240.225:3128'
]
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'ganjiScrapySpider (+http://www.yourdomain.com)'
