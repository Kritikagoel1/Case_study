from Util.dbconnection import connect
c=connect()
c.connection()
class AuthenticationService:
    @staticmethod
    def authenticate():
        firstname = input("Enter username: ")
        password= input("Enter password: ")
        try:
            stmt = c.cursor
            select_str = 'SELECT * FROM customer WHERE FirstName = %s AND password = %s'
            stmt.execute(select_str, (firstname, password))
            user = stmt.fetchall()
            if user:
                print("Authentication successful.")
                return True
            else:
             print("Authentication failed. Invalid username or password.")
            return False
        except Exception as e:
            print(f"could not authenticate {e} ")
            return False

auth_service = AuthenticationService()
auth_service.authenticate()
