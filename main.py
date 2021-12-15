from flask import Flask
from flask_restful import Api
from flask_cors import CORS

from routes.users import *
from routes.contacts import *
from routes.authentication import *

app = Flask(__name__)

api = Api(app)
CORS(app)

# authentication routes
api.add_resource(LoginRoute, '/session')
api.add_resource(RefreshTokenRoute, '/refresh_token')

# users routes

api.add_resource(CreateUserRoute, '/users')
api.add_resource(GetUserInfoRoute, '/me')
api.add_resource(UpdateUserByIdRoute, '/users')
api.add_resource(DeleteUserByIdRoute, '/users')

# Contacts routes

api.add_resource(CreateContactRoute, '/contacts')
api.add_resource(ListAllContactByUserIdRoute, '/contacts')
api.add_resource(UpdateContactByIdRoute, '/contacts/<int:id>')
api.add_resource(DeleteContactByIdRoute, '/contacts/<int:id>')
api.add_resource(ListContactByIdRoute, '/contacts/<int:id>')

if __name__ == "__main__":
    app.run(debug=True, port=5000)
