from services.connection import Connection
from helpers.parser_data import parse_dict_to_tuple, parser_null_values
from datetime import datetime


class Contacts(Connection):
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

            c.execute(f'SELECT * FROM phones WHERE contact_id = {c_id}')
            result_phones = c.fetchall()

            c_phones = []

            for v in result_phones:
                c_phones.append({
                    "id": v[0],
                    "phone": v[1]
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
