from sqlalchemy import Column, Integer, String

from Models.Database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    google_id = Column(String, unique=True)
    email = Column(String, unique=True)
    name = Column(String)
    picture = Column(String)
