from flask_restful import request
import jwt
from os import getenv
from helpers.http_responses import HttpResponses
from models.users import Users


def token_required(f):
    def wrapper(*args, **kwargs):
        auth_header = request.headers.get('Authorization')
        current_user = None

        if auth_header:
            try:
                token = auth_header.split(' ')[1]
                users = Users()

                try:
                    key = getenv('JWT_KEY')
                    token_decoded = jwt.decode(
                        token, key, algorithms=["HS256"]
                    )
                    current_user = users.select_by_id(token_decoded['uid'])

                except jwt.ExpiredSignatureError as e:
                    return HttpResponses.token_expired()

                except (jwt.InvalidSignatureError, jwt.InvalidTokenError):
                    return HttpResponses.token_invalid()

            except IndexError as e:
                return HttpResponses.token_required()
        else:
            return HttpResponses.token_required()

        return f(*args, **kwargs, current_user=current_user)

    return wrapper
