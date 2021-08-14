from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from db import Base, engine

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String , unique=True , nullable=False)
    password = Column(String , nullable=False)
    test_host = Column(String)
    test_names = relationship("Test_name" , back_populates="user")
    def __repr__(self):
        return f'<User {self.name} {self.password} {self.test_host} >'


class Test_name(Base):
    __tablename__ = 'test_names'
    id = Column(Integer, primary_key=True)
    name_of_test = Column(String , nullable=False)
    user_id = Column(Integer , ForeignKey("users.id") )
    user = relationship("User" , back_populates="test_names")
    question = relationship("Question" , back_populates="test_name")
    
    def __repr__(self):
        return f'<Test_name {self.id} {self.name_of_test} {self.user_id} >'


class Question(Base):
    __tablename__ = 'questions'
    id = Column(Integer, primary_key=True)
    question = Column(String , nullable=False)
    test_id = Column(Integer , ForeignKey("test_names.id")  )
    test_name = relationship("Test_name" , back_populates="question")
    answer = relationship("Answer" , back_populates="question")
    answer_id = Column(Integer , ForeignKey("answers.id") )
    
    def __repr__(self):
        return f'<Question {self.name} {self.question}>'


class Answer(Base):
    __tablename__ = 'answers'
    id = Column(Integer, primary_key=True)
    question_id = (Integer , ForeignKey("questions.id")) 
    question = relationship("Question" , back_populates="answer")
    answer = Column(String , nullable=False)
    accuracy = Column(Integer)
       
    def __repr__(self):
        return f'<Answer {self.question} {self.answer} {self.accuracy}>'


if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)