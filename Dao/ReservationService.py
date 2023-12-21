from abc import ABC, abstractmethod
from datetime import datetime
from Util.dbconnection import connect


class IReservationService(ABC):
    @abstractmethod
    def GetReservationById(self, reservation_id):
        pass
    def GetReservationsByCustomerId(self, customer_id):
        pass

    def CreateReservation(self,reservation_data):
        pass

    def UpdateReservation(self, reservation_data):
        pass

    def CancelReservation(self, reservation_id):
        pass


class ReservationService(IReservationService):
    def __init__(self):
        self.c = connect()
        self.c.connection()
    def GetReservationById(self, reservation_id=None):
        reservation_id = int(input("Enter reservation ID: "))
        stmt = self.c.cursor

        select_str = 'SELECT * FROM reservation WHERE ReservationID = %s'
        stmt.execute(select_str, (reservation_id,))

        data = stmt.fetchall()
        for p in data:
            print(p)

    def GetReservationsByCustomerId(self, customer_id=None):
        customer_id = int(input("Enter customer ID: "))
        stmt = self.c.cursor

        select_str = 'SELECT * FROM reservation WHERE CustomerID = %s'
        stmt.execute(select_str, (customer_id,))

        data = stmt.fetchall()
        for p in data:
            print(p)

    def CreateReservation(self):
        customer_id = int(input("Enter customer ID: "))
        vehicle_id = int(input("Enter vehicle ID: "))
        start_date = input("Enter start date and time (YYYY-MM-DD HH:mm:ss): ")
        end_date = input("Enter end date and time (YYYY-MM-DD HH:mm:ss): ")
        total_cost = float(input("Enter total cost: "))
        status = input("Enter status: ")

        stmt = self.c.cursor

        insert_str = '''INSERT INTO reservation (CustomerID, VehicleID, StartDate, EndDate, TotalCost, Status) 
                     VALUES (%s, %s, %s, %s, %s, %s)'''
        reservation_values = (customer_id, vehicle_id, start_date, end_date, total_cost, status)
        stmt.execute(insert_str, reservation_values)
        c.conn.commit()
        print("Reservation created successfully.")

    def UpdateReservation(self):
        id = int(input("enter vehicle id you want to update: "))
        field_to_update = input("enter the field you want to update: ")
        new = input("enter new value: ")
        stmt = self.c.cursor
        update_str = f"update reservation set {field_to_update}= %s where ReservationID= %s"
        data = (new, id)
        stmt.execute(update_str, data)
        c.conn.commit()
        print("updated succesfully")

    def CancelReservation(self, reservation_id=None):
        reservation_id = int(input("Enter reservation ID you want to cancel: "))
        stmt = self.c.cursor

        delete_str = 'DELETE FROM reservation WHERE ReservationID = %s'
        stmt.execute(delete_str, (reservation_id,))
        c.conn.commit()
        print("Reservation canceled successfully.")
'''
res=ReservationService()
res.GetReservationById()
res.GetReservationsByCustomerId()
res.CreateReservation()
res.UpdateReservation()
res.CancelReservation()
'''
