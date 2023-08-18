from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from hashlib import sha256
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    password = Column(String(64), nullable=False)
    
    def signup(username, password):
        try:
            session = Session()

            
            # Check if the username already exists
            if session.query(User).filter_by(username=username).first():
                session.close()
                return "Error: Username already exists"

            # Hash the password
            hashed_password = sha256(password.encode()).hexdigest()


            # Create a new user
            user = User(username=username, password=hashed_password)
            session.add(user)
            session.commit()
            session.close()

            return "Sign up successful"
        except Exception as e:
            session.rollback()
            session.close()
            
            return "Error: " + str(e)

# create the engine 
engine = create_engine('sqlite:///signup.db')

#Create a Session
Session = sessionmaker(bind=engine)
session = Session()

#Create a table defined by the class structure
Base.metadata.create_all(engine)

#Create a new instance
new_user = User(username="leon", password="kim2")
 
#Add the new user to the session
session.add(User)

#Commit the session
session.commit()