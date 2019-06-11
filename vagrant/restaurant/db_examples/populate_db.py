from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

# create db engine and bind to new session and objects
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()

# create new Restaurant and add to session
myFirstRestaurant = Restaurant(name= "Pizza Palace")
session.add(myFirstRestaurant)

# create new MenuItem and add to session
cheesePizza = MenuItem(name = "Cheese Pizza", description = "Made with all natural ingredients and fresh mozzarella", course = "Entree", price = "$8.99", restaurant = myFirstRestaurant)
session.add(cheesePizza)

# commit changes to db
session.commit()