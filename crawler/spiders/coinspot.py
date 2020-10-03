import scrapy

class CoinspotSpider(scrapy.Spider):
    name = 'coinspot'
    allowed_domains = ['www.coinspot.com.au']
    start_urls = ['https://www.coinspot.com.au/tradecoins']

    def parse(self, response):
        rows = response.xpath('//table/tr')
        for r in rows:
            c1, c2, c3, c4, c5, c6, c7, c8 = r.xpath('td')

            code_name = c1.xpath('span[contains(@class, "visible-xs")]/text()').get()
            name = c1.xpath('span[contains(@class, "hidden-xs")]/text()').get()

            buy = c2.xpath('span/text()').get()
            sell = c3.xpath('span/text()').get()

            market_cap = c4.xpath('span/text()').get()

            volume = c5.xpath('span/text()').get()
            change = c6.xpath('span/span/text()').get()

            yield {
                'code_name': code_name,
                'name': name,
                'buy': buy,
                'sell': sell,
                'market_cap': market_cap,
                'volume': volume,
                'change': change,
            }
