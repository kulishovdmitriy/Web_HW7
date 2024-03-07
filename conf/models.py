from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()


class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    fullname = Column(String(155), nullable=False)
    group_id = Column('group_id', ForeignKey('groups.id', ondelete='CASCADE'))


class Group(Base):
    __tablename__ = 'groups'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)


class Teacher(Base):
    __tablename__ = 'teachers'
    id = Column(Integer, primary_key=True)
    fullname = Column(String(155), nullable=False)


class Subject(Base):
    __tablename__ = 'subjects'
    id = Column(Integer, primary_key=True)
    name = Column(String(155), nullable=False)
    teacher_id = Column('teacher_id', ForeignKey('teachers.id', ondelete='CASCADE'))
    teacher = relationship('Teacher', backref='disciplines')


class Grade(Base):
    __tablename__ = 'grades'
    id = Column(Integer, primary_key=True)
    grade = Column(Integer, nullable=False)
    data_of = Column('data_of', Date, nullable=True)
    student_id = Column('student_id', ForeignKey('students.id', ondelete='CASCADE'))
    subject_id = Column('subject_id', ForeignKey('subjects.id', ondelete='CASCADE'))
    student = relationship('Student', backref='grade')
    discipline = relationship('Discipline', backref='grade')


class Discipline(Base):
    __tablename__ = 'disciplines'
    id = Column(Integer, primary_key=True)
    student_id = Column('student_id', ForeignKey('students.id', ondelete='CASCADE'))
    student = relationship('Student', backref='disciplines')
    subject = relationship('Subjects', backref='disciplines')


