from controllers.contacts import *
from validation.token_required import token_required
from flask_restful import Resource, reqparse
from datetime import datetime


class CreateContactRoute(Resource):
    @token_required
    def post(self, current_user: dict):
        params = reqparse.RequestParser()

        params.add_argument('first_name', type=str, required=True)
        params.add_argument('last_name', type=str, required=True)
        params.add_argument('email', type=str, required=True)
        params.add_argument('phone_number', type=str, required=True)
        params.add_argument('phone_type_id', type=int, required=True)
        params.add_argument('birthday', type=str, required=False)
        params.add_argument('company', type=str, required=False)
        params.add_argument('job', type=str, required=False)
        params.add_argument('department', type=str, required=False)
        params.add_argument('avatar_url', type=str, required=False)

        args = params.parse_args()

        id = current_user['id']

        args.update({'user_id': id})

        resp = CreateContactController.execute(args)

        return resp


class ListAllContactByUserIdRoute(Resource):
    @token_required
    def get(self, current_user: dict):

        id = current_user['id']

        resp = ListAllContactByUserIdController.execute(id)

        return resp


class ListContactByIdRoute(Resource):
    @token_required
    def get(self, id: int, current_user):

        resp = ListContactByIdController.execute(id)

        return resp


class DeleteContactByIdRoute(Resource):
    @token_required
    def delete(self, id: int, current_user):

        resp = DeleteContactByIdController.execute(id)

        return resp


class UpdateContactByIdRoute(Resource):
    @token_required
    def put(self, id, current_user):
        params = reqparse.RequestParser()

        params.add_argument('first_name', type=str, required=False)
        params.add_argument('last_name', type=str, required=False)
        params.add_argument('email', type=str, required=False)
        params.add_argument('phone_number', type=str, required=False)
        params.add_argument('phone_type_id', type=int, required=False)
        params.add_argument('birthday', type=str, required=False)
        params.add_argument('company', type=str, required=False)
        params.add_argument('job', type=str, required=False)
        params.add_argument('department', type=str, required=False)
        params.add_argument('deleted_at', type=str, required=False)
        params.add_argument('is_favorite', type=int, required=False)
        params.add_argument('is_onTrash', type=int, required=False)
        params.add_argument('avatar_url', type=str, required=False)

        args = params.parse_args()

        resp = UpdateContactByIdController.execute(id, args)

        return resp
