import scrapy


class TopPlayersSpider(scrapy.Spider):
    name = "top_players"
    allowed_domains = ["ratings.fide.com"]
    start_urls = ["https://ratings.fide.com"]

    def parse(self, response):
        pass
