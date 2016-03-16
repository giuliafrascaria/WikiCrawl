# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem
import json

class WikicrawlerPipeline(object):
    def process_item(self, item, spider):
        return item

    '''
    Typical uses of item pipelines are:

    cleansing HTML data
    validating scraped data (checking that the items contain certain fields)
    checking for duplicates (and dropping them)
    storing the scraped item in a database
    '''

    def __init__(self):
        self.link_seen = set()
        self.file = open('items.jl', 'wb')


    def process_item(self, item, spider):
        if not(item['link'] in self.link_seen):
            #check for duplicate page in the list, if it is not duplicate write a json entry
            line = json.dumps(dict(item)) + "\n"
            self.file.write(line)
            self.link_seen.add(item['link'])
            return item
        else:
            #if it is duplicate dump the item
            raise DropItem("Missing price in %s" % item)
