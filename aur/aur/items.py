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
    # url = https://archlinux.org/packages/?page=1&
    #base = #pkglist-results-form > table > tbody


    name = scrapy.Field()
    #tr:nth-child(1) > td:nth-child(3) > a::text
    currentVersion = scrapy.Field()
    #tr:nth-child(1) > td:nth-child(4) > a::text
    description = scrapy.Field()
    #tr:nth-child(1) > td:nth-child(5)::text
    lastUpdated = scrapy.Field()
    #tr:nth-child(1) > td:nth-child(6)::text
