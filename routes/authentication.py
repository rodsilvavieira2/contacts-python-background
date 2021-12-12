from controllers.authentication import *

from validation.token_required import token_required

from flask_restful import Resource, reqparse


class LoginRoute(Resource):
    def post(self):
        params = reqparse.RequestParser()

        params.add_argument('password', type=str, required=True)
        params.add_argument('email', type=str, required=True)

        args = params.parse_args()

        resp = LoginController.execute(args)

        return resp


class RefreshTokenRoute(Resource):
    def post(self):

        params = reqparse.RequestParser()

        params.add_argument('access_token', type=str, required=True)

        args = params.parse_args()

        token = args['access_token']

        resp = RefreshTokenController.execute(token)

        return resp
