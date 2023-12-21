class Vehicle:
    def __init__(self,vehicleiD, model, make, year, color, regnum, availability, dailyrate):
        self.Vehicle_Id=vehicleiD
        self.Model = model
        self.Make = make
        self.Year = year
        self.Color = color
        self.Reg_Num = regnum
        self.Availability = availability
        self.DailyRate = dailyrate

veh=Vehicle(
    vehicleiD=int(input("enter vehicle id: ")),
    model=input("enter vehicle model: "),
    make=input("enter model companny: "),
    year=input("enter year of manufacture: "),
    color=input("enter vehicle color: "),
    regnum=input("enter registration number: "),
    availability=input("enter availability of car"),
    dailyrate=float(input("enter daily rate: "))
)

print("Vehicle ID:", veh.Vehicle_Id)
print("Vehicle Model:", veh.Model)
print("Vehicle Company:", veh.Make)
print("Year of manufacture:", veh.Year)
print("Color of Vehicle:", veh.Color)
print("Registration Number of Vehicle:", veh.Reg_Num)
print("Availability of vehicle:", veh.Availability)
print("Daily Rate:", veh.DailyRate)