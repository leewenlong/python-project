from pymongo import MongoClient
import json
try:
    # Python 3.x
    from urllib.parse import quote_plus
except ImportError:
    # Python 2.x
    from urllib import quote_plus


def conn():
    uri = "mongodb://%s:%s@%s" % (
        quote_plus("root"), quote_plus("password"), "10.128.106.176")
    client = MongoClient(uri)
    db = client.test
    db.authenticate("test","password")
    return db.zhihu


def insert(collect,item):
    # i = json.dumps(item)
    # print i
    collect.insert_one(item)