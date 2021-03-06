# author: zhaowei

BOT_NAME = 'rss_spider'

SPIDER_MODULES = ['rss_spider.spiders']
NEWSPIDER_MODULE = 'rss_spider.spiders'

ITEM_PIPELINES = ['rss_spider.pipelines.SQLStorePipeline']

HOST = "localhost"
DB = "world_rss"
USER = ""
PASSWD = ""

DOWNLOAD_DELAY = 1

CONCURRENT_ITEMS = 100
CONCURRENT_REQUESTS = 16
CONCURRENT_REQUESTS_PER_DOMAIN = 8
CONCURRENT_REQUESTS_PER_IP = 0

DEPTH_LIMIT = 0
DEPTH_PRIORITY = 0
DNSCACHE_ENABLED = True

AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 3.0
AUTOTHROTTLE_CONCURRENCY_CHECK_PERIOD = 10

COOKIES_ENABLED = False
