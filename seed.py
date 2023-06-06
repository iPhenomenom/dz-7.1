from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Student, Group, Teacher, Subject, Grade
from datetime import datetime
import random

fake = Faker()

engine = create_engine('sqlite:///mydatabase.db')
Session = sessionmaker(bind=engine)

session = Session()

# создаем группы
for _ in range(3):
    group = Group(name=fake.word())
    session.add(group)

# создаем преподавателей
for _ in range(5):
    teacher = Teacher(name=fake.name())
    session.add(teacher)

# создаем предметы
for _ in range(8):
    subject = Subject(name=fake.word(), teacher_id=random.randint(1, 5))
    session.add(subject)

# создаем студентов и их оценки
for _ in range(50):
    student = Student(name=fake.name(), group_id=random.randint(1, 3))
    session.add(student)
    for _ in range(20):
        grade = Grade(student_id=student.id, subject_id=random.randint(1, 8), grade=random.randint(1, 5), date=fake.date_between(start_date='-1y', end_date='today'))
        session.add(grade)

session.commit()
