from flask import Blueprint
from .apis import *

users_api = Blueprint('users_api', __name__)

users_api.route('/list', methods=['GET'])(test)