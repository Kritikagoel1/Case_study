import mysql.connector as sql
class connect:
    def __init__(self):
        self.conn=None
        self.cursor = None

    def connection(self):
        host=input("enter host: ")
        user=input("enter user name: ")
        password=input("enter password: ")
        database=input("enter database name: ")

        self.conn=sql.connect(host=host,user=user,password=password,database=database)
        self.cursor=self.conn.cursor()

        try:
            if self.conn.is_connected():
              print("database is connected")
        except:
            print("can't connect to database")



