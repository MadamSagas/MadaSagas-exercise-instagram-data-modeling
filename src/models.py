import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er
import enum

# import os
# import sys
# from sqlalchemy import Column, ForeignKey, Integer, String, Enum, DateTime
# from sqlalchemy.orm import relationship, declarative_base
# from sqlalchemy import create_engine
# from eralchemy2 import render_er
# import enum


class MediaType(enum.Enum):
    image = "image"
    video = "video"

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    user_name = Column(String(50), unique=True ,nullable=False )
    name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    Password = Column(String(32), nullable=False)

class Post(Base):
    __tablename__= 'post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user_id_relationship = relationship(User)

class Comment(Base):
    __tablename__= 'comment'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(100))
    user_id = Column(Integer, ForeignKey('user.id'))
    user_id_relationship = relationship(User)
    post_id = Column(Integer, ForeignKey('post.id'))
    post_id_relationship = relationship(Post)

class Media(Base):
    __tablename__= 'media'
    id = Column(Integer, primary_key=True)
    type = Column(Enum(MediaType), nullable=False)
    url = Column(String(100), nullable=False)
    post_id = Column(Integer, ForeignKey('post.id'))
    post_id_relationship = relationship(Post)

class Followers(Base):
    __tablename__= 'followers'
    id = Column(Integer, primary_key=True)
    user_from =  Column(Integer, ForeignKey('user.id'))
    user_from_relationship = relationship(User)
    user_to = Column(Integer, ForeignKey('user.id'))
    user_to_relationship = relationship(User)



# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
