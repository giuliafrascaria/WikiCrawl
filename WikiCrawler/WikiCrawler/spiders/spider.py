# -*- coding: utf-8 -*-
import scrapy
import os, sys
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(CURRENT_DIR))
#from .items import WikiItem
#from WikiCrawler import WikiItem

class WikiCrawler(scrapy.Spider):
    name = 'WikiCrawler'
    allowed_domains = ["wikipedia.org"]
    start_urls = (
        'https://it.wikipedia.org/wiki/Due_americane_scatenate',
    )
    '''
    The parse() method is in charge of processing the response and returning
    scraped data (as Item objects) and
    more URLs to follow (as Request objects).

    def parse(self, response):
        for sel in response.xpath('//div[@id="mw-content-text"]/@href'):
            item = WikiItem()
            #title = sel.xpath('a/text()').extract()
            item['link'] = sel.xpath('a/@href').extract()
            print item['link']
            yield item
    '''
    def parse(self, response):
        for href in response.css("ul.directory.dir-col > li > a::attr('href')"):
            url = response.urljoin(href.extract())
            yield scrapy.Request(url, callback=self.parse_dir_contents)

    def parse_dir_contents(self, response):
        for sel in response.xpath('//div[@id="mw-content-text"]/@href'):
            item = WikiItem()
            item['title'] = sel.xpath('a/text()').extract()
            item['link'] = sel.xpath('a/@href').extract()
            print item['link']
            yield item
