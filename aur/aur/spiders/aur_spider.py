import scrapy

from aur.items import AurPackage

class AurSpiderSpider(scrapy.Spider):
    name = "aur_spider"
    allowed_domains = ["archlinux.org"]
    start_urls = ["https://archlinux.org/packages/?page=1&"]

    def parse(self, response):
        """Tells the scrapy spider what it's looking for onsite
        
        1. Digs into the table body with all of the packages as well as their info
        2. Loops through all packages 
        3. Find the target package *name*,*current*,*version*,*description*,*lastUpdated* info
        4. Returns results

        """
        for aur_package in response.css("#pkglist-results-form > table > tbody"):
            item = AurPackage()
            item["name"] = aur_package.css("td:nth-child(3) > a::text").get()
            item["currentVersion"] = aur_package.css("td:nth-child(4)::text").get()
            item["description"] = aur_package.css("td:nth-child(5)::text").get()
            item["lastUpdated"] = aur_package.css("td:nth-child(6)::text").get()
            yield item
