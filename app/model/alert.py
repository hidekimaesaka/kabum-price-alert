from app.db import Base

from sqlalchemy import String

from sqlalchemy.orm import Mapped, mapped_column

class AlertQueue(Base):

    __tablename__ = 'alert_queue'

    id: Mapped[int] = mapped_column(primary_key=True)
    product_link: Mapped[str] = mapped_column(String())
    product_price: Mapped[str] = mapped_column(String())
    user_email: Mapped[str] = mapped_column(String())
