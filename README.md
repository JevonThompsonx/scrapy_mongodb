# A web scraping project built w/ scrapy and mongodb
---
## Target
This project uses [qoutes.toscrape.com](https://quotes.toscrape.com) as a target

## Tools 
- [Mongodb](https://www.mongodb.com) to store data
- [scrapy](https://docs.scrapy.org/en/latest/)
    -  to crawl the site
    -  drop duplicates
    -  other middleware
- [pydotenv](https://github.com/theskumar/python-dotenv) to read mongo key from dotenv file
    - named *mongo_connect_string*
- hashlib to create unique ids

## What does it do? 
- scrapes the site to find an individual quote
- drops duplicate quotes
- adds new quote to mongodb
- logs warning level info to a seperate file 

## Prerequisites
1. python
2. a mongo database named **qoutes_db** w/ a collection named **qoutes**

## How to
This can be tested by cloning this repo:
1. ``git clone https://github.com/JevonThompsonx/scrapy_mongodb.git``
2. ``cd scrapy_mongod``
3. ``pip install -r requirements.txt``
5. create a **.env** file with mongo connet string ( I used mongo atlas)
6. activate the python virtual environment according to ur shell
    - bash/zsh: ``source venv/bin/activate``
    - fish: ``source /path/to/venv/bin/activate.fish``
7. ``cd qoutes``
8. ``scrapy crawl qoute`` (yes with the mispelling of quote)

## It works
I mispelled quote pretty early on and didn't want to start the whole thing over so I just fixed it where it mattered and left the rest

## Suggestions
Please feel free to leave any comments w/ suggestions on this project or what to try next in order to fascilitate my growth w/ python and soon rust. Thanks for checking this out!!
