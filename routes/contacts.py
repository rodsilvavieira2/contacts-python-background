from controllers.contacts import *
from flask_restful import Resource, reqparse


class CreateContactRoute(Resource):
    def post(self):
        params = reqparse.RequestParser()

        params.add_argument('first_name', type=str, required=True)
        params.add_argument('last_name', type=str, required=True)
        params.add_argument('birthday', type=str, required=False)
        params.add_argument('company', type=str, required=False)
        params.add_argument('workload', type=str, required=False)
        params.add_argument('department', type=str, required=False)
        params.add_argument('user_id', type=str, required=True)

        args = params.parse_args()

        resp = CreateContactController.execute(args)

        return resp


class ListAllContactByUserIdRoute(Resource):
    def get(self, id: int):

        resp = ListAllContactByUserIdController.execute(user_id=id)

        return resp


class DeleteContactByIdRoute(Resource):
    def delete(self, id: int):

        resp = DeleteContactByIdController.execute(id)

        return resp


class UpdateContactByIdRoute(Resource):
    def put(self, id):
        params = reqparse.RequestParser()

        params.add_argument('first_name', type=str, required=False)
        params.add_argument('last_name', type=str, required=False)
        params.add_argument('birthday', type=str, required=False)
        params.add_argument('company', type=str, required=False)
        params.add_argument('workload', type=str, required=False)
        params.add_argument('department', type=str, required=False)
        params.add_argument('user_id', type=str, required=False)

        args = params.parse_args()

        resp = UpdateContactByIdController.execute(id, args)

        return resp
