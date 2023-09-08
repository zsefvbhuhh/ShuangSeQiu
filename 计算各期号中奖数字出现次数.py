import csv
from collections import Counter

if __name__ == '__main__':
    f = open('双色球中奖号码.csv', 'r')
    with f:
        reader = csv.reader(f)
        redList = list()
        blueList = list()
        next(reader)
        for row in reader:
            redList.append(row[1])
            redList.append(row[2])
            redList.append(row[3])
            redList.append(row[4])
            redList.append(row[5])
            redList.append(row[6])
            blueList.append(row[7])
            if row[8] != '':
                blueList.append(row[8])
    redCounter = dict(Counter(redList))
    blueCounter = dict(Counter(blueList))
    b = open('双色球中奖号码出现次数.csv', mode='a', encoding='gbk', newline='')
    csv_dict_writer = csv.DictWriter(b, fieldnames=['红球中奖号码',
                                                    '出现次数1',
                                                    '蓝球中奖号码',
                                                    '出现次数2'])
    csv_dict_writer.writeheader()

    for key, value in redCounter.items():
        dit1 = {
            '红球中奖号码': key,
            '出现次数1': value,
        }
        csv_dict_writer.writerow(dit1)

    for key, value in blueCounter.items():
        dit2 = {
            '蓝球中奖号码': key,
            '出现次数2': value,
        }
        csv_dict_writer.writerow(dit2)
