# coding: utf-8
import csv

from datetime import datetime
import matplotlib.dates as mdate
import matplotlib.pyplot as plt

emotions_date = []  # date
emotions_value = []
emotions_value5 = []
szindex_date = []  # date
szindex_value = []

with open("emotions.txt", 'rb') as file:
    reader = csv.reader(file, delimiter=' ')
    for row in reader:
        #        print list(row)
        _row = row[0].split('\t');
        date = _row[0];
        v = _row[1];
        v5 = _row[2];
        emotions_date.append(date)
        emotions_value.append(v)
        emotions_value5.append(v5)

with open("000001-clip.csv", 'rb') as file:
    reader = csv.reader(file)
    for row in reader:
        date = row[0].replace('-', '')
        if date.isdigit():
            szindex_date.append(date)
            szindex_value.append(row[3])


def drawMutilLine(x1, y1, x2, y2):
    fig = plt.figure()
    fmt = '%Y%m%d'
    xs1 = [datetime.strptime(k, fmt).date() for k in x1]
    xs2 = [datetime.strptime(k, fmt).date() for k in x2]
    ys1 = y1
    ys2 = y2

    plt.gca().xaxis.set_major_formatter(mdate.DateFormatter(fmt))
    # plt.gca().xaxis.set_major_locator(DateFormatter(fmt))
    fig.autofmt_xdate
    plt.title(u'余额宝情绪指数与上证收盘指数叠加图')  # 使用微软雅黑

    plt.plot(xs1, ys1, label=u'余额宝情绪指数')
    plt.plot(xs2, ys2, 'r', label=u'上证指数')

    plt.legend()
    # 单条曲线
    # plt.plot(xs, ys1)
    # plt.xlabel('date')
    # plt.ylabel('emotions')

    plt.show()


if __name__ == "__main__":
    drawMutilLine(emotions_date, emotions_value, szindex_date, szindex_value)
