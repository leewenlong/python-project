# coding: utf-8

import csv
import matplotlib.pyplot as plt
from datetime import datetime as dt
import matplotlib.dates as md
import pandas as pd
from datetime import timedelta as td


def read():
    dates = []
    values = []
    with open('000001-clip.csv', 'rb') as f:
        lines = csv.reader(f)
        for row in lines:
            dates.append(row[0])  # 日期
            values.append(row[8])  # 涨跌额
    return dates, values


# data = read()
# x = [i for i in data[0]]
# x.pop(0)
# y = [i for i in data[1]]
# y.pop(0)

def draw_bar():
    data = pd.read_csv('000001-clip-1.csv', encoding='utf-8')
    x = data[u'日期'].T.values
    y = data[u'涨跌额'].T.values

    fmt = '%Y-%m-%d'
    fig = plt.figure()
    plt.gca().xaxis.set_major_formatter(md.DateFormatter(fmt))
    fig.autofmt_xdate()

    x = [dt.strptime(k, fmt).date() for k in x]
    color_list = []
    for i in y:
        if i > 0:
            color_list.append('r')
        else:
            color_list.append('g')
    plt.bar(x, y, color=color_list)
    plt.show()


# 按时间序列分组汇总
def draw_bar_month():
    data = pd.read_csv('000001-clip-1.csv', encoding='utf-8')
    data.index = pd.to_datetime(data[u'日期'])  # 索引设置为日期格式数据列
    data = data.groupby(pd.Grouper(freq='M'))  # 按月累加
    data = data.sum()

    x = data.index.values
    y = data[u'涨跌幅'].values

    plt.gca().xaxis.set_major_formatter(md.DateFormatter('%Y-%m'))
    plt.gca().xaxis.set_major_locator(md.MonthLocator())  # 以月为间隔
    color_list = []
    for i, j in zip(x, y):
        if j > 0:
            color_list.append('r')
            plt.text(i, j, '%.2f' % j, va='bottom', ha='center', size=8)  # 柱状图上添加数字
        else:
            color_list.append('g')
            plt.text(i, j, '%.2f' % j, va='top', ha='center', size=8)

    plt.bar(x, y, color=color_list, width=20)
    plt.xlabel(u'月份')
    plt.ylabel(u'上证指数涨跌幅度')
    plt.title(u'上证指数月度涨跌幅度')
    plt.xticks(rotation=60)
    plt.show()


# 按时间序列分组汇总双柱图
def draw_double_bar_month():
    data = pd.read_csv('000001-clip-1.csv', encoding='utf-8')
    data.index = pd.to_datetime(data[u'日期'])  # 索引设置为日期格式数据列
    data = data.groupby(pd.Grouper(freq='M'))  # 按月累加
    data = data.sum()

    x = data.index.values
    y1 = data[u'涨跌幅'].values
    y2 = data[u'涨跌额'].values
    plt.gca().xaxis.set_major_formatter(md.DateFormatter('%Y-%m'))
    plt.gca().xaxis.set_major_locator(md.MonthLocator())  # 以月为间隔

    g = (x[1] - x[0]) / 2  # 间隔

    color_list1 = []
    color_list2 = []
    for i, j, k in zip(x, y1, y2):
        if j > 0:
            color_list1.append('r')
            color_list2.append('cyan')
            plt.text(i - g, j, '%.2f' % j, va='bottom', ha='center', size=8)  # 柱状图上添加数字
            plt.text(i, k, '%.2f' % k, va='bottom', ha='center', size=8)  # 柱状图上添加数字
        else:
            color_list1.append('g')
            color_list2.append('blue')
            plt.text(i - g, j, '%.2f' % j, va='top', ha='center', size=8)
            plt.text(i, k, '%.2f' % k, va='top', ha='center', size=8)

    plt.bar(x - g, y1, color=color_list1, width=10)
    plt.bar(x, y2, color=color_list1, width=10)

    plt.xlabel(u'月份')
    plt.ylabel(u'上证指数涨跌幅度')
    plt.title(u'上证指数涨跌幅度与点数图')
    plt.xticks(rotation=45)
    plt.show()


# 汇总每个月份涨跌个数
def draw_bar_month_count():
    data = pd.read_csv('000001-clip-1.csv', encoding='utf-8')
    data.index = pd.to_datetime(data[u'日期'])  # 索引设置为日期格式数据列
    data = data.groupby(pd.Grouper(freq='M'))  # 按月累加

    x = []#时间序列
    y1 = []#上涨个数
    y2 = []#下跌个数
    for i in data[u'涨跌幅']:
        x.append(pd.Timestamp(i[0]).to_pydatetime())
        up = 0
        down = 0
        for j in i[1]:
            if j >= 0:
                up += 1
            else:
                down += 1
        y1.append(up)
        y2.append(down)

    plt.gca().xaxis.set_major_formatter(md.DateFormatter('%Y-%m'))
    plt.gca().xaxis.set_major_locator(md.MonthLocator())#以月为间隔

    g = (x[1] - x[0]) / 2  # 间隔
    x1 = []
    x2 = []
    for i in x:
        x1.append(i - g / 6)
        x2.append(i + g / 2)
    for i, j in zip(x1, y1):
        plt.text(i, j, j, va='bottom', ha='center', size=8)  # 柱状图上添加数字

    for i, j in zip(x2, y2):
        plt.text(i, j, j, va='bottom', ha='center', size=8)  # 柱状图上添加数字

    plt.bar(x1, y1, color='r', width=10, label=u'上涨天数')
    plt.bar(x2, y2, color='g', width=10, label=u'下跌天数')
    plt.legend(loc='upper right')


    plt.xlabel(u'月份')
    plt.ylabel(u'上证指数涨跌个数')
    plt.title(u'上证指数月度涨跌天数')
    plt.xticks(rotation=45)
    plt.show()


if __name__ == '__main__':
    # draw_bar()
    # draw_bar_month()
    # draw_double_bar_month()
    draw_bar_month_count()
