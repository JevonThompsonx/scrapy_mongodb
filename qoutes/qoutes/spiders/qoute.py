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
        for qoute in response.css('body > div > div:nth-child(2) > div.col-md-8 > div.quote'):
            item = QoutesItem()
            item['qoute'] = qoute.css('span.text::text').get()
            item['author'] = qoute.css('span > small.author::text').get()
            yield item

        next_page = response.css("nav > ul > li > a").get()
        if next_page:
            next_page_url = response.urljoin(next_page)
            yield scrapy.Request(url=next_page_url, callback=self.parse)
