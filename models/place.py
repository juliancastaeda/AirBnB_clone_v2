#!/usr/bin/python3
"""This is the place class"""
from models.base_model import BaseModel, Base
import models
import os
import sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey, Float, Table
from sqlalchemy.orm import relationship
from models.amenity import Amenity, place_amenity
from models.review import Review

class Place(BaseModel, Base):
    """ Class Place
    """
    __tablename__ = "places"
    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship("Review", backref="place",
                               cascade="all, delete-orphan")
        """
        place_amenity = Table('place_amenity', Base.metadata,
                              Column('place_id', String(60),
                                     ForeignKey('places.id'), nullable=False,
                                     primary_key=True),
                              Column('amenity_id', String(60),
                                     ForeignKey('amenities.id'),
                                     nullable=False, primary_key=True))
        """
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, default=0, nullable=False)
        number_bathrooms = Column(Integer, default=0, nullable=False)
        max_guest = Column(Integer, default=0, nullable=False)
        price_by_night = Column(Integer, default=0, nullable=False)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        amenity_ids = []

        reviews = relationship("Review", backref='place',
                               cascade='all, delete')
        amenities = relationship("Amenity",  secondary=place_amenity,
                                 back_populates="place_amenities",
                                 viewonly=False)
    else:
        city_id = ''
        user_id = ''
        name = ''
        description = ''
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def reviews(self):
            review = models.storage.all(Review)
            relation = []
            for key in review.values():
                if key.place.id == self.id:
                    relation.append(key)
            return relation

        @property
        def amenities(self):
            amenity = models.storage.all()
            relation = []
            for key in amenity:
                if key.place.id == self.id and\
                        obj.__class.__.__name__ == 'Amenity':
                    relation.append(key)
            return relation

        @amenities.setter
        def amenities(self, value):
            if value.__class__.__name__ == 'Amenity':
                    self.amenity_ids.append(value.amenities.id)
