import os
import psycopg2

DATABASE_URL = "os.environ['DATABASE_URL']"


# establish database connection
class MyDatabase():
    def __init__(self):
        pass
        # self.conn = psycopg2.connect(DATABASE_URL, sslmode='require')
        # self.cursor = self.conn.cursor()

my_database = MyDatabase()