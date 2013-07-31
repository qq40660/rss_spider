#!/usr/bin/env python
# _*_ coding: utf-8 _*_

import subprocess
try:
    from simplejson import json
except:
    import json


# -> list ["422e608f9f28cef127b3d5ef93fe9399", ""]
def list_job_ids(host="http://localhost", port=6800, project="default"):
    command = "curl %s:%d/listjobs.json?project=%s" % (host, port, project)
    command_result = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE).stdout.readline()
    running_ids = json.loads(command_result).get("running")
    ids = []
    for i in running_ids:
        ids.append(i["id"])
    return ids


# str -> list "43242342342354efklajdf14" -> [4234, grep_pid]
def id_to_pid(spider_id):
    command = "ps aux | grep %s | grep -v grep | awk '{print $2}'" % spider_id
    info = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE).stdout.readlines()
    return info


# list -> list ["asdfasdf234234", "a2345asdfaa"] -> [4324, 3453]
def ids_to_pids(spider_ids):
    pids = []
    for i in spider_ids:
        pid = id_to_pid(i)
        pids.extend(pid)
    return pids


# kill 4323
def kill_spider(pid):
    command = "kill -9 %s" % pid
    subprocess.Popen(command, shell=True)


# kill [4324, 4234]
def kill_spider_list(pid_list):
    for i in pid_list:
        kill_spider(i)


if __name__ == "__main__":
    ids = list_job_ids()
    pids = ids_to_pids(ids)
    kill_spider_list(pids)
