import http

from flask import Blueprint, Response, request

from db.bookdb import BookDB

book_router = Blueprint('book', __name__, url_prefix='/book')
db = BookDB()


@book_router.route('')
def get():
    books = db.get_all()
    return Response(str(books))


@book_router.route('/<id>')
def retrieve(id):
    book = db.retrieve_by_id(id)
    return book


@book_router.route('', methods=['POST'])
def create():
    name = request.json.get("name")
    author = request.json.get("author")
    new_book = db.add(name, author)

    if not new_book:
        return "This book is already exists", http.HTTPStatus.BAD_REQUEST
    else:
        return new_book, http.HTTPStatus.CREATED



@book_router.route('/<id>', methods=['PUT'])
def update(id):
    name = request.json.get("name")
    author = request.json.get("author")
    updated_user = db.update_by_id(name, id, author)

    return updated_user


@book_router.route('/<id>', methods=['DELETE'])
def delete(id):
    result = db.delete_by_id(id)
    return result