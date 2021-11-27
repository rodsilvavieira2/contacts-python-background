from services.connection import Connection
from helpers.parser_data import parse_dict_to_tuple, parser_null_values
from datetime import datetime


class Users(Connection):
    def insert(self, data: dict) -> bool:
        c = self.connection.cursor()

        sql = 'INSERT INTO contacts' \
            ' values(null, %s, %s, %s, %s, %s, %s, %s, %s, %s)'

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

        sql = 'SELECT * FROM contacts'

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
                "birthday": v[3],
                "company": v[4],
                "workload": v[5],
                "department": v[6],
                "created_at": v[8],
                "updated_at": v[9],
            })

        return data

    def select_byu_user_id(self, id: int):
        c = self.connection.cursor()

        sql = f'SELECT * FROM contacts WHERE user_id = {id}'

        c.execute(sql)

        raw_data = c.fetchone()

        if not raw_data:
            return False

        return {
            "id": v[0],
            "first_name": v[1],
            "last_name": v[2],
            "birthday": v[3],
            "company": v[4],
            "workload": v[5],
            "department": v[6],
            "created_at": v[8],
            "updated_at": v[9],
        }

        return data

    def update(self, id: int, data: dict) -> bool:
        c = self.connection.cursor()

        str_data = parser_null_values(data)

        sql = f"UPDATE contacts SET {str_data} WHERE id = {id}"

        c.execute(sql)
        self.connection.commit()

        if not c.rowcount:
            return False

        return True

    def delete(self, id: int) -> bool:
        c = self.connection.cursor()

        sql = f"DELETE FROM contacts WHERE id = {id}"

        c.execute(sql)
        self.connection.commit()

        if not c.rowcount:
            return False

        return True
