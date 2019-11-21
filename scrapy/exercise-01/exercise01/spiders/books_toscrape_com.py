import scrapy
from exercise01.items import Exercise01Item
from datetime import datetime
import re

class BooksToscrapeComSpider(scrapy.Spider):
    name = 'books.toscrape.com'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']

    def start_requests(self):
        yield scrapy.Request(
            'http://books.toscrape.com/',
            callback=self.parse
        )

    def parse(self, response):
        for (i, book) in enumerate(response.css("section .row li")):
            # Gets the link to item - Remove the last part of the request URL
            baseUrl = "/".join(response.request.url.split("/")[:-1])

            # Join whith / and href attribute to get the full path to redirect
            linkDetailItem = baseUrl + "/" + book.css(".product_pod h3 a").attrib['href']

            name = book.css(".product_pod h3 a").attrib['title']
            price = book.css(".product_pod .price_color::text").get()
            available = book.css(".product_price .instock.availability").extract() != None
            
            item = Exercise01Item(
                name=name,
                price=price,
                available=available)

            yield scrapy.Request(linkDetailItem, callback=self.parseItem, cb_kwargs=dict(item=item))
        
        nextPageUrl = response.css('.pager .next a::attr(href)').get()
        print("Next Page", nextPageUrl)
        if nextPageUrl:
            yield response.follow(nextPageUrl)

    def parseItem(self, response, item):
        quantity = response.css(".product_main .instock.availability::text").extract()[1]
        quantity = re.findall(r'\d+', quantity)[0]
        
        item['quantity'] = quantity

        stars = response.css(".product_main .star-rating::attr(class)").get().split()[1]
        for (i, number) in enumerate(["Zero", "One", "Two", "Three", "Four", "Five"]):
            if number == stars:
                stars = i
                break
        
        item['rate'] = stars
        
        category = response.css(".page_inner .breadcrumb li:nth-child(3) a::text").get()
        item['category'] = category

        upc = response.css(".table.table-striped tr:nth-child(1) td::text").get()
        item['upc'] = upc
        item['url'] = response.url,
        item['scrape_date'] = datetime.now().isoformat()
        
        yield item
        
