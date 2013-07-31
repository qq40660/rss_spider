rss_crawl rss爬虫
=========

A crawl for rss websites. The more websites the better.


### requirements:  
python 2.7  
Scrapy==0.16.5  
Twisted==13.1.0  
MySQL-python==1.2.4


### how to use:  
* Create the database via the sql.sql file  

* init the table rss_urls via the script in the script folder:  

        python insert_rss_list.py  
(the rss_list_init.txt file include more then 800 rss links)

* start a scrapy server:

        scrapy server &

* start a spider:

        cd /script
        ./start_spider.py

* stop a spider:

        cd /script
        ./stop_spider.py


### autostart:  
you can autostart the spider, for example:  

        crontab -e
        0 * * * * /home/name/work/rss_spider/script/./start_spider.py
        28 * * * * /home/name/work/rss_spider/script/./stop_spider.py
        30 * * * * /home/name/work/rss_spider/script/./start_spider.py
        58 * * * * /home/name/work/rss_spider/script/./stop_spider.py

(start the spider at 0 and 30 per hour, and stop the spider at 28 and 58 per hour.)


### interface:
I also write a website using clojure for handling the infomation downing from these rss sources. I will open source it some day.





### 如何使用：
* 通过sql.sql这个文件来初始化数据库。

* 通过script文件夹下的脚本来初始化rss_urls这个表。

        python insert_rss_list.py

(rss_list_init.txt这个文件下有超过800个rss链接)

* 开启一个爬虫服务：

        scrapy server &

* 启动一个爬虫:

        cd /script
        ./start_spider.py

* 停止爬虫:

        cd /script
        ./stop_spider.py


### 自启动脚本：

        crontab -e
        0 * * * * /home/name/work/rss_spider/script/./start_spider.py
        28 * * * * /home/name/work/rss_spider/script/./stop_spider.py
        30 * * * * /home/name/work/rss_spider/script/./start_spider.py
        58 * * * * /home/name/work/rss_spider/script/./stop_spider.py


### 界面:

我用clojure写了一个关于对所抓取倒数据操作，展示的网站。近期会对它开源。
