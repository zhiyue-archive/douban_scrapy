# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanScrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    director = scrapy.Field()
    scriptwriter = scrapy.Field()
    actor = scrapy.Field()
    film_type = scrapy.Field()
    produce_country = scrapy.Field()
    langue = scrapy.Field()
    release_date = scrapy.Field()
    play_duration = scrapy.Field()
    alias = scrapy.Field()
    imdb = scrapy.Field()
    
    pass
