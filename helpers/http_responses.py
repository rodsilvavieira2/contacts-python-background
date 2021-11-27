from flask import jsonify

OK = 200
CREATED = 201
NOT_FOUND = 404
BAD_REQUEST = 400
SERVER_ERROR = 500
NO_CONTENT = 204


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
    def bad_request(message: str = ''):
        resp = {
            "message": "sorry, you submitted a poorly formatted request",
            "success": False
        }

        if message:
            resp.update({"message": message})

        return resp, BAD_REQUEST

    @staticmethod
    def server_error():
        return {
            "message": "sorry, something went wrong",
            "success": False
        }, SERVER_ERROR

    @staticmethod
    def no_content():
        return {}, NO_CONTENT
