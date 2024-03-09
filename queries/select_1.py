from conf.models import Student, Grade
from conf.conect import session

from sqlalchemy import func, desc


def select_1():
    """
        SELECT
        s.id,
        s.name,
        ROUND(AVG(g.grade)) AS average_grade
    FROM students s
    JOIN grades g ON s.id = g.student_id
    GROUP BY s.id
    ORDER BY average_grade DESC
    LIMIT 5;
    """

    result = session.query(Student.id, Student.fullname, func.round(func.avg(Grade.grade)).label('average_grade')) \
        .select_from(Student).join(Grade).group_by(Student.id).order_by(desc('average_grade')).limit(5).all()
    return result


if __name__ == '__main__':
    print(select_1())
