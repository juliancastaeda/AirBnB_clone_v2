#!/usr/bin/python3
"""This is the state class"""
import models
from models.base_model import BaseModel, Base
from models.city import City
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = "cities"

    if models.storage_t == 'db':
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state",
                              cascade="all, delete-orphan")
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)

    else:
        name = ''

        def __init__(self, *args, **kwargs):
            """initializes state"""
            super().__init__(*args, **kwargs)
