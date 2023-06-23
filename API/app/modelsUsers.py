from sqlalchemy import Column, Integer, Date, JSON, String, Boolean
from app.db import Base

#Authentification
class Users(Base):
    __tablename__ = 'users2'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(4),  unique=True, index=True)
    password_hashed = Column(String(60))
    disabled = Column(Boolean, default=True)
