from django.db import models
from django.utils.html import format_html

# from sqlalchemy import Column,Integer,String,ForeignKey
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker,relationship
# from sqlalchemy.ext.declarative import declarative_base

#Post model
class User(models.Model):
    id=models.AutoField(primary_key=True)
    email=models.CharField(unique=True, max_length=100)
    fname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    password=models.CharField(max_length=30)
    

class Post(models.Model):
    post_id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=100)
    content=models.TextField()




# engine=create_engine("mysql+mysqlconnector://root:root@localhost:3306/blog",echo=True)
# Base=declarative_base()
# class User(Base):
#     __tablename__='user'
#     __table_args__={'schema':'blog'}
#     id=Column(Integer,primary_key=True)
#     email=Column(String(length=100))
#     fname=Column(String(length=100))
#     lname=Column(String(length=100))
#     password=Column(String(length=30))



# class Post(Base):
#     __tablename__='post'
#     __table_args__={'schema':'blog'}
#     post_id=Column(Integer,primary_key=True)
#     title=Column(String(length=100))
#     content=Column(String)

# Base.metadata.create_all(engine)
    
    
