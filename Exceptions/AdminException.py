from Util.dbconnection import connect
c = connect()
c.connection()


class AdminE:
    def GetAdminByUsername(self, username=None):
        try:

            username = input("Enter admin username: ")
            stmt = c.cursor

            select_str = '''SELECT * FROM admin WHERE FirstName = %s'''
            stmt.execute(select_str, (username,))
            data = stmt.fetchall()
            if data:
                for p in data:
                    print(p)
            else:
                print("name not found")

        except Exception as e:
            print(f"error: {e}")


ad = AdminE()
ad.GetAdminByUsername()
