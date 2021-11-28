from services.connection import Connection
from helpers.parser_data import parse_dict_to_tuple, parser_null_values
from datetime import datetime


class Contacts(Connection):
    def insert(self, data: dict) -> bool | int:
        c = self.connection.cursor()

        sql = 'INSERT INTO contacts' \
            ' values(null, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'

        now = datetime.now()

        data.update({'create_at': now})
        data.update({'update_at': now})

        c.execute(sql, parse_dict_to_tuple(data))
        self.connection.commit()

        if not c.rowcount:
            return False

        return c.lastrowid

    def select_by_user_id(self, id: int):
        c = self.connection.cursor()

        sql = f'SELECT * FROM contacts WHERE user_id = {id}'

        c.execute(sql)

        raw_data = c.fetchall()

        if not len(raw_data):
            return False

        emails = dict()
        phones = dict()

        for v in raw_data:
            c_id = v[0]

            c.execute(f'SELECT * FROM emails WHERE contact_id = {c_id}')
            result_emails = c.fetchall()

            c_emails = []

            for v in result_emails:
                c_emails.append({
                    "id": v[0],
                    "email": v[1]
                })

            sql_phone = 'SELECT * FROM phones as p' \
                        ' JOIN phone_types as pt ON p.phone_type_id = pt.id' \
                        f'  WHERE contact_id = {c_id}'

            c.execute(sql_phone)
            result_phones = c.fetchall()

            c_phones = []

            for v in result_phones:
                c_phones.append({
                    "id": v[0],
                    "phone": v[1],
                    "type": v[3]
                })

            phones.update({
                c_id: c_phones
            })

            emails.update({
                c_id: c_emails
            })

        data = list()

        for v in raw_data:
            data.append(
                {
                    "id": v[0],
                    "first_name": v[1],
                    "last_name": v[2],
                    "birthday": v[3],
                    "company": v[4],
                    "workload": v[5],
                    "department": v[6],
                    "emails": emails.get(v[0]),
                    "phones": phones.get(v[0]),
                    "created_at": v[8],
                    "updated_at": v[9],
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
            "birthday": raw_data[3],
            "company": raw_data[4],
            "workload": raw_data[5],
            "department": raw_data[6],
            "user_id": raw_data[7],
            "created_at": raw_data[8],
            "updated_at": raw_data[9],
        }

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
