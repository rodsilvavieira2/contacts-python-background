from faker import Faker
from mysql.connector import connect

c = connect(
    host="localhost",
    port=3306,
    user="root",
    password="123456",
    database="contacts"
)

faker = Faker()

contacts = []
phone_types = [
    {
        "type": "residencial"
    },
    {
        "type": "comercial"
    },
    {
        "type": "celular"
    }
]

user = {
    "first_name": 'rodrigo',
    "last_name": 'silva',
    "email": 'rodsilvavieira@gmail.com',
    "password": '123456'
}


for index in range(1, 1000):
    contacts.append({
        "first_name": faker.first_name(),
        "last_name": faker.last_name(),
        "email": faker.email(),
        "phone_number": faker.phone_number(),
        "birthday": faker.date(),
        "company": faker.company(),
        "job": faker.job(),
        "department": faker.bs(),
        "avatar_url": faker.image_url(),
        "user_id":  2,
        "phone_type_id": faker.randomize_nb_elements(min=1, max=3)
    })

cursor = c.cursor()

sql = 'INSERT INTO users (`first_name`, `last_name`, `email`, `password`) ' \
    ' VALUES (%s, %s, %s, %s)'

cursor.execute(sql, tuple(user.values()))
c.commit()

sql_phone_types = "INSERT INTO phone_types (`type`) VALUES (%s) "

for v in phone_types:
    cursor.execute(sql_phone_types, tuple(v.values()))
    c.commit()

sql_contacts = "INSERT INTO contacts" \
    "(`first_name`, `last_name`, `email`, `phone_number`, `birthday`, `company`," \
    " `job`, `department`,`avatar_url`, `user_id`, `phone_type_id`)" \
    " VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

for v in contacts:
    cursor.execute(sql_contacts, tuple(v.values()))
    c.commit()
