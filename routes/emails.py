from controllers.emails import *
from flask_restful import Resource, reqparse


class CreateEmailRoute(Resource):
    def post(self):
        params = reqparse.RequestParser()

        params.add_argument('email', type=str, required=True)
        params.add_argument('contact_id', type=int, required=True)

        args = params.parse_args()

        resp = CreateEmailController.execute(args)

        return resp


class DeleteEmailByIdRoute(Resource):
    def Delete(self, id: int):

        resp = DeleteEmailByIdController.execute(id)

        return resp


class UpdateEmailByIdRoute(Resource):
    def put(self, id):
        params = reqparse.RequestParser()

        params.add_argument('email', type=str, required=False)
        params.add_argument('contact_id', type=int, required=False)

        args = params.parse_args()

        resp = UpdateEmailByIdController.execute(id, args)

        return resp
