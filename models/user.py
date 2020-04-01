#!/usr/bin/python3
"""This is the user class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column,Integer,Sequence, String
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class User(BaseModel, base):
    """This is the class for user
    Attributes:
        email: email address
        password: password for you login
        first_name: first name
        last_name: last name
    """
    if getenv('HBNB_TYPE_STORAGE') == DBStorage:
        __tablename__ = 'users'
        email = Column(String(128), unique=True, nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128)), nullable=True)

    elif getenv('HBNB_TYPE_STORAGE') == FileStorage:
        email = ""
        password = ""
        first_name = ""
        lastname = ""
