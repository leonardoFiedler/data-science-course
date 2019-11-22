import scrapy
from exercise01.items import Exercise01Item
from datetime import datetime
import re

class BooksToscrapeComSpider(scrapy.Spider):
    name = 'books.toscrape.com'
    allowed_domains = ['books.toscrape.com']

    categories = [("travel", "travel_2"), ("mystery", "mystery_3"), ("historical fiction", "historical-fiction_4")]

    def __init__(self, category=None, *args, **kwargs):
        super(BooksToscrapeComSpider, self).__init__(*args, **kwargs)
        if (category is None):
            self.start_urls = ['http://books.toscrape.com/']
        else:
            (_, urlpath) = [item for item in self.categories if item[0] == category.lower()][0]
            print("Category Path", urlpath)
            self.start_urls = ['http://books.toscrape.com/catalogue/category/books/%s/index.html' % urlpath]

    def parse(self, response):
        for (i, book) in enumerate(response.css("section .row li")):
            linkDetailItem = response.urljoin(book.css(".product_pod h3 a::attr(href)").get())
            name = book.css(".product_pod h3 a::attr(title)").get()
            price = book.css(".product_pod .price_color::text").get()[1:]

            available = book.css(".product_price .instock.availability").extract() is not None
            
            item = Exercise01Item(
                name=name,
                price=price,
                available=available)

            yield scrapy.Request(linkDetailItem, callback=self.parseItem, cb_kwargs=dict(item=item))
        
        nextPageUrl = response.css('.pager .next a::attr(href)').get()

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
        
