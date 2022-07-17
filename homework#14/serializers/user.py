from marshmallow import Schema, fields
from marshmallow.validate import Length


class UserSchema(Schema):
    # name = fields.String(required=True, validate=Length(min=2, max=15))
    # email = fields.Email(required=True, validate=Length(min=10, max=355))
    # password = fields.String(required=True)
    id = fields.Integer(required=True, dump_only=True)
    email = fields.Email(required=True, validate=Length(min=10, max=355))