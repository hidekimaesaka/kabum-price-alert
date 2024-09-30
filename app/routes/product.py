from flask import Flask, Blueprint, request, jsonify

from app.repo.product import ProductRepo
from app.repo.user import UserRepo

product = Blueprint('product', __name__)

user_repo = UserRepo()
product_repo = ProductRepo()

@product.route('/product/create', methods=['POST'])
def create_product():

    product = request.get_json()

    user_email = product.get('user_mail')
    user = user_repo.get_user_by_email(user_email)

    product['user_id'] = user[0].id

    created = product_repo.create_product(**product)

    return jsonify(product_created=created)


def init(app: Flask):
    return app.register_blueprint(product)
