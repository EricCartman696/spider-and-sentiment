import pandas as pd
from news_spider import eastmoney_news_spider
import time
# 读取CSV文件到DataFrame
def main():
    df = pd.read_csv('hs300_stocks.csv')

    # 遍历DataFrame中的每一行
    for index, row in df.iterrows():
        # 提取证券代码
        code = row['code']
        # 调用爬虫函数，这里假设爬取最近1天的数据
        eastmoney_news_spider('code', 1)
        print('finish: %s' % code)
        time.sleep(5)