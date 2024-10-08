import scrapy

from qoutes.items import QoutesItem

class QouteSpider(scrapy.Spider):
    name = "qoute"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com"]

    def parse(self, response):
        """parses the qouteItem created by the Spider
        
        see qoutes.items.py for more info on qoute model
        @url https://quotes.toscrape.com
        @returns items 0 20
        @returns request 1 50
        @scrapes qoute author identifier
        """
        for qoute in response.css('body > div > div:nth-child(2) > div.col-md-8 > div.quote'):
            item = QoutesItem()
            quote =  qoute.css('span.text::text').get()
            author = qoute.css('span > small.author::text').get()

            item['qoute'] = quote
            item['identifier'] = f'${author}:{quote}'
            item['author'] = author
            yield item

        next_page = response.css("nav > ul > li > a::attr(href)").get()
        if next_page:
            next_page_url = response.urljoin(next_page)
            self.logger.info(
                f"Navigating to next page with URL {next_page_url}."
            )
            yield scrapy.Request(url=next_page_url, callback=self.parse)
