import scrapy


class ImdbSpider(scrapy.Spider):
    name = 'imdb'
    start_urls = ['https://www.imdb.com/chart/top/']

    def parse(self, response):
        list_notas = response.css('strong::text').getall()
        pos = 0
        for filme in response.css('.titleColumn'):
            yield {
                'titulo': filme.css('.titleColumn a::text').get(),
                'ano': filme.css('.secondaryInfo::text').get()[1:-1],
                'nota': list_notas[pos]
            }
            pos = pos + 1
        pass
