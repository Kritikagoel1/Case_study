from abc import ABC, abstractmethod
from datetime import datetime

from Util.dbconnection import connect



class IAdminService(ABC):
    @abstractmethod
    def GetAdminById(self, admin_id):
        pass
    @abstractmethod
    def GetAdminByUsername(self, username):
        pass
    @abstractmethod
    def RegisterAdmin(self, admin_data):
        pass
    @abstractmethod
    def UpdateAdmin(self, admin_data):
        pass
    @abstractmethod
    def DeleteAdmin(self, admin_id):
        pass


class AdminService(IAdminService):
    def __init__(self):
        self.c = connect()
        self.c.connection()

    def GetAdminById(self, admin_id=None):
            admin_id = int(input("Enter admin ID: "))
            stmt = self.c.cursor

            select_str = 'SELECT * FROM admin WHERE AdminID = %s'
            stmt.execute(select_str, (admin_id,))

            data = stmt.fetchall()
            for p in data:
                print(p)



    def GetAdminByUsername(self, username=None):
        username = input("Enter admin username: ")
        stmt = self.c.cursor

        select_str = 'SELECT * FROM admin WHERE FirstName = %s'
        stmt.execute(select_str, (username,))

        data = stmt.fetchall()
        for p in data:
            print(p)

    def RegisterAdmin(self):
        admin_id = int(input("Enter admin ID: "))
        first_name = input("Enter admin first name: ")
        last_name = input("Enter admin last name: ")
        email = input("Enter admin email: ")
        phone_number = input("Enter admin phone number: ")
        username = input("Enter admin username: ")
        password = input("Enter admin password: ")
        role = input("Enter admin role: ")
        join_date = input("Enter admin join date (YYYY-MM-DD HH:mm:ss): ")

        stmt = self.c.cursor

        insert_str = '''
            INSERT INTO admin (AdminID, FirstName, LastName, Email, PhoneNumber, Username, Password, Role, JoinDate)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        '''
        join_date = datetime.strptime(join_date, "%Y-%m-%d %H:%M:%S")

        admin_values = (
            admin_id, first_name, last_name, email, phone_number, username, password, role, join_date
        )

        stmt.execute(insert_str, admin_values)
        self.c.conn.commit()
        print("Admin registered successfully.")

    def UpdateAdmin(self):
        id = int(input("enter vehicle id you want to update: "))
        field_to_update = input("enter the field you want to update: ")
        new = input("enter new value: ")
        stmt = self.c.cursor
        update_str = f"update admin set {field_to_update}= %s where AdminID= %s"
        data = (new, id)
        stmt.execute(update_str, data)
        c.conn.commit()
        print("updated succesfully")

    def DeleteAdmin(self, admin_id=None):
        admin_id = int(input("Enter admin ID you want to delete: "))
        stmt = self.c.cursor

        delete_str = 'DELETE FROM admin WHERE AdminID = %s'
        stmt.execute(delete_str, (admin_id,))
        c.conn.commit()
        print("Admin deleted successfully.")
'''
ad=AdminService()
ad.GetAdminById()
ad.GetAdminByUsername()
ad.RegisterAdmin()
ad.UpdateAdmin()
ad.DeleteAdmin()
'''
