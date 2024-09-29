from flask import Flask

from app import scheduler

from app.routes import user
from app.routes import product


def create_app():

    app = Flask(__name__)

    user.init(app)
    product.init(app)

    scheduler.init()

    return app
