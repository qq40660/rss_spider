# _*_ coding: utf-8 _*_
# author: zhaowei

from scrapy.item import Item, Field


class RssSpiderInfo(Item):
    info_title = Field()
    info_desc = Field()
    info_lang = Field()
    info_pubDate = Field()


class RssSpiderItem(Item):
    link = Field()
    title = Field()
    desc = Field()
    pubDate = Field()
    category = Field()
    source = Field()
    summary = Field()
    content = Field()
    current_url = Field()
    is_pass = Field()
