import pandas as pd
from dict_analysis import DictAnalysis
# 1. 读取 Excel 文件
excel_path = 'E:/股吧文本/分析师/2020-2024.xlsx'  # 替换为你的文件路径
data = pd.read_excel(excel_path)

# 确保 Summary 列是字符串类型
data['Summary'] = data['Summary'].astype(str)

# 2. 初始化 DictAnalysis 类
# 根据需求选择合适的情感词典类型（例如 'news' 或'guba'）
text_type = 'news'  # 或其他类型
sentiment_analyzer = DictAnalysis(text_type)

# 3. 计算每行文本的情感得分
def calculate_sentiment_score(row):
    summary = row['Summary']
    score = sentiment_analyzer.sentiment_score(summary)
    return score

# 应用函数计算情感得分
data['SentimentScore'] = data.apply(calculate_sentiment_score, axis=1)

# 4. 查看结果
print(data[['Summary', 'SentimentScore']])

# 可选：保存结果到新的 Excel 文件
data.to_excel('sentiment_scores2020-2024.xlsx', index=False)