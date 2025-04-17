import random
import time

from dateutil.relativedelta import relativedelta
from dateutil.parser import parse
import requests
from bs4 import BeautifulSoup
import pandas as pd
from tools.config import MyMysql
from tools.ua import UaPool

def eastmoney_news_spider(code, time_frame):
    database = MyMysql()
    ua_p = UaPool()
    page = 0
    flag = True
    data_list = []
    # 转换股票代码为东财股吧识别格式
    if code == 'sh000001':
        code = 'zssh000001'
    elif 'sh' in code:
        code = code.replace('sh', '')
    # 存储上一条日期，以经过对比发现年份变化
    last_date_time = None
    for page in range(100):
        while flag:
            page += 1
            url = 'https://guba.eastmoney.com/list,' + str(code) + ',2,f_' + str(page) + '.html'
            ua = ua_p.choose_ua()
            headers = {
                'User-Agent': ua
            }
            try:
                res = requests.get(url, headers=headers, timeout=10).text
            except:
                continue
            bs = BeautifulSoup(res, 'html.parser')
            for div in bs.select('div .report_item'):
                view_num = div.select('.read')[0].string
                comment_num = div.select('.reply')[0].string
                content = div.select('a')[0].string
                date_time = parse(div.select('.pub_time')[0].string)
                print(view_num, comment_num, content,  date_time)
                if not last_date_time:
                    last_date_time = date_time
                    # 若较早发的帖子日期经过格式化后日期晚于较晚发的帖子，则认为年份发生变化
                if last_date_time < date_time:
                    date_time = date_time - relativedelta(years=1)
                data_list.append((code, content, date_time, view_num, comment_num))
            time.sleep(random.randint(20, 30))
            if page > time_frame:
                flag = False
        else:
            break

    df = pd.DataFrame(data_list, columns=['Code', 'Title', 'PublishTime', 'Views', 'Comments'])
    df.to_csv('stock_news' + str(code) +'.csv', index=False)

if __name__ == "__main__":
    eastmoney_news_spider('sz300832', 0)
