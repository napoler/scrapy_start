import scrapy
from start.items import StartItem


class DemoSpider(scrapy.Spider):
    name = 'demo'
    allowed_domains = ['www.baidu.com']
    start_urls = ['http://www.baidu.com']

    def parse(self, response):
        items=StartItem()
        #  print(response.body)
        items['title']=response.xpath('//title/text()').extract()
        yield items
