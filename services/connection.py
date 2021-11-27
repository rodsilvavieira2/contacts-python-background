from mysql.connector import connect


class Connection:
    def __init__(self):
        self.connection = connect(
            host="localhost",
            port=3306,
            user="root",
            password="123456",
            database="contacts"
        )
