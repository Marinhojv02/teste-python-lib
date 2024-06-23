from sqlalchemy import Column, Integer, String
from .database import Base

class UserModel(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)

    def __repr__(self):
        return f"<User(name={self.name}, email={self.email})>"
