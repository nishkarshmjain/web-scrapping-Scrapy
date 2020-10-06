import scrapy
from ..items import ecom_item

class EcomSpiderSpider(scrapy.Spider):
    name = 'ecom_spider'
    allowed_domains = ['https://www.matchesfashion.com/']
    start_urls = ['https://www.matchesfashion.com/intl/mens/shop/shoes?page=1&noOfRecordsPerPage=240&sort=']

    def parse(self, response):
        
        items = ecom_item()
        
        name = response.css('.lister__item__details::text').extract()
        brand= response.css('.lister__item__title').css('::text').extract()
        price= response.css('.lister__item__price-full').css('::text').extract()
        image_url = response.css('.lazy::attr(src').extract()
        product_url = response.css('.lister__item__inner').css('::text').extract()
        
        items['Name'] = name
        items['Brand'] = brand
        items['Price'] = price
        items['Image_Url'] = image_url
        items['Product_Url'] = product_url
        
        yield items
        
        
    
