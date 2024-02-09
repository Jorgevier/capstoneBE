from app import db

from models.resturant_model import ResturantModel


from werkzeug.security import generate_password_hash, check_password_hash

following = db.Table( 'following',
    db.Column('follower_id', db.Integer, db.ForeignKey('users.id')),
    db.Column('followed_id', db.Integer, db.ForeignKey('resturant.id'))                    
)

class UserModel(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(30))
    last_name = db.Column(db.String(30))
    email = db.Column(db.String(75), nullable = False, unique=True)
    username = db.Column(db.String(30), nullable = False, unique=True)
    password_hash = db.Column(db.String(250), nullable = False)
    followed = db.relationship('ResturantModel',
                               secondary = 'following',
                               primaryjoin = following.c.follower_id == id,
                               secondaryjoin = following.c.followed_id == ResturantModel.id,
                               backref = db.backref('following', lazy = 'dynamic'))

    reviews = db.relationship('ReviewModel', back_populates='user', lazy='dynamic', cascade= 'all, delete')

    def __repr__(self):
        return f'<User: {self.username}>'
    
    def commit(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def from_dict(self, user_dict):
        for k, v in user_dict.items():
            if k != 'password':
                setattr(self, k, v)
            else:
                setattr(self, 'password_hash', generate_password_hash(v))
            
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def is_following(self, resturant):
        return resturant in self.followed
  
    def follow(self, resturant):
        if self.is_following(resturant):
            return
        self.followed.append(resturant)

    def unfollow(self,resturant):
        if not self.is_following(resturant):
            return
        self.followed.remove(resturant)




