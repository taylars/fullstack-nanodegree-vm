from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem


class RestDb:
    def __init__(self):
        # create db engine and bind to new session and objects
        engine = create_engine('sqlite:///restaurantmenu.db')
        Base.metadata.bind = engine
        DBSession = sessionmaker(bind = engine)
        self.__session = DBSession()
    
    def getAllRestaurants(self):
        return self.__session.query(Restaurant).all()