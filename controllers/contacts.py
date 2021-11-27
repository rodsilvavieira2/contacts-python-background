from models.contacts import Contacts
from helpers.http_responses import HttpResponses


class CreateContactController:

    @staticmethod
    def execute(data: dict):
        try:
            contacts = Contacts()

            contacts.insert(data)

            return HttpResponses.created()

        except Exception as e:
            return HttpResponses.server_error()


class ListAllContactByUserIdController:
    @staticmethod
    def execute(self, user_id: int):
        try:
            contacts = Contacts()

            resp = contacts.select_by_user_id(user_id)

            if not resp:
                return HttpResponses.not_found('No contacts for this user')

            return HttpResponses.created()

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

            if not resp:
                return HttpResponses.not_found(
                    f'Contact not found'
                )

            return HttpResponses.ok()

        except Exception as e:
            return HttpResponses.server_error()
