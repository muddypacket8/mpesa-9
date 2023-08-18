from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()


class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    quantity = Column(Integer, default=0)
    price = Column(Integer, nullable=False)


    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

    def __repr__(self):
        return f"<Product(id={self.id}, name='{self.name}', quantity={self.quantity}, price={self.price})>"

    def update_quantity(self, new_quantity):
        self.quantity = new_quantity

# Create the database and establish a connection
engine = create_engine('sqlite:///store.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Create a new product
product1 = Product(name='wood', quantity=10, price=1000)
product2 = Product(name='metal', quantity=10, price=1000)
session.add(product1)
session.add(product2)
session.commit()

# Update the quantity of a product
product1.update_quantity(7)
product2.update_quantity(8)
session.commit()

# Retrieve all products
products = session.query(Product).all()
for product in products:
    print(product)

