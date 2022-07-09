import http

from flask import Blueprint, jsonify

from models.group import Group
from serializers.group import GroupSchema

group_router = Blueprint('group', __name__, url_prefix='/group')


@group_router.route('')
def get():
    group_schema = GroupSchema()

    groups = Group.query.order_by(Group.id)
    print(groups[0].users)

    group_json = group_schema.dump(groups, many=True)
    return jsonify(group_json)
