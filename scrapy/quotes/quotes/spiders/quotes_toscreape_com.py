from datetime import datetime

import scrapy

from quotes.items import QuotesItem


class QuotesToscreapeComSpider(scrapy.Spider):
    name = 'quotes.toscrape.com'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    author = None

    def start_requests(self):
        yield scrapy.Request(
            'http://quotes.toscrape.com/',
            callback=self.parse
        )

    def parse(self, response):
        for (i, quote) in enumerate(response.css('.quote')):
            text = quote.css('span.text::text').get()
            author = quote.css('.author::text').get()
            print(text)
            yield QuotesItem(
                text=text,
                author=author,
                rank=i,
                url=response.url,
                scrape_date = datetime.now().isoformat()
            )

        url = response.css('.pager .next a::attr(href)').get()
        # if url is not None:
        if url:
            yield response.follow(url)
