import http

from flask import Blueprint, Response, request, jsonify
from marshmallow import ValidationError

from database import db
from models.shop import Shop
from serializers.shop import ShopSchema

shop_router = Blueprint('shop', __name__, url_prefix='/shop')

@shop_router.route('')
def get_list_of_goods():
    shop_schema = ShopSchema()

    goods_of_shop = Shop.query.order_by(Shop.name_of_good)
    goods_json = shop_schema.dump(goods_of_shop, many=True)
    return jsonify(goods_json)


@shop_router.route('/<int:id_>')
def retrieve(id_):
    shop_schema = ShopSchema()
    good_by_id = Shop.query.filter_by(id=id_).first()
    good_by_id_json = shop_schema.dump(good_by_id)
    return jsonify(good_by_id_json)


@shop_router.route('', methods=['POST'])
def create():
    data = request.get_json(force=True)

    schema = ShopSchema()
    try:
        goods_data = schema.load(data)
        new_product = Shop(name_of_good=goods_data['name_of_good'], maker=goods_data['maker'], category_of_good=goods_data['category_of_good'])
        db.session.add(new_product)
        db.session.commit()

        new_product_json = schema.dump(new_product)
    except ValidationError as e:
        return {'errors': e.messages}, http.HTTPStatus.UNPROCESSABLE_ENTITY

    return new_product_json


@shop_router.route('/<int:id_>', methods=['PUT'])
def update(id_):
    data = request.get_json(force=True)

    schema = ShopSchema()
    try:
        product_data = schema.load(data)
        product = Shop.query.filter_by(id=id_).first()
        product.name_of_good = product_data['name_of_good']
        product.maker = product_data['maker']
        product.category_of_good = product_data['goods_data']
        db.session.add(product)
        db.session.commit()

        new_product_data_json = schema.dump(product)
    except ValidationError as e:
        return {'errors': e.messages}, http.HTTPStatus.UNPROCESSABLE_ENTITY

    return new_product_data_json


@shop_router.route('/<int:id_>', methods=['DELETE'])
def delete(id_):
    Shop.query.filter_by(id=id_).delete()
    db.session.commit()
    return {}, http.HTTPStatus.NO_CONTENT