from scrapy.spider import BaseSpider
from scrapy.selector import Selector
from ..items import BlogScraperItem


class MyBlogSpider(BaseSpider):
    name = 'mouse'
    start_urls = ['https://www.blog.pythonlibrary.org']

    def parse(self, response):
        selector = Selector(response)
        blog_titles = selector.xpath("//h1[@class='entry-title']")
        selections = []
    
        for data in blog_titles:
            selection = BlogScraperItem()
            selection['title'] = data.xpath("a/text()").extract()
            selection['link'] = data.xpath("a/@href").extract()
            selections.append(selection)
        
        return selections