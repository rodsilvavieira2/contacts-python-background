from models.users import Users
from models.user_tokens import UserTokens
from config.auth import auth
from helpers.http_responses import HttpResponses

from bcrypt import checkpw
import jwt
from datetime import datetime, timedelta


class LoginController:
    @staticmethod
    def execute(data: dict):
        try:
            email = data.get('email')
            password = data.get('password')

            users = Users()

            user = users.select_by_email(email)

            if not user:
                return HttpResponses.invalid_credentials()

            hashed_password = user['password']

            isValid = checkpw(password.encode(), hashed_password.encode())

            if not isValid:
                return HttpResponses.invalid_credentials()

            access_token = jwt.encode(
                {
                    'sub': user['id'],
                    'exp': datetime.utcnow() + timedelta(seconds=30),
                    'iat': datetime.utcnow()
                },
                auth['jwt_key']
            )

            refresh_token = jwt.encode(
                {
                    'sub': user['id'],
                    'exp': datetime.utcnow() + timedelta(
                        days=30
                    ),
                    'iat': datetime.utcnow()
                },
                auth['jwt_key']
            )

            userTokens = UserTokens()

            userTokens.insert(
                {'token': refresh_token, 'user_id': user['id']}
            )

            return HttpResponses.ok({
                'access_token': access_token,
                'refresh_token': refresh_token,
                'first_name': user['first_name'],
                'last_name': user['last_name'],
                'email': user['email'],
                'avatar_url': user['avatart_url']
            })

        except Exception as e:
            return HttpResponses.server_error()


class RefreshTokenController:
    @staticmethod
    def execute(token: str):
        try:
            key = auth['jwt_key']
            payload = jwt.decode(token, key, algorithms=["HS256"])

            userTokens = UserTokens()

            current_refresh_token = userTokens.select_by_token_and_id(
                token, payload['sub']
            )

            if not current_refresh_token:
                return HttpResponses.token_invalid()

            userTokens.delete(current_refresh_token['id'])

            access_token = jwt.encode(
                {
                    'sub': payload['sub'],
                    'exp': datetime.utcnow() + timedelta(seconds=30),
                    'iat': datetime.utcnow()
                },
                auth['jwt_key']
            )

            refresh_token = jwt.encode(
                {
                    'sub': payload['sub'],
                    'exp': datetime.utcnow() + timedelta(
                        days=auth['refresh_token_experie']
                    ),
                    'iat': datetime.utcnow()
                },
                auth['jwt_key']
            )

            userTokens.insert(
                {'token': refresh_token, 'user_id': payload['sub']}
            )

            return HttpResponses.ok({
                'access_token': access_token,
                'refresh_token': refresh_token
            })

        except jwt.ExpiredSignatureError as e:
            return HttpResponses.token_expired()

        except jwt.DecodeError as e:
            return HttpResponses.token_invalid()

        except Exception as e:
            return HttpResponses.server_error()
