import scrapy


class AudibleSpider(scrapy.Spider):
    name = "audible"
    allowed_domains = ["www.audible.co.uk"]
    # start_urls = ["https://www.audible.co.uk/search/"]

    def start_requests(self):
        yield scrapy.Request(url='https://www.audible.co.uk/search/',callback=self.parse,
                       headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.57'})

    def parse(self, response):
        product_container = response.xpath('//li[contains(@class,"productListItem")]')
        for product in product_container:
            product_title = product.xpath('.//h3/a/text()').get()
            product_author = product.xpath(".//li[contains(@class,'authorLabel')]/span/a/text()").getall()

            yield {
                'Title':product_title,
                'Author':product_author,
                'User-Agent':response.request.headers['User-Agent']

            }

        pagination = response.xpath('//ul[contains(@class, "pagingElements")]')
        next_page = pagination.xpath('.//span[contains(@class, "nextButton")]/a/@href').get()

        if next_page:
            yield response.follow(url=next_page, callback=self.parse,
                                  headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.57'})






