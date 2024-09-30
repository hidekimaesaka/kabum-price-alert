from flask import Blueprint, Flask, request, jsonify

from app.repo.user import UserRepo

user = Blueprint('user', __name__)

user_repo = UserRepo()

@user.route('/user/create', methods=['POST'])
def create_user():

    new_user = request.get_json()

    status = user_repo.create_user(**new_user)

    return jsonify(msg=status)


def init(app: Flask):

    return app.register_blueprint(user)
