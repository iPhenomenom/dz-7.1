from sqlalchemy import func
from sqlalchemy.orm import Session
from models import Student, Group, Teacher, Subject, Grade

def select_1(session: Session):
    return session.query(Student.name, func.avg(Grade.grade))\
                  .join(Grade)\
                  .group_by(Student.name)\
                  .order_by(func.avg(Grade.grade).desc())\
                  .limit(5)\
                  .all()

def select_2(session: Session, subject_name: str):
    return session.query(Student.name, func.avg(Grade.grade))\
                  .join(Grade)\
                  .join(Subject)\
                  .filter(Subject.name == subject_name)\
                  .group_by(Student.name)\
                  .order_by(func.avg(Grade.grade).desc())\
                  .first()

def select_3(session: Session, group_name: str, subject_name: str):
    return session.query(func.avg(Grade.grade))\
                  .join(Student)\
                  .join(Group)\
                  .join(Subject)\
                  .filter(Group.name == group_name, Subject.name == subject_name)\
                  .scalar()

def select_4(session: Session):
    return session.query(func.avg(Grade.grade)).scalar()

def select_5(session: Session, teacher_name: str):
    return session.query(Subject.name)\
                  .join(Teacher)\
                  .filter(Teacher.name == teacher_name)\
                  .all()

def select_6(session: Session, group_name: str):
    return session.query(Student.name)\
                  .join(Group)\
                  .filter(Group.name == group_name)\
                  .all()

def select_7(session: Session, group_name: str, subject_name: str):
    return session.query(Student.name, Grade.grade)\
                  .join(Grade)\
                  .join(Group)\
                  .join(Subject)\
                  .filter(Group.name == group_name, Subject.name == subject_name)\
                  .all()

def select_8(session: Session, teacher_name: str):
    return session.query(func.avg(Grade.grade))\
                  .join(Subject)\
                  .join(Teacher)\
                  .filter(Teacher.name == teacher_name)\
                  .scalar()

def select_9(session: Session, student_name: str):
    return session.query(Subject.name)\
                  .join(Grade)\
                  .join(Student)\
                  .filter(Student.name == student_name)\
                  .all()

def select_10(session: Session, student_name: str, teacher_name: str):
    return session.query(Subject.name)\
                  .join(Grade)\
                  .join(Student)\
                  .join(Teacher)\
                  .filter(Student.name == student_name, Teacher.name == teacher_name)\
                  .all()
