from conf.models import Student, Grade
from conf.conect import session

from sqlalchemy import func, desc


def select_2():
    """
    SELECT
        s.id,
        s.fullname,
        ROUND(AVG(g.grade)) AS average_grade
    FROM grades g
    JOIN students s ON s.id = g.student_id
    where g.subject_id = 1
    GROUP BY s.id
    ORDER BY average_grade DESC
    LIMIT 1;
    """
    result = session.query(Student.id, Student.fullname, func.round(func.avg(Grade.grade)).label('average_grade')) \
        .select_from(Grade).join(Student).filter(Grade.subject_id == 1).group_by(Student.id).order_by(
        desc('average_grade')).limit(1).all()
    return result


if __name__ == '__main__':
    print(select_2())
