
# financial-spider-data-analysis
# 金融爬虫与数据分析
本项目功能为爬取股票的股吧舆论数据，作情感分析与数据分析后，以供因子挖掘使用。


## 使用方法
### 本地运行

在执行程序前，需要在以下文件中配置相关参数：
- tools/config.py
```
import pymysql  
  
class MyMysql:  
    def __init__(self):  
        self.connect = pymysql.connect(  
			host=Mysql服务IP地址,  
            port=Mysql数据库端口,  
			user=数据库用户名,  
            password=数据库密码,  
            database=数据库名,  
            charset='utf8'  
        )  
        self.cursor = self.connect.cursor()
```

其中，数据库ua_pool为用于生成随机请求头user_agent的库，需要在建立完成数据库后导入位于文件根目录下的```ua_pool.sql```文件数据。

代码所需数据存放在网盘中，链接为https://pan.baidu.com/s/1PRUdM8xaUb0Jb4TsfLZkXg 提取码为f589
下载后放在项目根目录即可
在完成上述配置后，运行```main.py```即可自动开始爬取分析，并生成情感得分。
