"""
My first project with python using scrappy to web scrape

The goal will be to web scrape the arch user repository for package information
"""
from pprint import pprint
import httpx
import scrapy
from parsel import Selector

response = httpx.get('https://archlinux.org/packages/?page=1&').text
selector = Selector(text = response)
packages = selector.css("#pkglist-results-form > table > tbody")
for package in packages:
    pprint(package.css('tbody > tr:nth-child(1) > td:nth-child(4)::text').get())
