import scrapy

from qoutes.items import QoutesItem

class QouteSpider(scrapy.Spider):
    name = "qoute"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com"]

    def parse(self, response):
        """parses the qouteItem created by the Spider
        
        see qoutes.items.py for more info on qoute model
        """
        for qoute in response.css('body > div > div:nth-child(2) > div.col-md-8 > div.qoute'):
            item = QoutesItem()
            item['qoute'] = qoute.css('span.text::text').get()
            item['author'] = qoute.css('span > small.text::text').get()
            yield item
