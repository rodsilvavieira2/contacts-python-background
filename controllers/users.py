from models.users import Users
from models.user_tokens import UserTokens
from helpers.http_responses import HttpResponses
from bcrypt import hashpw, gensalt, checkpw
from jwt import encode, decode, InvalidIssuerError
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

            passsword = data.get('password')

            hashed_password = hashpw(passsword.encode(), gensalt())

            data.update({'password': hashed_password})

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
            hashed_password = current_user.get('password')

            isValid = checkpw(password.encode(), hashed_password.encode())

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

            userTokens = UserTokens()

            refresh_token = encode(
                {
                    'uid': current_user['id'],
                    'exp': datetime.utcnow() + timedelta(days=30),
                    'iat': datetime.utcnow()
                },
                getenv('JWT_KEY').encode('utf-8')
            )

            userTokens.insert(
                {'token': refresh_token, 'user_id': current_user['id']}
            )

            return HttpResponses.ok({
                'access_token': access_token,
                'refresh_token': refresh_token
            })

        except Exception as e:
            return HttpResponses.server_error()


class RefreshTookenController:

    @staticmethod
    def execute(token: str):
        try:
            payload = decode(token)

            userTokens = UserTokens()

            refresh_token = userTokens.select_by_token_and_id(
                token, payload['uid']
            )

            if not refresh_token:
                raise HttpResponses.unauthorized('invalid refresh token')

            userTokens.delete(refresh_token['id'])

            access_token = encode(
                {
                    'uid': current_user['id'],
                    'exp': datetime.utcnow() + timedelta(minutes=15),
                    'iat': datetime.utcnow()
                },
                getenv('JWT_KEY').encode('utf-8')
            )

            userTokens = UserTokens()

            refresh_token = encode(
                {
                    'uid': current_user['id'],
                    'exp': datetime.utcnow() + timedelta(days=30),
                    'iat': datetime.utcnow()
                },
                getenv('JWT_KEY').encode('utf-8')
            )

            userTokens.insert(
                {'token': refresh_token, 'user_id': current_user['id']}
            )

            return HttpResponses.ok({
                'access_token': access_token,
                'refresh_token': refresh_token
            })

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
