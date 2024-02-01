from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from internal.database.postgres import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True)
