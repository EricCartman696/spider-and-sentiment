import pymysql


class MyMysql:
    def __init__(self):
        self.connect = pymysql.connect(
            host = '127.0.0.1',
            port=3306,
            user='root',
            password='123456',
            database='DEMO',
            charset='utf8'
        )
        self.cursor = self.connect.cursor()

