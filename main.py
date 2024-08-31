"""
My first project with python using scrappy to web scrape

The goal will be to web scrape the arch user repository for package information
"""
from pprint import pprint
import httpx
import scrapy
from parsel import Selector
URL_START = 'https://quotes.toscrape.com'
response = httpx.get(URL_START).text
selector = Selector(text = response)
qoutes = selector.css("body > div > div:nth-child(2) > div.col-md-8")
pprint(qoutes.get())
