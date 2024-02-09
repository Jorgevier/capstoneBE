from app import db

from werkzeug.security import generate_password_hash, check_password_hash

class ResturantModel(db.Model):

    __tablename__ = 'resturant'

    id = db.Column(db.Integer, primary_key = True)
    resturant_name = db.Column(db.String(30))
    resturant_address = db.Column(db.String(300))
    resturant_tel = db.Column(db.String(30))
    tax_id = db.Column(db.String(30))
    email = db.Column(db.String(75), nullable = False, unique=True)
    username = db.Column(db.String(30), nullable = False, unique=True)
    password_hash = db.Column(db.String(250), nullable = False)

    reviews = db.relationship('ReviewModel', back_populates='resturant', lazy='dynamic', cascade= 'all, delete')


    def __repr__(self):
        return f'<User: {self.username}>'
    
    def commit(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def from_resturant_dict(self, rest_dict):
        for k, v in rest_dict.items():
            if k != 'password':
                setattr(self, k, v)
            else:
                setattr(self, 'password_hash', generate_password_hash(v))
            
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)




