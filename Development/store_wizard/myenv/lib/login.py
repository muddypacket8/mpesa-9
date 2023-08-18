from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.exc import NoResultFound
from hashlib import sha256
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    password = Column(String(64), nullable=False)





def login(username, password):
    try:
        session = Session()

        # Retrieve the user with the provided username
        user = session.query(User).filter_by(username=username).one_or_none()

        # Validate the user's password
        if user and user.password == sha256(password.encode()).hexdigest():
            session.close()
            return "Login successful"
        else:
            session.close()
            return "Error: Invalid username or password"
    except NoResultFound:
        session.close()
        return "Error: Invalid username or password"
    except Exception as e:
        session.close()
        return "Error: " + str(e)


# Create the engine
engine = create_engine('sqlite:///login.db')

#Create a Session
Session = sessionmaker(bind=engine)
session = Session()

#Create a table defined by the class structure
Base.metadata.create_all(engine)

#Create a new instance
new_user = User(username=leon, password=password)
 
#Add the new user to the session
session.add(User)

#Commit the session
session.commit()
