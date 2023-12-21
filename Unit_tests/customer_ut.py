import unittest
class CarRentalSystemTests(unittest.TestCase):
   def test_updating_customer_information(self):
    from Dao.Customerservice import CustomerService
    customer_service = CustomerService()
    is_updated = customer_service.update_customer()
    self.assertTrue(is_updated)


if __name__ == '__main__':
    unittest.main()