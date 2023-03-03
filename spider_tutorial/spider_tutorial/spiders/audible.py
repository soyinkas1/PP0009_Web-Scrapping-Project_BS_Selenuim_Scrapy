import scrapy


class AudibleSpider(scrapy.Spider):
    name = "audible"
    allowed_domains = ["www.audible.co.uk"]
    start_urls = ["https://www.audible.co.uk/search/"]

    def parse(self, response):
        product_container = response.xpath('//li[contains(@class,"productListItem")]')

        for product in product_container:
            product_title = product.xpath('.//h3/a/text()').get()
            product_author = product.xpath(".//li[contains(@class,'authorLabel')]/span/a/text()").getall()

            yield {
                'Title':product_title,
                'Author':product_author

            }

        pagination = response.xpath('//ul[contains(@class, "pagingElements")]')
        next_page = pagination.xpath('.//span[contains(@class, "nextButton")]/a/@href').get()

        if next_page:
            yield response.follow(url=next_page, callback=self.parse)






