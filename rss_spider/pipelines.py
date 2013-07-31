# _*_ coding: utf-8 _*_
# author zhaowei

import sys
from datetime import datetime
from datetime import date

from twisted.enterprise import adbapi
from twisted.python import log
import MySQLdb.cursors

from settings import HOST, DB, USER, PASSWD


class SQLStorePipeline(object):
    def __init__(self):
        self.dbpool = adbapi.ConnectionPool("MySQLdb", host=HOST, db=DB, user=USER, passwd=PASSWD, cursorclass=MySQLdb.cursors.DictCursor, charset="utf8", use_unicode=True)

    def process_item(self, item, spider):
        query = self.dbpool.runInteraction(self.conditional_insert, item)
        query.addErrback(self.handle_error)
        return item

    def conditional_insert(self, tx, item):
        # if url_exists
        if item["is_pass"]:
            pass
        else:
            tx.execute("select id from rss_urls where link = %s", (item["current_url"]))
            result = tx.fetchone()
            if not result:
                pass
            else:
                reload(sys)
                sys.setdefaultencoding("utf-8")

                tx.execute("insert into rss_items (rss_urls_id, link, title, description, pubDate, category, source, summary, content, add_time, add_date) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (int(result["id"]), item["link"], item["title"], item["desc"], item["pubDate"], item["category"], item["source"], item["summary"], item["content"], datetime.now(), date.today()))

    def close_spider(self, spider):
        pass
        # spider.log("spider done")

    def handle_error(self, e):
        log.err(e)
