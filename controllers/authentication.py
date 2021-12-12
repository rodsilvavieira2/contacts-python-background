from models.users import Users
from models.user_tokens import UserTokens

from helpers.http_responses import HttpResponses

from bcrypt import checkpw
from jwt import encode, decode, DecodeError, ExpiredSignature


class LoginController:
    @staticmethod
    def execute(data: dict):
        try:
            email = data.get('email')
            password = data.get('password')

            user = Users().select_by_email(email)

            if not user:
                HttpResponses.invalid_credentials()

            hashed_password = user['password']

            if not checkpw(password.encode(), hashed_password.encode()):
                HttpResponses.invalid_credentials()

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

            UserTokens().insert(
                {'token': refresh_token, 'user_id': current_user['id']}
            )

            return HttpResponses.ok({
                'access_token': access_token,
                'refresh_token': refresh_token,
                'user': {
                    'first_name': user['first_name'],
                    'lastName': user['last_name'],
                    'email': user['email'],
                    'avatar_url': user['avatart_url']
                }
            })

        except Exception as e:
            HttpResponses.server_error()


class RefreshToken:
    @staticmethod
    def execute(toke: str):
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

        except ExpiredSignature as e:
            return HttpResponses.token_expired()

        except DecodeError as e:
            return HttpResponses.token_invalid()

        except Exception as e:
            return HttpResponses.server_error()
