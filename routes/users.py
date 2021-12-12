from controllers.users import *
from flask_restful import Resource, reqparse
from validation.token_required import token_required


class CreateUserRoute(Resource):
    def post(self):
        params = reqparse.RequestParser()

        params.add_argument('first_name', type=str, required=True)
        params.add_argument('last_name', type=str, required=True)
        params.add_argument('email', type=str, required=True)
        params.add_argument('password', type=str, required=True)
        params.add_argument('avatar_url', type=str, required=False)

        args = params.parse_args()

        resp = CreateUserController.execute(args)

        return resp


class LoginUserRoute(Resource):
    def post(self):
        params = reqparse.RequestParser()

        params.add_argument('password', type=str, required=True)
        params.add_argument('email', type=str, required=True)

        args = params.parse_args()

        resp = LoginUserController.execute(args)

        return resp


class RefreshTokenRoute(Resource):
    def post(self, token: str):
        resp = RefreshTookenController.execute(token)

        return resp


class GetUserInfoRoute(Resource):
    @token_required
    def get(self, current_user: dict):

        id = current_user['id']

        resp = GetUserByIdController.execute(id)

        return resp


class DeleteUserByIdRoute(Resource):
    @token_required
    def delete(self, current_user: dict):
        id = current_user['id']

        resp = DeleteUserByIdController.execute(id)

        return resp


class UpdateUserByIdRoute(Resource):
    @token_required
    def put(self, current_user: dic):
        params = reqparse.RequestParser()

        params.add_argument('first_name', type=str, required=False)
        params.add_argument('last_name', type=str, required=False)
        params.add_argument('email', type=str, required=False)
        params.add_argument('password', type=str, required=False)
        params.add_argument('avatar_url', type=str, required=False)

        args = params.parse_args()

        id = current_user['id']

        resp = UpdateUserByIdController.execute(id, args)

        return resp
