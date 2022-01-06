# Spider 1 
# Articles.py which scrape article links# imports
import scrapy
from scrapy.http import Request

class ArticlesSpider(scrapy.Spider):
    name = 'Articles'
    allowed_domains = ['bbc.com']
    start_urls = ['https://www.bbc.com/']
    
    def start_requests(self):
        url="https://www.bbc.com/news/world-{}"
        link_urls = [url.format(i) for i in range(59800000,59814662)]# Loops through 500 pages to get the article links
        for link_url in link_urls:
            print(link_url)# Request to get the HTML content
            request=Request(link_url, cookies={'store_language':'en'}, 
            callback=self.parse_main_pages)
            yield request
    
    def parse_main_pages(self,response):
        filename = response.url.split("/")[-1] + '.html'
        with open('../../../artcl/ ' + filename, 'wb') as f:
            f.write(response.body)
            
    def parse(self, response):
        pass