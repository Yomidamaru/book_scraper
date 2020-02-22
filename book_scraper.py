import scrapy

class BookSpider(scrapy.Spider):
    name = 'bookspider'
    start_urls = ['http://books.toscrape.com']
    
    def parse(self.response):
        response.css('article.product_pod')
