from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from dotenv import load_dotenv

from routes.users import *
from routes.contacts import *

load_dotenv()

app = Flask(__name__)

api = Api(app)
CORS(app)


# users routes

api.add_resource(CreateUserRoute, '/users')
api.add_resource(GetUserInfoRoute, '/users')
api.add_resource(UpdateUserByIdRoute, '/users')
api.add_resource(DeleteUserByIdRoute, '/users')
api.add_resource(LoginUserRoute, '/login')
api.add_resource(RefreshTokenRoute, '/refresh_token')


# Contacts routes

api.add_resource(CreateContactRoute, '/contacts')
api.add_resource(ListAllContactByUserIdRoute, '/contacts')
api.add_resource(UpdateContactByIdRoute, '/contacts/<int:id>')
api.add_resource(DeleteContactByIdRoute, '/contacts/<int:id>')
api.add_resource(ListContactByIdRoute, '/contacts/<int:id>')

if __name__ == "__main__":
    app.run(debug=True, port=5000)
