from Util.dbconnection import connect
c=connect()
c.connection()

class Vehicle:
    def GetVehicleById(self):
        try:
            vehicleid = int(input("enter id"))
            print("vehicle data: ")

            stmt = c.cursor
            select_str = f'''select * from vehicle where VehicleID=%s'''
            stmt.execute(select_str, (vehicleid,))

            data = stmt.fetchall()
            if data:
                for p in data:
                    print(p)
            else:
                print("data not found")



        except Exception as e:
            print(f"Vehicle id not found: {e}")

veh=Vehicle()
veh.GetVehicleById()
