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
                    "is_favorite": bool(v[12]),
                    "is_onTrash": bool(v[13]),
                    "deleted_at": v[14],
                    "created_at": v[15],
                    "updated_at": v[16],
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
            "id": raw_data[0],
            "first_name": raw_data[1],
            "last_name": raw_data[2],
            "phone_number": raw_data[3],
            "email": raw_data[4],
            "phone_type_id": raw_data[5],
            "birthday": raw_data[6],
            "company": raw_data[7],
            "job": raw_data[8],
            "department": raw_data[9],
            "avatar_url": raw_data[10],
            "is_favorite": bool(raw_data[12]),
            "is_onTrash": bool(raw_data[13]),
            "deleted_at": raw_data[14],
            "created_at": raw_data[15],
            "updated_at": raw_data[16],
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
