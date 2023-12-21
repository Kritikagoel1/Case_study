from datetime import datetime

class Customer:
    def __init__(self, customer_id, first_name, last_name, email, phone_number, address, username, password, registration_date):
        self.CustomerID = customer_id
        self.FirstName = first_name
        self.LastName = last_name
        self.Email = email
        self.PhoneNumber = phone_number
        self.Address = address
        self.Username = username
        self.Password = password
        self.RegistrationDate = registration_date

    def authenticate(self, entered_password):

        return self.Password == entered_password

c=Customer(
    customer_id=int(input("enter customer id: ")),
    first_name=input("enter first name: "),
    last_name=input("enter last name"),
    email=input("enter email:"),
    phone_number=input("enter phone number"),
    address=input("enter address"),
    username=input("enter user name: "),
    password=input("enter password: "),
    registration_date=datetime.now()
)
entered_password = input("Enter your password: ")
is_authenticated = c.authenticate(entered_password)

if is_authenticated:
    print("Authentication successful!")
else:
    print("Authentication failed.")
