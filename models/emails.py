from services.connection import Connection
from helpers.parser_data import parse_dict_to_tuple, parser_null_values
from datetime import datetime


class Emails(Connection):
    def insert(self, data: dict) -> bool:
        c = self.connection.cursor()

        sql = 'INSERT INTO emails values(null, %s, %s, %s, %s)'

        now = datetime.now()

        data.update({'create_at': now})
        data.update({'update_at': now})

        c.execute(sql, parse_dict_to_tuple(data))
        self.connection.commit()

        if not c.rowcount:
            return False

        return True

    def select_by_email(self, email: str):
        c = self.connection.cursor()

        sql = f"SELECT * FROM emails WHERE email = '{email}'"

        c.execute(sql)

        raw_data = c.fetchone()

        if not raw_data:
            return False

        return {
            "id": raw_data[0],
            "email": raw_data[1],
            "contact_id": raw_data[2],
            "created_at": raw_data[3],
            "updated_at": raw_data[4],
        }

        return data

    def update(self, id: int, email: str) -> bool:
        c = self.connection.cursor()

        sql = f"UPDATE emails SET email = '{email}' WHERE id = {id}"

        c.execute(sql)
        self.connection.commit()

        if not c.rowcount:
            return False

        return True

    def delete(self, id: int) -> bool:
        c = self.connection.cursor()

        sql = f"DELETE FROM emails WHERE id = {id}"

        c.execute(sql)
        self.connection.commit()

        if not c.rowcount:
            return False

        return True
