from flask_smorest import Blueprint

bp = Blueprint('resturant', __name__, description="Operation for Resturant users")

from . import routes, auth_routes