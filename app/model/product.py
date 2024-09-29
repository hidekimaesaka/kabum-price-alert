from app.db import Base

from datetime import datetime

from sqlalchemy import String, Integer

from sqlalchemy.orm import Mapped, mapped_column

class Product(Base):

    __tablename__ = 'product'

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer())
    date_inserted: Mapped[datetime] = mapped_column(default=datetime.now())
    product_link: Mapped[str] = mapped_column(String())
    product_desired_price: Mapped[str] = mapped_column(String())
    product_actual_price: Mapped[str] = mapped_column(String(), nullable=True)
