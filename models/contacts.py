from services.connection import Connection
from helpers.parser_data import parse_dict_to_tuple, parser_null_values


class Contacts(Connection):
    def insert(self, data: dict) -> bool:
        c = self.connection.cursor()

        sql = "INSERT INTO contacts (`first_name`, `last_name`, `email`," \
            " `phone_number`, `phone_type_id`, `birthday`, `company`," \
            " `job`, `department`,`avatar_url`, `user_id`)" \
            " VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

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
                    "phone_number": v[3],
                    "email": v[4],
                    "phone_type_id": v[5],
                    "birthday": v[6],
                    "company": v[7],
                    "job": v[8],
                    "department": v[9],
                    "avatar_url": v[10],
                    "is_favorite": v[12],
                    "is_onTrash": v[13],
                    "created_at": v[14],
                    "updated_at": v[15],
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
            "phone_number": v[3],
            "email": v[4],
            "phone_type_id": v[5],
            "birthday": v[6],
            "company": v[7],
            "job": v[8],
            "department": v[9],
            "avatar_url": v[10],
            "is_favorite": bool(v[12]),
            "is_onTrash": bool(v[13]),
            "created_at": v[14],
            "updated_at": v[15],
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
