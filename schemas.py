from marshmallow import Schema, fields

class ResturantSchema(Schema):
    id = fields.Str(dump_only = True)
    resturant_name = fields.Str()
    resturant_address = fields.Str()
    resturant_tel = fields.Str()
    tax_id = fields.Str()
    email = fields.Str(required=True)
    username = fields.Str(required=True)
    password = fields.Str(required=True, load_only=True)

class ResturantLogin(Schema):
    username = fields.Str(required=True)
    password = fields.Str(required=True, load_only = True)

class UserSchema(Schema):
    id = fields.Str(dump_only = True)
    first_name = fields.Str()
    last_name = fields.Str()
    email = fields.Str(required=True)
    username = fields.Str(required=True)
    password = fields.Str(required=True, load_only=True)

class UserLogin(Schema):
    username = fields.Str(required=True)
    password = fields.Str(required=True, load_only = True)

class ReviewSchema(Schema):
    id = fields.Str(dump_only=True)
    body = fields.Str(required=True)
    timestamp = fields.DateTime(dump_only = True)
    resturant_id = fields.Str(required=True)

class ResturantSchemaNested(ResturantSchema):
    reviews = fields.List(fields.Nested(ReviewSchema), dump_only=True)

class ReviewSchemaNested(ReviewSchema):
    user = fields.Nested(UserSchema, dump_only = True)

class UserSchemaNested(UserSchema):
  reviews = fields.List(fields.Nested(ReviewSchema), dump_only=True)
  followed = fields.Function(lambda user: {followed.id: UserSchema().dump(followed) for followed in user.followed} )


