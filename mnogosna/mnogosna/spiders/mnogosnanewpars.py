import scrapy


class MnogosnanewparsSpider(scrapy.Spider):
    name = "mnogosnanewpars"
    allowed_domains = ["mnogosna.ru"]
    start_urls = ["https://mnogosna.ru/tipy-matrasov/matrasy/"]

    def parse(self, response):
        # Extract product information
        for product in response.css('div.product-item'):  # Adjust the CSS selector based on the actual HTML structure
            yield {
                'title': product.css('h2.product-title::text').get().strip(),  # Extract text
                'link': product.css('a.product-link::attr(href)').get(),        # Extract href attribute
                'price': product.css('span.price::text').get(),                 # Extract price text
            }

        # Follow pagination links (if applicable)
        next_page = response.css('a.next-page::attr(href)').get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)