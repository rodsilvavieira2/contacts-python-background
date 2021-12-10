from services.connection import Connection
from helpers.parser_data import *


class UserTokens(Connection):
    def insert(self, data: dict) -> bool:
        c = self.connection.cursor()

        sql = 'INSERT INTO user_tokens (`token`, `user_id`)' \
            'VALUES (%s, %s)'

        c.execute(sql, parse_dict_to_tuple(data))
        result = self.connection.commit()

        if c.rowcount <= 0:
            return False

        return True

    def select_by_token(self, token: str, id: int) -> dict | bool:
        c = self.connection.cursor()

        sql = f"SELECT * FROM user_tokens WHERE token = '{token}'"\
            f" AND id = {id}"

        c.execute(sql)

        raw_data = c.fetchone()

        if not raw_data:
            return False

        return {
            'id': raw_data[0],
            'token': raw_data[1],
            'user_id': raw_data[2],
            'created_at': raw_data[3],
            'updated_at': raw_data[4]
        }

    def delete(self, id: int) -> bool:
        c = self.connection.cursor()

        sql = f'DELETE FROM user_tokens WHERE id = {id}'

        c.execute(sql)

        self.connection.commit()

        if c.rowcount <= 0:
            return False

        return True
