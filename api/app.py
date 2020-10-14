import os
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from database import initialize_db
from flask_restful import Api
from resources.routes import initialize_routes

app = Flask(__name__)

app.config["JWT_SECRET_KEY"] = os.environ.get("JWT_SECRET_KEY")

api = Api(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

app.config["MONGODB_SETTINGS"] = {
    'host': os.environ.get('DB')
}

initialize_db(app)
initialize_routes(api)

app.run(host="0.0.0.0", debug=True)
