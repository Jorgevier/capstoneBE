from flask_jwt_extended import jwt_required, get_jwt_identity
from flask.views import MethodView
from flask_smorest import abort

from models import ReviewModel
from schemas import ReviewSchema, ReviewSchemaNested

from . import bp 

@bp.route('<review_id>')
class Review(MethodView):

    @bp.response(200, ReviewSchemaNested)
    def get(self, review_id):
        review = ReviewModel.query.get(review_id)
        if review:
            return review
        abort(400, message='Invalid Review')

    @jwt_required
    @bp.arguments(ReviewSchema)
    def put(self, review_data, review_id):
        review = ReviewModel.query.get(review_id)
        if review and review.user_id == get_jwt_identity():
            review.body = review_data['body']
            review.commit()
            return {'message': 'review updated'}, 201
        return {'message': 'Invalid review ID'}, 400
    
    @jwt_required()
    def delete(self, review_id):
        review = ReviewModel.query.get(review_id)
        if review and review.user_id == get_jwt_identity():
            review.delete()
            return{'message': 'Review deleted'}, 202
        return {'message': 'Invalid review or user'}, 400
    
    @bp.route('/', methods=['GET','POST'])
    class ReviewList(MethodView):

        @bp.response(200, ReviewSchemaNested(many = True))
        def get(self):
            return ReviewModel.query.all()
        
        @jwt_required()
        @bp.arguments(ReviewSchema)
        def post(self, review_data):
            try:
                review = ReviewModel()
                review.user_id = get_jwt_identity()
                review.body = review_data['body']
                review.resturant_id = review_data['resturant_id']
                review.commit()
                return {'message': "Review created"}, 201
            except:
                return {'message':'invalid user'}, 401
            



