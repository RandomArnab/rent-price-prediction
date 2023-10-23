# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class RentScrapeItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    city = scrapy.Field()
    locality = scrapy.Field()
    price = scrapy.Field()
    area = scrapy.Field()
    status = scrapy.Field()
    deposit = scrapy.Field()
    num_bath = scrapy.Field()

    pass
