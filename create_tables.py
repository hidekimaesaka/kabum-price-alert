from app.db import Base, engine

from app.model.user import User
from app.model.product import Product
from app.model.alert import AlertQueue

Base.metadata.create_all(engine)
