import unittest
class CarRentalSystemTests(unittest.TestCase):

    def test_adding_new_vehicle(self):
        from Dao.VehicleService import VehicleService
        vehicle_service = VehicleService()
        is_added = vehicle_service.AddVehicle()
        self.assertTrue(is_added)

    def test_updating_vehicle_details(self):
        from Dao.VehicleService import VehicleService
        vehicle_service = VehicleService()
        is_updated = vehicle_service.UpdateVehicle()
        self.assertTrue(is_updated)

    def test_getting_list_of_available_vehicles(self):
        from Dao.VehicleService import VehicleService
        vehicle_service = VehicleService()
        available_vehicles = vehicle_service.GetAvailableVehicles()
        self.assertIsNotNone(available_vehicles)
        self.assertGreater(len(available_vehicles), 0)

    def test_getting_list_of_all_vehicles(self):
        from Dao.VehicleService import VehicleService
        vehicle_service = VehicleService()
        all_vehicles = vehicle_service.GetVehicleById()
        self.assertIsNotNone(all_vehicles)
        self.assertGreater(len(all_vehicles), 0)


if __name__ == '__main__':
    unittest.main()
