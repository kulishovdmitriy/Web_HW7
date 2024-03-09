from faker import Faker
from conf.models import Teacher, Subject, Student, Grade, Group
from conf.conect import session

import random

fake = Faker('ru-Ru')


def init():
    # for _ in range(3):
    #     group_name = fake.word()
    #     group = Group(name=group_name)
    #     session.add(group)
    #     session.commit()
    #
    #     for _ in range(30):
    #         student_name = fake.name()
    #         student = Student(fullname=student_name, group_id=group.id)
    #         session.add(student)
    #         session.commit()
    #     print('Студенты и группы созданы')
    #
    # for _ in range(5):
    #     teacher_name = fake.name()
    #     teacher = Teacher(fullname=teacher_name)
    #     session.add(teacher)
    #     session.commit()
    #
    #     for _ in range(8):
    #         subject_name = fake.word()
    #         subject = Subject(name=subject_name, teacher_id=teacher.id)
    #         session.add(subject)
    #         session.commit()
    #     print('Предметы и учителя созданы')

    students_ids = [student.id for student in session.query(Student.id).all()]
    subjects_ids = [subject.id for subject in session.query(Subject.id).all()]

    # Создание оценок для студентов по всем предметам
    for student_id in students_ids:
        for subject_id in subjects_ids:
            grade = random.randint(50, 100)
            date = fake.date_between(start_date='-2y', end_date='today')
            grade = Grade(student_id=student_id, subject_id=subject_id, grade=grade, date=date)
            session.add(grade)
            session.commit()


if __name__ == '__main__':
    init()
    print('Данные внесены и сохранены в базу данных')