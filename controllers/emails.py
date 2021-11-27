from models.emails import Emails
from helpers.http_responses import HttpResponses


class CreateEmailController:

    @staticmethod
    def execute(data: dict):
        try:
            emails = Emails()

            email_attr = data['email']

            isExistingEmail = emails.select_by_email(email)

            if isExistingEmail:
                return HttpResponses.bad_request(
                    f'This EMAIL ({email_attr}) already exits'
                )

            return HttpResponses.created()

        except Exception as e:
            return HttpResponses.server_error()


class DeleteEmailByIdController:

    @staticmethod
    def execute(id: int):
        try:
            emails = Emails()

            rep = emails.delete(id)

            if isExistingEmail:
                return rep.not_found(
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

            rep = emails.update(id, data)

            if isExistingEmail:
                return rep.not_found(
                    f'Email not found'
                )

            return HttpResponses.ok()

        except Exception as e:
            return HttpResponses.server_error()
