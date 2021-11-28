from models.contacts import Contacts
from models.users import Users
from models.emails import Emails
from models.phones import Phones
from validation.params import email_validation
from helpers.http_responses import HttpResponses


class CreateContactController:

    @staticmethod
    def execute(data: dict):
        try:
            users = Users()

            user_id = data['user_id']

            isUserExisting = users.select_by_id(user_id)

            if not isUserExisting:
                return HttpResponses.bad_request(
                    f'This user id ({user_id}) not exists.'
                )

            contacts = Contacts()

            emails_attr = data.get('emails')
            phones_attr = data.get('phones')

            data.pop('emails')
            data.pop('phones')

            if emails_attr and len(emails_attr):
                for v in emails_attr:
                    email = v.get('email')
                    isValid = email_validation(email)

                    if not isValid:
                        return HttpResponses.bad_request(
                            f'The email:{email} is invalid'
                        )

            contact_id = contacts.insert(data)

            if contact_id:
                if emails_attr and len(emails_attr):
                    for v in emails_attr:
                        email = v.get('email')
                        if email and contact_id:
                            Emails().insert({
                                "email": email,
                                "contact_id": contact_id
                            })

                if phones_attr and len(phones_attr):
                    for v in phones_attr:
                        phone = v.get('phone')
                        phone_type_id = v.get('type')

                        if phone and contact_id and phone_type_id:
                            Phones().insert({
                                "phone": phone,
                                "contact_id": contact_id,
                                "phone_type_id": phone_type_id
                            })

            return HttpResponses.created()

        except Exception as e:
            return HttpResponses.server_error()


class ListAllContactByUserIdController:
    @staticmethod
    def execute(user_id: int):
        try:
            contacts = Contacts()

            resp = contacts.select_by_user_id(user_id)

            if not resp:
                return HttpResponses.not_found('No contacts for this user')

            return HttpResponses.ok(resp)

        except Exception as e:
            return HttpResponses.server_error()


class DeleteContactByIdController:

    @staticmethod
    def execute(id: int):
        try:
            contacts = Contacts()

            resp = contacts.delete(id)

            if not resp:
                return HttpResponses.not_found(
                    f'Contact not found'
                )

            return HttpResponses.no_content()

        except Exception as e:
            return HttpResponses.server_error()


class UpdateContactByIdController:

    @staticmethod
    def execute(id: int, data: dict):
        try:
            contacts = Contacts()

            emails_attr = data.get('emails')
            phones_attr = data.get('phones')

            data.pop('emails')
            data.pop('phones')

            resp = contacts.update(id, data)

            if not resp:
                return HttpResponses.not_found(
                    f'Contact not found'
                )

            if emails_attr:
                for v in emails_attr:
                    id = v.get('id')
                    email = v.get('email')

                    if id and email:
                        Emails().update(id, email)

            if phones_attr:
                for v in phones_attr:
                    id = v.get('id')
                    phone = v.get('phone')

                    if id and phone:
                        Phones().update(id, phone)

            return HttpResponses.ok()

        except Exception as e:
            return HttpResponses.server_error()
