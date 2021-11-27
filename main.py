from flask import Flask
from flask_restful import Api
from flask_cors import CORS

from routes.users import *

app = Flask(__name__)

api = Api(app)

# users routes

api.add_resource(CreateUserRoute, '/users')
api.add_resource(GetUserByIdRoute, '/users/<int:id>')
api.add_resource(UpdateUserByIdRoute, '/users/<int:id>')
api.add_resource(DeleteUserByIdRoute, '/users/<int:id>')
