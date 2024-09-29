from flask import Flask

from app import scheduler

from app.routes import user
from app.routes import product

from app.extensions import cors

def create_app():

    app = Flask(__name__)

    cors.init(app)

    user.init(app)
    product.init(app)

    scheduler.init()

    return app
