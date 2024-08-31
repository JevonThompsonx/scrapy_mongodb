# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AurPackage(scrapy.Item):
    """Class created to model the web scraped aur package
    
    `scrapy.Field() is used to create a temporary placeholder 
    it's really a dict alias. The expected values are below`

    Attributes
    ----------
    name:str #css selector
    description:str #css selector
    maintainer:str #css selector
    lastUpdated:str #css selector
    """
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    # element.css('td:nth-child(1)> a::text')
    currentVersion = scrapy.Field()
    #element.css('td:nth-child(2)::text')
    description = scrapy.Field()
    #element.css('td:nth-child(5)::text')
    maintainer = scrapy.Field()
    #element.css('td:nth-child(6) > a::text')
    lastUpdated = scrapy.Field()
    #element.css('td:nth-child(7)a::text')
