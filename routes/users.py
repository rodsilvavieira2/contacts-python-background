from controllers.users import *
from flask_restful import Resource, reqparse


class CreateUserRoute(Resource):
    def post(self):
        params = reqparse.RequestParser()

        params.add_argument('first_name', type=str, required=True)
        params.add_argument('last_name', type=str, required=True)
        params.add_argument('email', type=str, required=True)
        params.add_argument('password', type=str, required=True)
        params.add_argument('avatart_url', type=str, required=False)

        args = params.parse_args()

        resp = CreateUserController.execute(args)

        return resp


class GetUserByIdRoute(Resource):
    def get(self, id: int):

        resp = GetUserByIdController.execute(id)

        return resp


class DeleteUserRoute(Resource):
    def Delete(self, id: int):

        resp = DeleteUserByIdController.execute(id)

        return resp


class UpdateUserRoute(Resource):
    def put(self, id):
        params = reqparse.RequestParser()

        params.add_argument('first_name', type=str, required=False)
        params.add_argument('last_name', type=str, required=False)
        params.add_argument('email', type=str, required=False)
        params.add_argument('password', type=str, required=False)
        params.add_argument('avatart_url', type=str, required=False)

        args = params.parse_args()

        resp = UpdateUserByIdController.execute(id, args)

        return resp
