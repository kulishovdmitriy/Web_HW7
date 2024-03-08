from faker import Faker
from conf.models import Teacher, Subject, Student, Grade, Group, Discipline
from conf.conect import session

import random

fake = Faker()

def init():
    # Создание групп, студентов и привязка их к группам
    for _ in range(3):
        group_name = fake.word()
        group = Group(name=group_name)
        session.add(group)
        session.commit()

        for _ in range(random.randint(10, 20)):
            student_name = fake.name()
            student = Student(name=student_name, group_id=group.id)
            session.add(student)
            session.commit()

    # Создание учителей и предметов, а также привязка предметов к учителям
    for _ in range(5):
        teacher_name = fake.name()
        teacher = Teacher(name=teacher_name)
        session.add(teacher)
        session.commit()

        for _ in range(random.randint(2, 5)):
            subject_name = fake.word()
            subject = Subject(name=subject_name, teacher_id=teacher.id)
            session.add(subject)
            session.commit()

    # Получение всех идентификаторов студентов и предметов
    students_ids = [student.id for student in session.query(Student.id).all()]
    subjects_ids = [subject.id for subject in session.query(Subject.id).all()]

    # Создание оценок для студентов по всем предметам
    for student_id in students_ids:
        for subject_id in subjects_ids:
            grade = random.randint(0, 100)
            date = fake.date_between(start_date='-1y', end_date='today')
            grade = Grade(student_id=student_id, subject_id=subject_id, grade=grade, date=date)
            session.add(grade)
            session.commit()

    # Создание записей об учебном процессе (enrollments)
    for _ in range(50):
        student_id = random.randint(1, 50)
        subject_id = random.randint(1, 9)
        discipline = Discipline(student_id=student_id, subject_id=subject_id)
        session.add(discipline)
        session.commit()


if __name__ == '__main__':
    init()
