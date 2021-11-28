from models.phones import Phones
from models.contacts import Contacts
from models.phone_type import PhoneType
from helpers.http_responses import HttpResponses


class DeletePhoneByIdController:

    @staticmethod
    def execute(id: int):
        try:
            phones = Phones()

            resp = phones.delete(id)

            if not resp:
                return HttpResponses.not_found(
                    f'Phone not found'
                )

            return HttpResponses.no_content()

        except Exception as e:
            return HttpResponses.server_error()


class UpdatePhoneByIdController:

    @staticmethod
    def execute(id: int, data: dict):
        try:
            phones = Phones()

            resp = phones.update(id, data)

            if not resp:
                return HttpResponses.not_found(
                    f'Phone not found'
                )

            return HttpResponses.ok()

        except Exception as e:
            return HttpResponses.server_error()
