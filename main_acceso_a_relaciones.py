import datetime
#from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, create_engine
import sqlalchemy
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.orm import declarative_base
from sqlalchemy.exc import NoResultFound

engine = create_engine('postgresql://postgres:root@localhost/pythondb')
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer(), primary_key=True)
    username = Column(String(50), nullable=False, unique=True)
    email = Column(String(50), nullable=False, unique=True)
    created_at = Column(DateTime(), default=datetime.datetime.now)
    courses = relationship('Course', backref='user')
    
    def __str__(self):
        return self.username
    
    
class Course(Base):
    __tablename__ = 'courses'
    
    id = Column(Integer(), primary_key=True)
    title =  Column(String(50), nullable=False, unique=True)
    user_id = Column(ForeignKey('users.id'))
    created_at = Column(DateTime(), default=datetime.datetime.now)
    
    def __str__(self):
        return self.title
    
Session = sessionmaker(engine)   
session = Session() 

if __name__ == '__main__':
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    
    user1 = User(username='user1', email='user1@example.com')
    user2 = User(username='user2', email='user2@example.com')
    
    course1 = Course(title='Curso profesional de Base de datos')
    
    user1.courses.append(
        course1
    )
    user1.courses.append(
        Course(title='Curso profesional de Python')
    )
    user1.courses.append(
        Course(title='Curso profesional de Go')
    )
    
    session.add(user1)
    session.add(user2)
    
    session.commit()
    
    print(course1.id)