"""pyMongo test script

A test sript to make sure I've set up python w/ mongo correctly. I've only done this in javascript so I figured I should try it before I write the code. Espescially since I'm connecting w/ mongo atlas which isn't what the thing teaching me is using
"""
import os
from pprint import pprint
#import httpx
#import scrapy
import warnings
from cryptography.utils import CryptographyDeprecationWarning
warnings.filterwarnings("ignore", category=CryptographyDeprecationWarning)
from dotenv import load_dotenv
from pymongo import MongoClient
load_dotenv()
mongo_key = os.getenv('mongo_key')
mongo_connect_string = os.getenv('mongo_connect_string')
client = MongoClient(mongo_connect_string)
db = client['expressConnect']
collection = db['groceryproducts']
pprint(list(collection.find()))
