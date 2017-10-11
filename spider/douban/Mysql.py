# -*- coding: utf-8 -*-
import MySQLdb

def connect():
    return MySQLdb.connect(
        host='10.128.106.153',
        port = 3306,
        user='root',
        passwd='oneapm_si',
        db ='python_zhihu',
        charset="utf8")


def insert(item):
    conn = connect()
    cur = conn.cursor()
    sql = "insert into topic_answer values(%s,%s,%s,%s)"
    value = (item['answer_url'],item['question'],item['author'],item['author_url'])

    cur.execute(sql,value)
    cur.close()
    conn.commit()
    conn.close()