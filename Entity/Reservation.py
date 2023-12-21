from datetime import datetime
class Reservation:
    def __init__(self, reservation_id, customer_id, vehicle_id, start_date, end_date, total_cost, status):
        self.ReservationID = reservation_id
        self.CustomerID = customer_id
        self.VehicleID = vehicle_id
        self.StartDate = start_date
        self.EndDate = end_date
        self.TotalCost = total_cost
        self.Status = status

    def calculate_total_cost(self, daily_rate):
        try:

                duration = (self.EndDate - self.StartDate).days


                if duration >= 0 and daily_rate >= 0:
                    self.TotalCost = daily_rate * duration
                else:

                    raise ValueError("Invalid duration or daily rate")

        except:
            print(f"Error calculating total cost")

reservation = Reservation(
        reservation_id=int(input("enter reservation id: ")),
        customer_id=int(input("enter customer id: ")),
        vehicle_id=int(input(" enter vehicle id: ")),
        start_date=datetime(input("enter start date in yy-mm-dd format")),
        end_date=datetime(input("enter end date in yy-mm-dd format")),
        total_cost=float(input("enter total cost")),
        status=input("enter status")
    )

daily_rate = float(input("Enter the daily rate for the reservation: "))

reservation.calculate_total_cost(daily_rate)

print("Reservation ID:", reservation.ReservationID)
print("Customer ID:", reservation.CustomerID)
print("Vehicle ID:", reservation.VehicleID)
print("Start Date:", reservation.StartDate)
print("End Date:", reservation.EndDate)
print("Total Cost:", reservation.TotalCost)
print("Status:", reservation.Status)