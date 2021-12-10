from models.users import Users
from helpers.http_responses import HttpResponses
from bcrypt import hashpw, gensalt, checkpw
from jwt import encode
from datetime import datetime, timedelta
from os import getenv


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

            data.update({'password': hashpw(data['password'], gensalt())})

            users.insert(data)

            return HttpResponses.created()

        except Exception as e:
            return HttpResponses.server_error()


class LoginUserController:

    @staticmethod
    def execute(data: dict):
        try:
            user = Users()

            email = data.get('email')

            current_user = user.select_by_email(email)

            if not current_user:
                return HttpResponses.not_found(
                    f'User not found for this email: {email}'
                )

            password = data.get('password')
            hashed_password = current_user.get('passsword')

            isValid = checkpw(password, hashed_password)

            if not isValid:
                return HttpResponses.unauthorized('Invalid passsword')

            access_token = encode(
                {
                    'uid': current_user['id'],
                    'exp': datetime.utcnow() + timedelta(minutes=15),
                    'iat': datetime.utcnow()
                },
                getenv('JWT_KEY').encode('utf-8')
            )

            refresh_token = encode(
                {
                    'uid': current_user['id'],
                    'exp': datetime.utcnow() + timedelta(days=30),
                    'iat': datetime.utcnow()
                },
                getenv('JWT_KEY').encode('utf-8')
            )

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
