from Util.dbconnection import connect
c=connect()
c.connection()

class InvalidInputException(Exception):
    def __init__(self, field_name, message="Invalid input for field."):
        self.field_name = field_name
        super().__init__(f"{message} Field: {field_name}")

class CustomerService:
    def validate_email(self, email):

        if not "." or "@" not in email:
            raise InvalidInputException("Email", "Invalid email format.")

    def get_customer_by_email(self, email=None):
        try:
            email = input("Enter customer email: ")
            self.validate_email(email)


            stmt = c.cursor
            select_str = f'''SELECT * FROM customer WHERE Email = %s'''
            stmt.execute(select_str, (email,))
            data = stmt.fetchall()

            if data:
                for p in data:
                    print(p)
            else:
                print("Customer not found.")

        except InvalidInputException as iie:
            print(f"InvalidInputException: {iie}")
        except Exception as e:
            print(f"An error occurred: {e}")

# Usage
customer_service = CustomerService()
customer_service.get_customer_by_email()
