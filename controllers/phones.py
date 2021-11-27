from models.phones import Phones
from helpers.http_responses import HttpResponses


class CreatePhoneController:

    @staticmethod
    def execute(data: dict):
        try:
            phones = Phones()

            phone_attr = data['phone']

            isExistingEmail = phones.select_by_phone(phone_attr)

            if isExistingEmail:
                return HttpResponses.bad_request(
                    f'This PHONE ({phone_attr}) already exits'
                )

            phones.insert(data)

            return HttpResponses.created()

        except Exception as e:
            return HttpResponses.server_error()


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
