from marshmallow import Schema, fields
from marshmallow.validate import Length

from serializers.user import UserSchema


class GroupSchema(Schema):
    id = fields.Integer(required=True, dump_only=True)
    name = fields.String(required=True, validate=Length(min=2, max=355))
    description = fields.String(required=False)
    user = fields.List(fields.Nested(UserSchema))
