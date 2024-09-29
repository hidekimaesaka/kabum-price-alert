from app.db import engine

from app.model.product import Product

from sqlalchemy import insert, select, update

class ProductRepo:

    def __init__(self) -> None:
        self.con = engine.connect()

    def create_product(self, **product):

        user_id = product.get('user_id')
        product_link = product.get('product_link')
        product_desired_price = product.get('product_desired_price')

        is_valid = user_id or product_link or product_desired_price

        if not is_valid: return False

        insert_stmt = insert(Product).values(
            user_id = user_id,
            product_link = product_link,
            product_desired_price = product_desired_price
        )

        self.con.execute(insert_stmt)
        self.con.commit()

        return True

    def get_products(self):

        select_stmt = select(Product)

        query = self.con.execute(select_stmt)
        query_result = query.all()

        return query_result

    def get_products_to_alert(self):

        select_stmt = select(Product).where(Product.product_actual_price != None)

        query = self.con.execute(select_stmt)
        query_result = query.all()

        return query_result

    def update_product_price(self, id, price):

        update_stmt = update(Product).where(Product.id == id).values(product_actual_price=price)

        self.con.execute(update_stmt)
        self.con.commit()
