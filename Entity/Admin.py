from datetime import datetime

class Admin:
    def __init__(self, admin_id, first_name, last_name, email, phone_number, username, password, role, join_date):
        self.AdminID = admin_id
        self.FirstName = first_name
        self.LastName = last_name
        self.Email = email
        self.PhoneNumber = phone_number
        self.Username = username
        self.Password = password  # Should be securely hashed
        self.Role = role
        self.JoinDate = join_date

    def authenticate(self, entered_password):
        # Implement authentication logic (compare hashed passwords, etc.)
        return self.Password == entered_password

# Example usage:

# Create an admin
admin = Admin(
    admin_id=int(input("enter admin id: ")),
    first_name=input('enter first name:'),
    last_name=input('enter last name: '),
    email=input("enter email: "),
    phone_number=input('enter phone no'),
    username=input("enter username"),
    password=input("enter password"),
    role=input("enter role: "),
    join_date=datetime.now()
)

# Authenticate the admin
entered_password = input("Enter your password: ")
is_authenticated = admin.authenticate(entered_password)

if is_authenticated:
    print("Authentication successful!")
else:
    print("Authentication failed.")
