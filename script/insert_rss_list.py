# _*_ coding: utf-8 _*_
# author: zhaowei

# just insert into the database when the rss_urls is empty
from datetime import datetime

import MySQLdb as mysql

from config import USER, PASSWD, DB, HOST


def read_file(file_name):
    with open(file_name) as f:
        all_info = f.readlines()
        return all_info


# str => list
def manage_info(info):
    results = []
    for i in info:
        i = i.strip()
        if i not in results:
            results.append(i)
    return results


# list -> dtabase
def insert_into_database(info_list):
    conn = mysql.connect(host=HOST, user=USER, passwd=PASSWD, db=DB, charset="utf8")
    cursor = conn.cursor()
    for i in info_list:
        try:
            cursor.execute("insert into rss_urls(link, add_time) values('%s', '%s')" % (i, datetime.now()))
        except:
            print "error"
    conn.commit()
    conn.close()


if __name__ == "__main__":
    info = read_file("rss_list_init.txt")
    res = manage_info(info)
    insert_into_database(res)
