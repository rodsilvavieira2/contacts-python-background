from models.users import Users
from helpers.http_responses import HttpResponses


class CreateUserController:

    @staticmethod
    def execute(data: dict):
        try:
            users = Users()

            email_attr = data['email']

            isExistingEmail = users.select_by_email(email)

            if isExistingEmail:
                return HttpResponses.bad_request(
                    f'This EMAIL ({email_attr}) already exits'
                )

            return HttpResponses.created()

        except Exception as e:
            return HttpResponses.server_error()


class GetUserByIdController:

    @staticmethod
    def execute(id: int):
        try:
            users = Users()

            isExistingUser = users.select_by_id(id)

            if isExistingEmail:
                return HttpResponses.not_found(
                    f'User not found'
                )

            return HttpResponses.ok(isExistingUser)

        except Exception as e:
            return HttpResponses.server_error()


class DeleteUserByIdController:

    @staticmethod
    def execute(id: int):
        try:
            users = Users()

            rep = users.delete(id)

            if isExistingEmail:
                return rep.not_found(
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

            rep = users.update(id, data)

            if isExistingEmail:
                return rep.not_found(
                    f'User not found'
                )

            return HttpResponses.ok()

        except Exception as e:
            return HttpResponses.server_error()
