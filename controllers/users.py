from models.users import Users
from helpers.http_responses import HttpResponses


class CreateUserController:

    @staticmethod
    def execute(data: dict):
        try:
            users = Users()

            email_attr = data['email']

            isExistingEmail = users.select_by_email(email_attr)

            if isExistingEmail:
                return HttpResponses.bad_request(
                    f'This EMAIL ({email_attr}) already exits'
                )

            users.insert(data)

            return HttpResponses.created()

        except Exception as e:
            return HttpResponses.server_error()


class GetUserByIdController:

    @staticmethod
    def execute(id: int):
        try:
            users = Users()

            resp = users.select_by_id(id)

            if not resp:
                return HttpResponses.not_found(
                    f'User not found'
                )

            return HttpResponses.ok(resp)

        except Exception as e:
            return HttpResponses.server_error()


class DeleteUserByIdController:

    @staticmethod
    def execute(id: int):
        try:
            users = Users()

            resp = users.delete(id)

            if not resp:
                return HttpResponses.not_found(
                    f'User not found'
                )

            return HttpResponses.no_content()

        except Exception as e:
            return HttpResponses.server_error()


class UpdateUserByIdController:

    @staticmethod
    def execute(id: int, data: dict):
        try:
            users = Users()

            resp = users.update(id, data)

            if resp:
                return HttpResponses.not_found(
                    f'User not found'
                )

            return HttpResponses.ok()

        except Exception as e:
            return HttpResponses.server_error()
