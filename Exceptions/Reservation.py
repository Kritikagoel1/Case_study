from Util.dbconnection import connect
c=connect()
c.connection()
class resrevation():

    def is_vehicle_avail(self, vehicleid):
        stmt=c.cursor
        vehicleid = int(input("enter vehicle id to check: "))
        select_str = 'SELECT Availability FROM vehicle WHERE VehicleID = %s'
        stmt.execute(select_str, (vehicleid,))
        data = stmt.fetchall()
        if data and data[0]:
            return True
        else:
            return False
    def CreateReservation(self):
        try:
            customer_id = int(input("Enter customer ID: "))
            vehicle_id = int(input("Enter vehicle ID: "))
            start_date = input("Enter start date and time (YYYY-MM-DD HH:mm:ss): ")
            end_date = input("Enter end date and time (YYYY-MM-DD HH:mm:ss): ")
            total_cost = float(input("Enter total cost: "))
            status = input("Enter status: ")

            if not self.is_vehicle_avail(vehicle_id):
                print("Vehicle is not available for reservation.")

            stmt = c.cursor

            insert_str = '''INSERT INTO reservation (CustomerID, VehicleID, StartDate, EndDate, TotalCost, Status) 
                                 VALUES (%s, %s, %s, %s, %s, %s)'''
            reservation_values = (customer_id, vehicle_id, start_date, end_date, total_cost, status)
            stmt.execute(insert_str, reservation_values)
            c.conn.commit()
            print("Reservation created successfully.")
        except Exception as e:
            print(f"error in reservation: {e}")

res=resrevation()
res.CreateReservation()
