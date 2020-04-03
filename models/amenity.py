#!/usr/bin/python3
"""This is the amenity class"""
from models.base_model import BaseModel, Base
import os
from sqlalchemy import Column, Table, ForeignKey, String
from sqlalchemy.orm import relationship

place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60),
                             ForeignKey('places.id'), nullable=False,
                             primary_key=True),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'), nullable=False,
                             primary_key=True))


class Amenity(BaseModel, Base):
    """This is the class for Amenity
    Attributes:
        name: input name
    """

    __tablename__ = "amenities"
    if os.getenv("HBNB_TYPE_STORAGE") == 'db':
        name = Column(String(128), nullable=False)
        place_amenities = relationship("Place", secondary="place_amenity")
