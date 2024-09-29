from app.db import Base

from sqlalchemy import String

from sqlalchemy.orm import Mapped, mapped_column

class User(Base):

    __tablename__ = 'user'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String())
    mail: Mapped[str] = mapped_column(String(), unique=True)
