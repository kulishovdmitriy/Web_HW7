from conf.models import Student, Teacher, Subject, Grade, Group
from conf.conect import session

from sqlalchemy import func, select, desc, and_


def select_8():
    """
    SELECT ROUND(AVG(g.grade)) AS average_grade
    FROM grades g
    JOIN subjects s ON g.subject_id = s.id
    WHERE s.teacher_id = 5;
    """

    result = session.query(func.round(func.avg(Grade.grade)).label('average_grade')) \
        .join(Subject, Grade.subject_id == Subject.id) \
        .filter(Subject.teacher_id == 5) \
        .scalar()
    return result


if __name__ == '__main__':
    print(select_8())