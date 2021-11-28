from flask import Flask
from flask_restful import Api
from flask_cors import CORS

from routes.users import *
from routes.emails import *
from routes.phones import *
from routes.contacts import *

app = Flask(__name__)

api = Api(app)

# users routes

api.add_resource(CreateUserRoute, '/users')
api.add_resource(GetUserByIdRoute, '/users/<int:id>')
api.add_resource(UpdateUserByIdRoute, '/users/<int:id>')
api.add_resource(DeleteUserByIdRoute, '/users/<int:id>')

# emails routes

api.add_resource(CreateEmailRoute, '/emails')
api.add_resource(UpdateEmailByIdRoute, '/emails/<int:id>')
api.add_resource(DeleteEmailByIdRoute, '/emails/<int:id>')

# phones routes

api.add_resource(CreatePhoneRoute, '/phones')
api.add_resource(UpdatePhoneByIdRoute, '/phones/<int:id>')
api.add_resource(DeletePhoneByIdRoute, '/phones/<int:id>')

# Contacts routes

api.add_resource(CreateContactRoute, '/contacts')
api.add_resource(ListAllContactByUserIdRoute, '/contacts/<int:id>')
api.add_resource(UpdateContactByIdRoute, '/contacts/<int:id>')
api.add_resource(DeleteContactByIdRoute, '/contacts/<int:id>')

if __name__ == "__main__":
    app.run(debug=True, port=3000)
