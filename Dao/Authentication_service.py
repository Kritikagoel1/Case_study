from Util.dbconnection import connect
class AuthenticationService:

    def __init__(self):
        self.c = connect()
        self.c.connection()

    def authenticate(self):
        firstname = input("Enter username: ")
        password= input("Enter password: ")

        stmt = self.c.cursor
        select_str = 'SELECT * FROM customer WHERE FirstName = %s AND password = %s'
        stmt.execute(select_str, (firstname, password))

        user = stmt.fetchall()

        if user:
            print("Authentication successful.")
            return True
        else:
            print("Authentication failed. Invalid username or password.")
            return False

'''
auth_service = AuthenticationService()
auth_service.authenticate()
'''
