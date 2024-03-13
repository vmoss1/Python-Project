from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Mapped, mapped_column

db = SQLAlchemy()

class Image(db.Model):
  __tablename__ = 'images'
  id: Mapped[int] = mapped_column(primary_key=True)
  image: Mapped[str] = mapped_column(nullable=False)
