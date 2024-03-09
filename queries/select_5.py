from conf.models import Student, Teacher, Subject, Grade, Group
from conf.conect import session

from sqlalchemy import func, select, desc, and_


def select_5():
    """
    SELECT s.name AS course_name
    FROM subjects s
    JOIN teachers t ON s.teacher_id = t.id
    WHERE t.fullname ='Цветкова Нинель Артемовна';
    """
    result = session.query(Subject.name) \
        .join(Teacher, Subject.teacher_id == Teacher.id) \
        .filter(Teacher.fullname == 'Цветкова Нинель Артемовна') \
        .all()
    return result


if __name__ == '__main__':
    print(select_5())
