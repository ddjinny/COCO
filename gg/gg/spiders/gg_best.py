import scrapy


class GgBestSpider(scrapy.Spider):
    name = 'gg_best'
    allowed_domains = ['http://corners.gmarket.co.kr/Bestsellers']
    start_urls = ['http://http://corners.gmarket.co.kr/Bestsellers/']

    def parse(self, response):
        pass
