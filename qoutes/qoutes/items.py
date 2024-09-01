# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class QoutesItem(scrapy.Item):
   #url = https://quotes.toscrape.com
    #base css selector = body > div > div:nth-child(2) > div.col-md-8 > div.qoute
    author = scrapy.Field() # span.text::text
    qoute = scrapy.Field() # span > small.author::text
