from flask import Flask
from flask import Blueprint
from flask import current_app as app
from main.auth import token_required
from main.user.models import User
from flask_cors import CORS, cross_origin

app = Flask(__name__)
app.config['SECRET_KEY'] = 'the quick brown fox jumps over the lazy   dog'
app.config['CORS_HEADERS'] = 'Content-Type'

cors = CORS(app, resources={r"/user": {"origins": "http://localhost:5000"}})

user_blueprint = Blueprint("user", __name__)

@user_blueprint.route("/", methods=["GET"])
@token_required
def get():
	return User().get()

@user_blueprint.route("/auth/", methods=["GET"])
def getAuth():
	return User().getAuth()

@user_blueprint.route("/login", methods=["POST"])
def login():
	return User().login()

@user_blueprint.route("/logout/", methods=["GET"])
def logout():
	return User().logout()

@user_blueprint.route("/register", methods=["POST"])
# @cross_origin() # allow all origins all methods.
def add():
	return User().add()