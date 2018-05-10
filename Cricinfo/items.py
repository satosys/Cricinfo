# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import Compose, MapCompose, Join, TakeFirst

class CricinfoItems(scrapy.Item):
    Full_name_player = Field()
    Born = Field()
    Major_teams = Field()
    Playing_Role = Filed()
    Batting_style = Field()
    Bowling_style = Field()
