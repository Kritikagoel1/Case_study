class Main:
    def mainfunction(self):
        print("Enter 1 for report functions")
        print("Enter 2 for admin")
        print("Enter 3 for authentication")
        print("Enter 4 for customer")
        print("Enter 5 for reservation")
        print("Enter 6 for vehicle")
        ch = input("Enter choice: ")

        if ch == "1":
            from Dao.ReportGenerator import ReportGenerator

            report_generator = ReportGenerator()

            print("1. Generate Reservation Report")
            print("2. Generate Vehicle Report")
            sub_choice = input("Enter sub-choice: ")

            if sub_choice == "1":
                report_generator.generate_reservation_report()
            elif sub_choice == "2":
                report_generator.generate_vehicle_report()
            else:
                print("Invalid sub-choice")

        elif ch == "2":
            print("Enter 1 for GetAdminById")
            print("Enter 2 for GetAdminByUsername")
            print("Enter 3 for RegisterAdmin")
            print("Enter 4 to update admin")
            print("Enter 5 to delete admin")
            choice = input("Enter choice: ")
            from Dao.AdminService import AdminService
            ad = AdminService()

            if choice == "1":
                ad.GetAdminById()
            elif choice == "2":
                ad.GetAdminByUsername()
            elif choice == "3":
                ad.RegisterAdmin()
            elif choice == "4":
                ad.UpdateAdmin()
            elif choice == "5":
                ad.DeleteAdmin()
            else:
                print("Invalid choice")

        elif ch == "3":
            from Dao.Authentication_service import AuthenticationService

            auth_service = AuthenticationService()
            auth_service.authenticate()

        elif ch == "4":
            print("Enter 1 for Get Customer By ID")
            print("Enter 2 for Get Customer By Username")
            print("Enter 3 for Register Customer")
            print("Enter 4 for Update Customer")
            print("Enter 5 for Delete Customer")
            choice = input("Enter choice: ")
            from Dao.Customerservice import CustomerService
            cs = CustomerService()

            if choice == "1":
                cs.get_customer_by_id()
            elif choice == "2":
                cs.get_customer_by_username()
            elif choice == "3":
                cs.register_customer()
            elif choice == "4":
                cs.update_customer()
            elif choice == "5":
                cs.delete_customer()
            else:
                print("Invalid choice")

        elif ch == "5":
            print("Enter 1 for Get Reservation By ID")
            print("Enter 2 for Get Reservations By Customer ID")
            print("Enter 3 for Create Reservation")
            print("Enter 4 for Update Reservation")
            print("Enter 5 for Cancel Reservation")
            choice = input("Enter choice: ")
            from Dao.ReservationService import ReservationService
            res = ReservationService()

            if choice == "1":
                res.GetReservationById()
            elif choice == "2":
                res.GetReservationsByCustomerId()
            elif choice == "3":
                res.CreateReservation()
            elif choice == "4":
                res.UpdateReservation()
            elif choice == "5":
                res.CancelReservation()
            else:
                print("Invalid choice")

        elif ch == "6":
            print("Enter 1 for Get Vehicle By ID")
            print("Enter 2 for Get Available Vehicles")
            print("Enter 3 for Add Vehicle")
            print("Enter 4 for Update Vehicle")
            print("Enter 5 for Remove Vehicle")
            choice = input("Enter choice: ")
            from Dao.VehicleService import VehicleService
            v = VehicleService()

            if choice == "1":
                v.GetVehicleById()
            elif choice == "2":
                v.GetAvailableVehicles()
            elif choice == "3":
                v.AddVehicle()
            elif choice == "4":
                v.UpdateVehicle()
            elif choice == "5":
                v.RemoveVehicle()
            else:
                print("Invalid choice")

        else:
            print("Invalid choice")


m = Main()
m.mainfunction()









