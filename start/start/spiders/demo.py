import scrapy
from start.items import StartItem
from scrapy_splash import SplashRequest

#这里写lua脚本
script = """
function main(splash, args)
  assert(splash:go(args.url))
  assert(splash:wait(0.5))
  local title = splash:evaljs("document.title")

  return {
    html = splash:html(),
    png = splash:png(),
    har = splash:har(),
    title=title
  }
end
"""




class DemoSpider(scrapy.Spider):
    name = 'demo'
    allowed_domains = ['www.baidu.com']
    start_urls = ['http://www.baidu.com']
    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, callback=self.parse, endpoint='execute',args={'lua_source': script, 'wait': 0.7})
    def parse(self, response):
        items=StartItem()
        #  print(response.body)
        items['title']=response.xpath('//title/text()').extract()
        yield items
