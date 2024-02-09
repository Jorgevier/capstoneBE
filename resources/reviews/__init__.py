from flask_smorest import Blueprint
bp = Blueprint('reviews', __name__, description=' ops for reviews', url_prefix='/reviews')

from . import routes