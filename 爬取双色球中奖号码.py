import requests
import csv

if __name__ == '__main__':

    f = open('双色球中奖号码.csv', mode='a', encoding='gbk', newline='')
    csv_dict_writer = csv.DictWriter(f, fieldnames=['期号',
                                                    '红球1',
                                                    '红球2',
                                                    '红球3',
                                                    '红球4',
                                                    '红球5',
                                                    '红球6',
                                                    '蓝球',
                                                    '蓝球2'])
    csv_dict_writer.writeheader()
    url = 'http://www.cwl.gov.cn/cwl_admin/front/cwlkj/search/kjxx/findDrawNotice'

    params = {
        'name': 'ssq',
        'issueCount': '',
        'issueStart': '',
        'issueEnd': '',
        'pageNo': '1',
        'pageSize': '100000',
        'systemType': 'PC'
    }

    headers = {
        'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
        'Accept': '*/*',
        'Host': 'www.cwl.gov.cn',
        'Connection': 'keep-alive',
        'Cookie': 'HMF_CI=b62c915bfddfa8a54118206293525de10ccd6b4e4f21e9add0af59d75b6be239f2ddba52eac361b7a1db0668234c1d16dcc8f555f9da1a1e93f272cbc345a97d17'
    }

    response = requests.get(url=url, params=params, headers=headers)
    result = response.json()['result']
    for r in result:
        red__split = r['red'].split(',')
        dit = {
            '期号': r['code'],
            '红球1': red__split[0],
            '红球2': red__split[1],
            '红球3': red__split[2],
            '红球4': red__split[3],
            '红球5': red__split[4],
            '红球6': red__split[5],
            '蓝球': r['blue'],
            '蓝球2': r['blue2']
        }
        csv_dict_writer.writerow(dit)
