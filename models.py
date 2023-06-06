from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    group_id = Column(Integer, ForeignKey('groups.id'))
    grades = relationship('Grade', backref='student')

class Group(Base):
    __tablename__ = 'groups'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    students = relationship('Student', backref='group')

class Teacher(Base):
    __tablename__ = 'teachers'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    subjects = relationship('Subject', backref='teacher')

class Subject(Base):
    __tablename__ = 'subjects'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    teacher_id = Column(Integer, ForeignKey('teachers.id'))
    grades = relationship('Grade', backref='subject')

class Grade(Base):
    __tablename__ = 'grades'
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('students.id'))
    subject_id = Column(Integer, ForeignKey('subjects.id'))
    grade = Column(Integer)
    date = Column(Date)
