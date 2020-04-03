#!/usr/bin/python3
"""
New engine DBStorage
"""
import models
from models.amenity import Amenity
from models.base_model import BaseModel, Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from os import getenv
import os
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


class DBStorage:
    """interaacts with the MySQL database"""
    __engine = None
    __session = None

    def __init__(self):
        """Instantiate a DBStorage object"""
        HBNB_MYSQL_USER = os.environ.get('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = os.environ.get('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST = os.environ.get('HBNB_MYSQL_HOST')
        HBNB_MYSQL_DB = os.environ.get('HBNB_MYSQL_DB')
        HBNB_ENV = getenv('HBNB_ENV')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(HBNB_MYSQL_USER,
                                             HBNB_MYSQL_PWD,
                                             HBNB_MYSQL_HOST,
                                             HBNB_MYSQL_DB))
        if (os.environ.get('HBNB_MYSQL_USER') == "test"):
            Base.metadata.drop.all(bind=self.__engine)

    def all(self, cls=None):
        """ Function all """
        lists = {}
        classes = {'State': State, 'City': City}
        """
        classes = {'Place': Place, 'City': City, 'Amenity': Amenity,
        'Review': Review, 'State': State, 'User': User}"""

        if cls:
            for row in self.__session.query(classes[cls]):
                key = "{}.{}".format(row.__class__.__name__, row.id)
                lists[key] = row
        else:
            for rows in classes:
                for row in self.__session.query(classes[rows]):
                    key = "{}.{}".format(row.__class__.__name__, row.id)
                    lists[key] = row
        return lists

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)
        self.save()

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session"""
        if obj is not None:
            self.__session.delete(obj)
            self.save()

    def reload(self):
        """reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine,
                                    expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

    def close(self):
        """call remove() method on the private session attribute"""
        self.__session.remove()
