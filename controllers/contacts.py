from models.contacts import Contacts
from models.users import Users
from validation.params import email_validation
from helpers.http_responses import HttpResponses


class CreateContactController:

    @staticmethod
    def execute(data: dict):
        try:
            users = Users()

            user_id = data['user_id']

            resp = users.select_by_id(user_id)

            if not resp:
                return HttpResponses.bad_request(
                    f'This user id ({user_id}) not exists.'
                )

            contacts = Contacts()

            email = data['email']

            if email:
                if not email_validation(email):
                    return HttpResponses.bad_request('Invalid Address Email')

            contacts.insert(data)

            return HttpResponses.created()

        except Exception as e:
            return HttpResponses.server_error()


class ListContactByIdController:
    @staticmethod
    def execute(id: int):
        try:
            contact = Contacts()

            resp = contact.select_contact_by_id(id)

            if not resp:
                return HttpResponses.not_found(
                    f'contact not found for this user {id}'
                )

        except Exception as e:
            return HttpResponses.server_error()


class ListAllContactByUserIdController:
    @staticmethod
    def execute(args: dict):
        try:
            contacts = Contacts()

            id = args.get('user')

            if not id:
                return HttpResponses.bad_request(
                    'Missing (user) argument on the query string.'
                )

            users = Users()

            isExistingUser = users.select_by_id(id)

            if not isExistingUser:
                return HttpResponses.not_found(
                    f"User not found  by the id ({id})"
                )

            resp = contacts.select_by_user_id(id)

            if not resp:
                return HttpResponses.no_content()

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
                    f'Error on delete contact'
                )

            return HttpResponses.no_content()

        except Exception as e:
            return HttpResponses.server_error()


class UpdateContactByIdController:

    @staticmethod
    def execute(id: int, data: dict):
        try:
            contacts = Contacts()

            resp = contacts.update(id, data)

            if not resp:
                return HttpResponses.not_found(
                    f'Error on update contact'
                )

            return HttpResponses.ok()

        except Exception as e:
            return HttpResponses.server_error()
