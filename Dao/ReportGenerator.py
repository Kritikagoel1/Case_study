from Util.dbconnection import connect

class ReportGenerator:
    def __init__(self):
        self.c = connect()
        self.c.connection()


    def generate_reservation_report(self):
        print("report from reservation")
        stmt = self.c.cursor
        select_str = 'SELECT * FROM reservation'
        stmt.execute(select_str)
        data = stmt.fetchall()
        for p in data:
            print(p)


    def generate_vehicle_report(self):
        print("report from vehicles")
        stmt = self.c.cursor
        select_str = 'SELECT * FROM vehicle'
        stmt.execute(select_str)
        data = stmt.fetchall()
        for p in data:
            print(p)


