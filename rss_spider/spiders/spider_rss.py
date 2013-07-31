# _*_ coding: utf-8 _*_
# author: zhaowei

import MySQLdb as mysqldb

from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.spiders import XMLFeedSpider
from scrapy.http import HtmlResponse

from rss_spider.items import RssSpiderItem
from rss_spider.settings import HOST, DB, USER, PASSWD
# from rss_spider.bs_extractors import SoupLinkExtractor
import urllib2

conn = mysqldb.connect(host=HOST, user=USER, passwd=PASSWD, db=DB, charset="utf8")
cursor = conn.cursor()
urls = cursor.execute("select link from rss_urls order by RAND() limit 100")
urls = cursor.fetchall()
# conn.close()


def next_url():
    list_of_urls = [n[0] for n in urls]
    return list_of_urls


class RssSpider(XMLFeedSpider):
    name = "spider_rss"
    start_urls = next_url()

    iterator = "iternodes"
    itertag = "item"

    def parse_node(self, response, node):
        item = RssSpiderItem()

        title = node.select("title/text()").extract()[0]
        link = node.select("link/text()").extract()[0]
        cursor.execute("select * from rss_items where link =%s", (link))
        link_exists = cursor.fetchone()
        if link_exists:
            item["is_pass"] = True
        else:
            item["is_pass"] = False
            try:
                desc = node.select("description/text()").extract()[0]
            except:
                desc = ""
            pubDate = node.select("pubDate/text()").extract()[0]
            try:
                category = node.select("category/text()").extract()[0]
            except:
                category = ""
            try:
                source = node.select("source/text()").extract()[0]
            except:
                source = ""
            try:
                summary = node.select("summary/text()").extract()[0]
            except:
                summary = ""
            try:
                content = node.select("content/text()").extract()[0]
            except:
                content = ""

            item["current_url"] = response.url
            item["title"] = title
            item["link"] = link
            item["desc"] = desc
            item["pubDate"] = pubDate
            item["category"] = category
            item["source"] = source
            item["summary"] = summary

            if content == "":
                try:
                    stream = urllib2.urlopen(link)
                    body = stream.read()
                    response = HtmlResponse(url=link.encode("utf-8"), body=body)

                    hxs = HtmlXPathSelector(response)
                    sample = "".join([sentence if len(sentence) > 50 else "" for sentence in hxs.select("//body//p/text()|//body//div/text()").extract()])

                    text = sample.split("\n")
                    text.sort(key=len)

                    item["content"] = text[-1]
                except:
                    item["content"] = ""
            else:
                item["content"] = content

        return item
