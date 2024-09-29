from flask import Flask, Blueprint, request, jsonify

from app.repo.product import ProductRepo

product = Blueprint('product', __name__)

product_repo = ProductRepo()

@product.route('/product/create', methods=['POST'])
def create_product():

    product = request.get_json()

    created = product_repo.create_product(**product)

    return jsonify(product_created=created)


def init(app: Flask):
    return app.register_blueprint(product)
