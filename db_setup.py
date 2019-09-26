from sqlalchemy import Column,Integer,String,Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship
from flask_login import UserMixin

Base=declarative_base()

class Register(Base):
	__tablename__='register'

	id =Column(Integer,primary_key=True)
	name=Column(String(30))
	email=Column(String(40))
	pwd=Column(String(20))
	des=Column(String(30))

class User(Base,UserMixin):
	__tablename__='user'

	id =Column(Integer,primary_key=True)
	name=Column(String(50))
	email=Column(String(40))
	pwd=Column(String(20))

#engine=create_engine('sqlite:///regiter.db')
engine = create_engine('postgresql://catalog:catalog@localhost/catalog')
Base.metadata.create_all(engine)
print("DB is Created!!")
