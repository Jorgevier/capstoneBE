from flask.views import MethodView
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_smorest import abort
from . import bp

from schemas import ResturantSchema, ResturantSchemaNested
from models import ResturantModel, UserModel

@bp.route('/resturant/<resturant_id>')
class Resturant(MethodView):

    @bp.response(200, ResturantSchemaNested)
    def get (self, resturant_id):
        resturant = None
        print(resturant_id)
        if resturant_id.isdigit():
            resturant = ResturantModel.query.get(resturant_id)
        if not resturant:
            resturant = ResturantModel.query.filter_by(username = resturant_id).first()
            print(resturant)
        if resturant:
            return resturant
        else:
            abort(400, message="Resturant user not found")
        

    @jwt_required()
    @bp.arguments(ResturantSchema)
    def put (self, resturant_data, resturant_id):
        resturant = ResturantModel.query.get(get_jwt_identity())
        if resturant and resturant.id == resturant_id:
            resturant.from_resturant_dict(resturant_data)
            resturant.commit()
            return {'message': f'{resturant.username} updated'}, 202
        abort(400, message = "Invalid resturant user")

    @jwt_required()
    def delete(self, resturant_id):
        resturant = ResturantModel.query.get(get_jwt_identity)
        if resturant == resturant_id:
            resturant.delete()
            return {'message': f'Resturant: {resturant.username} Deleted'}, 202
        return{'message': "Invalid resturant username"}, 400

@bp.route('/resturant')
class ResturantList(MethodView):

    @bp.response(200, ResturantSchema(many = True))
    def get(self):
        return ResturantModel.query.all()
    
@bp.route('/resturant/follow/<followed_id>')
class FollowResturant(MethodView):

    @jwt_required()
    def post(self, followed_id):
        followed = ResturantModel.query.get(followed_id)
        follower = UserModel.query.get(get_jwt_identity())
        if follower and followed:
            follower.follow(followed)
            followed.commit()
            return{'message': f'your are following {followed.resturant_name}'}
        else:
            return {'message': 'resturant not found'}, 400
        
        
            
   
        
