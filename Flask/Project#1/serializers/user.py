from marshmallow import Schema, fields
from marshmallow.validate import Length


class UserSchema(Schema):
    id = fields.Integer(required=True, dump_only=True)
    email = fields.Email(required=True, validate=Length(min=10, max=355))
    first_name = fields.String(required=True)
    last_name = fields.String(required=True)
    password = fields.String(required=True, load_only=True)
