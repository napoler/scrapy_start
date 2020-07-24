# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class StartItem(scrapy.Item):
    # define the fields for your item here like:
    collection ='data'
    title = scrapy.Field()
    url= scrapy.Field()
    pass
