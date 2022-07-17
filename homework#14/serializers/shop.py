from marshmallow import Schema, fields
from marshmallow.validate import Length


class ShopSchema(Schema):
    id = fields.Integer(required=True, dump_only=True)
    name_of_good = fields.Str(required=True)
    maker = fields.Str(required=True)
    category_of_good = fields.Str(required=True)
