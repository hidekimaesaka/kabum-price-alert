from app.db import engine

from app.model.alert import AlertQueue

from sqlalchemy import select, update, insert

class AlertQueueRepo:

    def __init__(self) -> None:
        self.con = engine.connect()

    def get_queue(self):
        
        select_stmt = select(AlertQueue).where(AlertQueue.sent == '0')
        result = self.con.execute(select_stmt).fetchall()

        return result

    def add_queue(self, **queue):

        product_link = queue.get('product_link')
        product_price = queue.get('product_price')
        user_email = queue.get('user_email')

        query_exists = select(AlertQueue).where(
            AlertQueue.product_link == product_link,
            AlertQueue.product_price == product_price,
            AlertQueue.user_email == user_email
        )
        exists = self.con.execute(query_exists).fetchall()
        if exists:
            return False

        insert_stmt = insert(AlertQueue).values(
            product_link = product_link,
            product_price = product_price,
            user_email = user_email
        )

        self.con.execute(insert_stmt)
        self.con.commit()
    
    def remove_queue(self, id):

        update_stmt = update(AlertQueue).where(AlertQueue.id == id).values(sent='1')        

        self.con.execute(update_stmt)
        self.con.commit()
