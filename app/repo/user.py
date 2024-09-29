from app.db import engine

from app.model.user import User

from sqlalchemy import insert, select

class UserRepo:

    def __init__(self) -> None:
        self.con = engine.connect()

    def get_user_by_id(self, id):

        select_stmt = select(User).where(User.id == id)
        result = self.con.execute(select_stmt).fetchall()

        return result

    def create_user(self, **user):
        
        name = user.get('name')
        mail = user.get('mail')

        if not name or not mail: return False

        insert_stmt = insert(User).values(
            name=name,
            mail=mail
        )

        self.con.execute(insert_stmt)
        self.con.commit()

        return True
