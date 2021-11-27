from controllers.phones import *
from flask_restful import Resource, reqparse


class CreatePhoneRoute(Resource):
    def post(self):
        params = reqparse.RequestParser()

        params.add_argument('phone', type=str, required=True)
        params.add_argument('contact_id', type=int, required=True)

        args = params.parse_args()

        resp = CreatePhoneController.execute(args)

        return resp


class DeletePhoneByIdRoute(Resource):
    def delete(self, id: int):

        resp = DeletePhoneByIdController.execute(id)

        return resp


class UpdatePhoneByIdRoute(Resource):
    def put(self, id):
        params = reqparse.RequestParser()

        params.add_argument('phone', type=str, required=False)
        params.add_argument('contact_id', type=int, required=False)

        args = params.parse_args()

        resp = UpdatePhoneByIdController.execute(id, args)

        return resp
