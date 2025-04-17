import pandas as pd
from sentiment.dict_analysis import DictAnalysis


class SentimentAnalyzer:
    def __init__(self, text_type='news'):
        """
        初始化情感分析器
        :param text_type: 情感词典类型 ('news' 或 'guba' 等)
        """
        self.text_type = text_type
        self.analyzer = DictAnalysis(text_type)

    def analyze_excel(self, input_path, output_path=None, text_column='Summary'):
        """
        分析Excel文件中的文本情感
        :param input_path: 输入Excel文件路径
        :param output_path: 输出Excel文件路径(可选)
        :param text_column: 包含文本的列名(默认为'Summary')
        :return: 包含情感得分的数据框
        """
        # 读取Excel文件
        data = pd.read_excel(input_path)

        # 确保文本列是字符串类型
        data[text_column] = data[text_column].astype(str)

        # 计算情感得分
        data['SentimentScore'] = data[text_column].apply(
            lambda text: self.analyzer.sentiment_score(text)
        )

        # 如果提供了输出路径，则保存结果
        if output_path:
            data.to_excel(output_path, index=False)

        return data