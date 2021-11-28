from models.emails import Emails
from models.contacts import Contacts
from helpers.http_responses import HttpResponses


class DeleteEmailByIdController:

    @staticmethod
    def execute(id: int):
        try:
            emails = Emails()

            resp = emails.delete(id)

            if not resp:
                return HttpResponses.not_found(
                    f'Email not found'
                )

            return HttpResponses.no_content()

        except Exception as e:
            return HttpResponses.server_error()


class UpdateEmailByIdController:

    @staticmethod
    def execute(id: int, data: dict):
        try:
            emails = Emails()

            resp = emails.update(id, data)

            if not resp:
                return HttpResponses.not_found(
                    f'Email not found'
                )

            return HttpResponses.ok()

        except Exception as e:
            return HttpResponses.server_error()
