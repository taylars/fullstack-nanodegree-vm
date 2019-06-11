from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

# create db engine and bind to new session and objects
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()

# query filter by id and update price
ogCheesePizza = session.query(MenuItem).filter_by(id = "1").one()
ogCheesePizza.price = '$4.99'
session.add(ogCheesePizza)
session.commit()

# query filter by name and delete one
oneCheesePizza = session.query(MenuItem).filter_by(name = "Cheese Pizza")[0]
session.delete(oneCheesePizza)
session.commit()