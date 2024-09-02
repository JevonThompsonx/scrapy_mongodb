# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class QoutesItem(scrapy.Item):
    """The model of scraped qoutes 

    Attributes 
    ---------
    author:str
    qoute:str
    url:str

    urlTarget = https://quotes.toscrape.com
    base css selector = body > div > div:nth-child(2) > div.col-md-8 > div.qoute
    
    The base css selector will be used to target    all divs that fit the qoute schema

    css selectors
    ------------
    author =  span.text::text
    qoute =  span > small.author::text
    """
    author = scrapy.Field()
    qoute = scrapy.Field()
    url = scrapy.Field()
    _id = scrapy.Field()
