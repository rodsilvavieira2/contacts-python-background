from services.connection import Connection
from helpers.parser_data import parse_dict_to_tuple, parser_null_values
from datetime import datetime


class Contacts(Connection):
    def insert(self, data: dict) -> bool:
        c = self.connection.cursor()

        sql = 'INSERT INTO contacts' \
            ' values(null, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'

        now = datetime.now()

        data.update({'create_at': now})
        data.update({'update_at': now})

        c.execute(sql, parse_dict_to_tuple(data))
        self.connection.commit()

        if c.rowcount <= 0:
            return False

        return True

    def select_by_user_id(self, id: int):
        c = self.connection.cursor()

        sql = f'SELECT * FROM contacts as c'\
            ' JOIN phone_types as pt ON pt.id = c.phone_type_id' \
            f" WHERE user_id = {id}"

        c.execute(sql)

        raw_data = c.fetchall()

        if not len(raw_data):
            return False

        data = list()

        for v in raw_data:
            data.append(
                {
                    "id": v[0],
                    "first_name": v[1],
                    "last_name": v[2],
                    "email": v[3],
                    "phone_number": v[4],
                    "phone_type": v[15],
                    "birthday": v[6],
                    "company": v[7],
                    "workload": v[8],
                    "department": v[9],
                    "avatar_url": v[10],
                    "created_at": v[12],
                    "updated_at": v[13],
                })

        return data

    def select_contact_by_id(self, contact_id) -> dict | bool:
        c = self.connection.cursor()

        sql = f'SELECT * FROM contacts WHERE id = {contact_id}'

        c.execute(sql)

        raw_data = c.fetchone()

        if not raw_data:
            return False

        return {
            "id": v[0],
            "first_name": v[1],
            "last_name": v[2],
            "email": v[3],
            "phone_number": v[4],
            "phone_type": v[5],
            "birthday": v[6],
            "company": v[7],
            "workload": v[8],
            "department": v[9],
            "avatar_url": v[10],
            "created_at": v[11],
            "updated_at": v[12],
        }

    def update(self, id: int, data: dict) -> bool:
        c = self.connection.cursor()

        str_data = parser_null_values(data)

        sql = f"UPDATE contacts SET {str_data} WHERE id = {id}"

        c.execute(sql)
        self.connection.commit()

        if c.rowcount <= 0:
            return False

        return True

    def delete(self, id: int) -> bool:
        c = self.connection.cursor()

        sql = f"DELETE FROM contacts WHERE id = {id}"

        c.execute(sql)
        self.connection.commit()

        if c.rowcount <= 0:
            return False

        return True
