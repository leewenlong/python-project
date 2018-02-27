# coding: utf-8
import csv

from datetime import datetime
import matplotlib.dates as mdate
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

emotions_date = []  # date
emotions_value = []  # 余额宝情绪指数
emotions_value5 = []  # value
szindex_date = []  # date
szindex_value = []  # 上证收盘指数

with open("emotions-reverse.csv", 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        emotions_date.append(row[0])
        emotions_value.append(row[1])
        emotions_value5.append(row[2])

# with open("emotions.txt", 'rb') as file:
#     reader = csv.reader(file, delimiter=' ')
#     for row in reader:
#         #print list(row)
#         _row = row[0].split('\t');
#         date = _row[0];
#         v = _row[1];
#         v5 = _row[2];
#         emotions_date.append(date)
#         emotions_value.append(v)
#         emotions_value5.append(v5)


with open("000001-clip.csv", 'rb') as file:
    reader = csv.reader(file)
    i = 0 # filter head
    for row in reader:
        if i == 0:
            i = 1
        else:
            date = row[0].replace('-', '')
            szindex_date.append(date)
            szindex_value.append(row[3])


def drawDoubleY(x1, y1, x2, y2):
    fig = plt.figure()

    fmt = '%Y%m%d'
    xs1 = [datetime.strptime(k, fmt).date() for k in x1]
    xs2 = [datetime.strptime(k, fmt).date() for k in x2]
    ys1 = y1
    ys2 = y2

    plt.gca().xaxis.set_major_formatter(mdate.DateFormatter(fmt))
    # plt.gca().xaxis.set_major_locator(mdate.MonthLocator())  # 以月为间隔
    fig.autofmt_xdate()


    '''中文字体设置
        1.代码中设置
        2.配置文件中设置Lib/site-packages/matplotlib/mpl-data/matplotlibrc
            设置font.sans-serif,追加需要的中文字体

    '''
    fontfamily = FontProperties(fname=r'c:/windows/fonts/STKAITI.TTF', size=15)  # 硬编码
    plt.title(u'余额宝情绪指数与上证收盘指数叠加图')  # 使用配置文件中的，微软雅黑

    ax1 = fig.add_subplot(111)
    ax1.plot(xs1, ys1, label=u'余额宝情绪指数')
    ax1.set_ylabel(u'余额宝情绪指数', fontproperties=fontfamily)  # 硬编码设置字体
    ax1.legend(loc=2, bbox_to_anchor=(0.01, 0.90))


    ax2 = ax1.twinx()
    ax2.plot(xs2, ys2, 'r', label=u'上证指数')
    ax2.set_ylabel(u'上证指数', fontproperties=fontfamily)
    ax2.legend(loc=2, bbox_to_anchor=(0.01, 0.96))

    # 单条曲线
    # plt.plot(xs, ys1)
    # plt.xlabel('date')
    # plt.ylabel('emotions')

    plt.show()


if __name__ == "__main__":
    drawDoubleY(emotions_date, emotions_value, szindex_date, szindex_value)
