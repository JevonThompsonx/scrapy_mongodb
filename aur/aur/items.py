# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class aurPackage(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    currentVersion = scrapy.Field()
    description = scrapy.Field()
    maintainer = scrapy.Field()
    lastUpdated = scrapy.Field()