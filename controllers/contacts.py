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

            isUserExisting = users.select_by_id(user_id)

            if not isUserExisting:
                return HttpResponses.bad_request(
                    f'This user id ({user_id}) not exists.'
                )

            contacts = Contacts()

            email = contacts['email']

            if not email_validation(email):
                return HttpResponses.bad_request('Invalid Address Email')

            contacts.insert(data)

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

            resp = contacts.update(id, data)

            if resp:
                return HttpResponses.not_found(
                    f'COntact not found'
                )

            return HttpResponses.ok()

        except Exception as e:
            return HttpResponses.server_error()
