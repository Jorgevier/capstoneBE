from datetime import datetime

from app import db

class ReviewModel(db.Model):

    __tablename__ = 'reviews'

    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String, nullable = False)
    timestamp = db.Column(db.DateTime, default = datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False)
    user = db.relationship('UserModel', back_populates = 'reviews')
    resturant_id = db.Column(db.Integer, db.ForeignKey('resturant.id'), nullable = False)
    resturant = db.relationship('ResturantModel', back_populates = 'reviews')

    def __repr__(self):
        return f'<Review: {self.body}>'
    
    def commit(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
    