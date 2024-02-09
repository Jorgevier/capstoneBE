from flask_jwt_extended import create_access_token

from models import ResturantModel

from . import bp
from schemas import ResturantLogin, ResturantSchema

@bp.post('/resturantlogin')
@bp.arguments(ResturantLogin)
def login(resturant_data):
    resturant = ResturantModel.query.filter_by(username = resturant_data['username']).first()
    if resturant and resturant.check_password(resturant_data['password']):
        acces_token = create_access_token(resturant.id)
        return {'token': acces_token}
    return {'message': 'Invalid resturant user data'}

@bp.post('/resturantregister')
@bp.arguments(ResturantSchema)
def register(resturant_data):
    try:
        resturant = ResturantModel()
        resturant.from_resturant_dict(resturant_data)
        resturant.commit()
        return {'message': f'{resturant_data["username"]} created'}, 200
    except:
        return {'message':'Resturant Username or email is already used'}, 400

