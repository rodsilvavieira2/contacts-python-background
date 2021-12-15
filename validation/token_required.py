from helpers.http_responses import HttpResponses
from models.users import Users
from config.auth import auth

from flask_restful import request
import jwt


def token_required(f):
    def wrapper(*args, **kwargs):
        auth_header = request.headers.get('Authorization')
        current_user = None

        if auth_header:
            try:
                token = auth_header.split(' ')[1]

                try:
                    key = auth['jwt_key']

                    token_decoded = jwt.decode(
                        token, key, algorithms=["HS256"]
                    )

                    current_user = Users().select_by_id(token_decoded['sub'])

                except jwt.ExpiredSignatureError as e:
                    return HttpResponses.token_expired()

                except jwt.DecodeError:
                    return HttpResponses.token_invalid()

            except IndexError as e:
                return HttpResponses.token_required()

            except Exception as e:
                return HttpResponses.server_error()
        else:
            return HttpResponses.token_required()

        return f(*args, **kwargs, current_user=current_user)

    return wrapper
