from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

# create db engine and bind to new session and objects
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()

# query all restaurants and menu items
print(session.query(Restaurant).all())
print(session.query(MenuItem).all())

# query first restaurant
firstRest = session.query(Restaurant).first()

# query filter by name
cheesePizzas = session.query(MenuItem).filter_by(name = "Cheese Pizza")