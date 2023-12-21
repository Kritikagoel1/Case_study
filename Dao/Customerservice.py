from abc import ABC, abstractmethod
from datetime import datetime

from Util.dbconnection import connect


class ICustomerService(ABC):
    @abstractmethod
    def get_customer_by_id(self, customer_id):
        pass

    @abstractmethod
    def get_customer_by_username(self, username):
        pass

    @abstractmethod
    def  register_customer(self, customer_data):
        pass

    @abstractmethod
    def update_customer(self, customer_data):
        pass

    @abstractmethod
    def delete_customer(self, customer_id):
        pass

class CustomerService(ICustomerService):
    def __init__(self):
        self.c = connect()
        self.c.connection()

    def get_customer_by_id(self, customer_id=None):
        customer_id=int(input("enter customer id: "))
        stmt=self.c.cursor
        select_str=f'''select * from customer where CustomerID={customer_id}'''
        stmt.execute(select_str)
        data=stmt.fetchall()
        for p in data:
            print(p)

    def get_customer_by_username(self, name=None):
        name=input("enter first name: ")
        stmt=self.c.cursor
        select_str=f'''select * from customer where FirstName= '{name}' '''
        stmt.execute(select_str)
        data = stmt.fetchall()
        for p in data:
            print(p)

    def register_customer(self):
        cust_id=int(input("enter customer id: "))
        first_name = input("Enter First Name: ")
        last_name = input("Enter Last Name: ")
        email=input("enter email")
        phone_number = input("Enter Phone Number: ")
        address = input("Enter Address: ")
        username = input("Enter Username: ")
        password = input("Enter Password: ")
        registration_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


        stmt=self.c.cursor

        create_insert='''insert into customer (CustomerID,FirstName, LastName, Email, PhoneNumber, Address, 
        Username, Password, RegistrationDate) values ( %s,%s,%s,%s,%s,%s,%s,%s,%s)'''
        data=(cust_id,first_name,last_name,email,phone_number,address,username,password,registration_date)
        stmt.execute(create_insert,data)
        print("inserted successfuly")

    def update_customer(self):
        id=int(input("enter customer id you want to update: "))
        field_to_update=input("enter the field you want to update: ")
        new=input("enter new value: ")
        stmt=self.c.cursor
        update_str=f"update customer set {field_to_update}= %s where CustomerID= %s"
        data=(new,id)
        stmt.execute(update_str,data)
        self.c.conn.commit()
        print("updated succesfully")

    def delete_customer(self, customer_id=None):
        customer_id=int(input("enter customer id you want to delete: "))
        stmt=self.c.cursor
        delete_str=f''' delete from customer where CustomerID={customer_id}'''
        stmt.execute(delete_str)
        c.conn.commit()
        print("deleted successfully")

'''
cs=CustomerService()
cs.get_customer_by_id()
cs.get_customer_by_username()
cs.register_customer()
cs.update_customer()
cs.delete_customer()
'''
