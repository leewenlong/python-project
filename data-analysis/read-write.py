# coding: utf-8

import csv


def readEmotions():
    data = [];
    # 余额宝情绪指数，列名为：日期(升序)，每日指数，五日均线
    with open("emotions.txt", 'rb') as file:
        reader = csv.reader(file, delimiter='\t')
        for row in reader:
            data.append(row)
    return data


def writeEmotionsReverse(data):
    data.reverse()
    f = open("emotions-reverse.csv", 'wb')  # 不加b会出现空行
    writer = csv.writer(f)
    length = len(data)
    for i in range(length):
        writer.writerow(data[i])
    f.close()


if __name__ == '__main__':
    writeEmotionsReverse(readEmotions())
