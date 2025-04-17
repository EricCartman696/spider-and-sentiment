from spider.news_spider import eastmoney_news_spider
import time
import pandas as pd
from sentiment.sentiment_analyzer import SentimentAnalyzer
from datetime import datetime
from sentiment.dict_analysis import DictAnalysis

def main():
    #1.批量爬取一定数量的新闻舆情数据
    df = pd.read_csv('spider/hs300_stocks.csv')
    # 遍历DataFrame中的每一行
    for index, row in df.iterrows():
        # 提取证券代码
        code = row['code']
        # 调用爬虫函数，这里假设爬取最近1天的数据
        eastmoney_news_spider('code', 1)
        print('finish: %s' % code)
        time.sleep(5)
    #2.爬取单只股票的文本数据,参数分别为股票代码和页码
    #eastmoney_news_spider('sz300832', 0)

    # 3.词典法进行情感分析
    # 初始化情感分析器
    analyzer = SentimentAnalyzer(text_type='news')  # 根据需要选择类型

    # 分析Excel文件
    input_path = 'data/2020-2024.xlsx'
    output_path = 'sentiment_scores2020-2024.xlsx'

    # 执行分析
    result_df = analyzer.analyze_excel(input_path, output_path)

    # 打印部分结果
    print(result_df[['Summary', 'SentimentScore']].head())


if __name__ == '__main__':
    print(datetime.now())
    main()
    print(datetime.now())

