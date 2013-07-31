#!/usr/bin/env python
# _*_ coding: utf-8 _*_

import subprocess


def start_spider(project="default", host="http://localhost", port=6800, spider="spider_rss"):
    command = "curl %s:%d/schedule.json -d project=%s -d spider=%s &" % (host, port, project, spider)
    subprocess.Popen(command, shell=True)


if __name__ == "__main__":
    start_spider()
