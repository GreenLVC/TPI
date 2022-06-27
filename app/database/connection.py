import pymysql


class DataBase:
    def __init__(self):
        self.connection = pymysql.connect(host='localhost',
                                          user='root',
                                          password='1234',
                                          db='myplaylists')

        self.close()

    def close(self):
        self.connection.close()

    def open(self):
        self.connection.connect()
        self.cursor = self.connection.cursor(pymysql.cursors.DictCursor)