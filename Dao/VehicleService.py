from abc import ABC, abstractmethod
from Util.dbconnection import connect

class IVehicleService(ABC):
    @abstractmethod
    def GetVehicleById(self, vehicleId):
        pass

    @abstractmethod
    def GetAvailableVehicles(self):
        pass

    @abstractmethod
    def AddVehicle(self, vehicleData):
        pass

    @abstractmethod
    def UpdateVehicle(self, vehicleData):
        pass

    @abstractmethod
    def RemoveVehicle(self, vehicleId):
        pass

class VehicleService(IVehicleService):
    def __init__(self):
        self.c = connect()
        self.c.connection()
    def GetVehicleById(self, vehicleid=None):
        vehicleid=int(input("enter id"))
        stmt = self.c.cursor
        select_str = f'''select * from vehicle where VehicleID=%s'''
        stmt.execute(select_str,(vehicleid,))

        data = stmt.fetchall()
        for p in data:
            print(p)

    def GetAvailableVehicles(self):
        availability_input = input("Enter availability (true/false): ").lower()
        availability = availability_input == 'true'
        stmt = self.c.cursor
        select_str = 'SELECT * FROM vehicle WHERE Availability = %s'
        stmt.execute(select_str, (availability,))

        data = stmt.fetchall()
        for p in data:
            print(p)

    def AddVehicle(self):
        try:
            VehicleID = int(input("enter vehicle id: "))
            Model = input("enter model: ")
            Make = input("enter company: ")
            Year = int(input("Enter Year: "))
            Color = input("Enter Color: ")
            RegistrationNumber = input("Enter Registration Number: ")
            Availability = input("Enter Availability (true/false): ").lower() == 'true'
            DailyRate = float(input("Enter Daily Rate: "))

            stmt = self.c.cursor

            create_insert = '''insert into vehicle (VehicleID,Model,Make, Year, Color,RegistrationNumber,Availability,DailyRate)
                    values ( %s,%s,%s,%s,%s,%s,%s,%s)'''
            data = (VehicleID, Model, Make, Year, Color, RegistrationNumber, Availability, DailyRate)
            stmt.execute(create_insert, data)
            self.c.conn.commit()
            print("inserted successfully")

            return True  # Indicate success

        except Exception as e:
            print(f"Error adding vehicle: {e}")
            return False

    def UpdateVehicle(self):
        id = int(input("enter vehicle id you want to update: "))
        field_to_update = input("enter the field you want to update: ")
        new = input("enter new value: ")
        stmt = self.c.cursor
        update_str = f"update vehicle set {field_to_update}= %s where VehicleID= %s"
        data = (new, id)
        stmt.execute(update_str, data)
        self.c.conn.commit()
        print("updated succesfully")

    def RemoveVehicle(self):
        vehicleid = int(input("enter customer id you want to delete: "))
        stmt = self.c.cursor
        delete_str = f''' delete from vehicle where VehicleID={vehicleid}'''
        stmt.execute(delete_str)
        self.c.conn.commit()
        print("deleted successfully")


'''
v=VehicleService()
v.GetVehicleById()
v.GetAvailableVehicles()
v.AddVehicle()
v.UpdateVehicle()
v.RemoveVehicle()
'''




