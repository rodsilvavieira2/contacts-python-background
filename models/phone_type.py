from services.connection import Connection


class PhoneType(Connection):
    def select_by_id(self, id) -> dict | bool:
        c = self.connection.cursor()

        sql = f'SELECT * FROM phone_types WHERE id = {id}'

        c.execute(sql)

        raw_data = c.fetchone()

        if not raw_data:
            return False

        return {
            "id": raw_data[0],
            "type": raw_data[1]
        }
