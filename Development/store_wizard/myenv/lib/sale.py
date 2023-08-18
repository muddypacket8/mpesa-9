from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from datetime import datetime


Base = declarative_base()

class Sale(Base):
    __tablename__ = 'sales'
    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customers.id'))
    product_id = Column(Integer, ForeignKey('products.id'))
    quantity = Column(Integer, nullable=False)
    total_amount = Column(Integer, nullable=False)
    sale_date = Column(DateTime, default=datetime.now())

    customer = relationship("Customer", backref="sales")
    product = relationship("Product", backref="sales")

    def __init__(self, customer, product, quantity, total_amount):
        self.customer = customer
        self.product = product
        self.quantity = quantity
        self.total_amount = total_amount

    def __repr__(self):
        return f"<Sale(id={self.id}, customer='{self.customer.name}', product='{self.product.name}', " \
               f"quantity={self.quantity}, total_amount={self.total_amount}, sale_date={self.sale_date})>"

# Create the database and establish a connection
engine = create_engine('sqlite:///store.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Create a sale
sale1 = Sale(customer=customer1, product=product1, quantity=5, total_amount=5)
session.add(sale1)
session.commit()

# Retrieve all sales
sales = session.query(Sale).all()
for sale in sales:
    print(sale)
