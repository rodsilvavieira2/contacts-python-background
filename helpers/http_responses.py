from flask import jsonify

OK = 200
CREATED = 201
NOT_FOUND = 404
BAD_REQUEST = 400
SERVER_ERROR = 500
NO_CONTENT = 204
UNAUTHORIZED = 401
FORBIDDEN = 403


class HttpResponses:
    @staticmethod
    def ok(data: dict = {}):
        resp = {
            'message': 'Request successfully complete',
            'success': True
        }

        if data:
            resp.update({"data": data})

        return jsonify(resp)

    @staticmethod
    def created():
        return {
            "message": "Resource successfully created",
            "success": True
        }, CREATED

    @staticmethod
    def not_found(message: str = ''):
        resp = {
            "message": "Resource cold not be found.",
            "success": True
        }

        if message:
            resp.update({"message": message})

        return resp, NOT_FOUND

    @staticmethod
    def unauthorized(message: str = ''):
        resp = {
            'message': 'unauthorized action',
            "success": False
        }

        if message:
            resp.update({'message': message})

        return resp, UNAUTHORIZED

    @staticmethod
    def token_expired():
        return {
            'code': 'token.expired',
            'message': 'token expired',
            'success': False
        }, UNAUTHORIZED

    @staticmethod
    def bad_request(message: str = ''):
        resp = {
            "message": "sorry, you submitted a poorly formatted request",
            "success": False
        }

        if message:
            resp.update({"message": message})

        return resp, BAD_REQUEST

    @staticmethod
    def invalid_credentials():
        return {
            "message": 'passsword or email incorrect',
            "code": 'auth.credentials',
            "success": False
        }, UNAUTHORIZED

    @staticmethod
    def server_error():
        return {
            "message": "sorry, something went wrong",
            "success": False,
            "code": 'error.general'
        }, SERVER_ERROR

    @staticmethod
    def no_content():
        return {}, NO_CONTENT

    @staticmethod
    def token_required():
        return {
            "message": 'acccess token required',
            "code": 'token.required',
            "success": False
        }, FORBIDDEN

    @staticmethod
    def token_invalid():
        return {
            "message": "invalid token",
            "code": "token.invalid",
            "success": False
        }

    @staticmethod
    def forbidden(message: str = ''):
        resp = {
            'success': False,
            "message": 'Forbidden content'
        }

        if message:
            resp.update({"message": message})

        return resp, FORBIDDEN
