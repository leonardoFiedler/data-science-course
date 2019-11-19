import scrapy

class Exercise01Item(scrapy.Item):
    name = scrapy.Field()
    price = scrapy.Field()
    available = scrapy.Field()
    quantity = scrapy.Field()
    rate = scrapy.Field()
    category = scrapy.Field()
    upc = scrapy.Field()
