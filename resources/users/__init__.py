from flask_smorest import Blueprint

bp = Blueprint('user', __name__, description="Operation for Users")

from . import routes, auth_routes