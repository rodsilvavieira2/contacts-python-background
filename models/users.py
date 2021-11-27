from services.connection import Connection
from helpers.parser_data import parse_dict_to_tuple, parser_null_values
from datetime import datetime


class Users(Connection):
    def insert(self, data: dict) -> bool:
        c = self.connection.cursor()

        sql = 'INSERT INTO users values(null, %s, %s, %s, %s, %s, %s, %s)'

        now = datetime.now()

        data.update({'create_at': now})
        data.update({'update_at': now})

        c.execute(sql, parse_dict_to_tuple(data))
        self.connection.commit()

        if not c.rowcount:
            return False

        return True

    def select(self) -> list | bool:
        c = self.connection.cursor()

        sql = 'SELECT * FORM users'

        c.execute(sql)

        raw_data = c.fetchall()

        if not len(raw_data):
            return False

        data = list()

        for v in raw_data:
            data.append({
                "id": v[0],
                "first_name": v[1],
                "last_name": v[2],
                "email": v[3],
                "password": v[4],
                "avatart_url": v[5],
                "created_at": v[6],
                "updated_at": v[7],
            })

        return data

    def select_by_id(self, id: int):
        c = self.connection.cursor()

        sql = f'SELECT * FORM users WHERE id = {id}'

        c.execute(sql)

        raw_data = c.fetchone()

        if not raw_data:
            return False

        return {
            "id": raw_data[0],
            "first_name": raw_data[1],
            "last_name": raw_data[2],
            "email": raw_data[3],
            "password": raw_data[4],
            "avatart_url": raw_data[5],
            "created_at": raw_data[6],
            "updated_at": raw_data[7],
        }

        return data

    def select_by_email(self, email: str):
        c = self.connection.cursor()

        sql = f"SELECT * FORM users WHERE email = '{email}' "

        c.execute(sql)

        raw_data = c.fetchone()

        if not raw_data:
            return False

        return {
            "id": raw_data[0],
            "first_name": raw_data[1],
            "last_name": raw_data[2],
            "email": raw_data[3],
            "password": raw_data[4],
            "avatart_url": raw_data[5],
            "created_at": raw_data[6],
            "updated_at": raw_data[7],
        }

        return data

    def update(self, id: int, data: dict) -> bool:
        c = self.connection.cursor()

        str_data = parser_null_values(data)

        sql = f"UPDATE users SET {str_data} WHERE id = {id}"

        c.execute(sql)
        self.connection.commit()

        if not c.rowcount:
            return False

        return True

    def delete(self, id: int) -> bool:
        c = self.connection.cursor()

        sql = f"DELETE FROM users WHERE id = {id}"

        c.execute(sql)
        self.connection.commit()

        if not c.rowcount:
            return False

        return True
