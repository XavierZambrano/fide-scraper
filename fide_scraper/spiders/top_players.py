import scrapy


class TopPlayersSpider(scrapy.Spider):
    name = "top_players"
    allowed_domains = ["ratings.fide.com"]
    start_urls = ["https://ratings.fide.com/a_top.phtml"]

    def parse(self, response):
        rows = response.xpath('//div[@id="top_rating_div"]//tr')
        rows_body = rows[1:]
        for container in rows_body:
            yield {
                "rank": container.xpath('.//td[1]/text()').get(),
                "name": container.xpath('.//td[2]/a/text()').get(),
                "federation": container.xpath('.//td[3]/text()[2]').get().strip(),
                "rating": container.xpath('.//td[4]/text()').get(),
                "born_year": container.xpath('.//td[6]/text()').get(),
            }
