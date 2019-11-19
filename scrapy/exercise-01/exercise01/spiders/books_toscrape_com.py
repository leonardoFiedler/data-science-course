import scrapy
from exercise01.items import Exercise01Item

class BooksToscrapeComSpider(scrapy.Spider):
    name = 'books.toscrape.com'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']

    def parseAll(self, response):
        for (i, book) in enumerate(response.css("section .row li")):
            linkDetailItem = response.request.url + book.css(".product_pod h3 a").attrib['href']
            name = book.css(".product_pod h3 a").attrib['title']
            price = book.css(".product_pod .price_color::text").get()
            available = book.css(".product_price .instock.availability").extract() != None
            
            item = Exercise01Item(
                name=name,
                price=price,
                available=available)

            yield scrapy.Request(linkDetailItem, callback=self.parseItem, cb_kwargs=dict(item=item))




    def parseItem(self, response, item):
        pass
        
