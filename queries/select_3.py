from conf.models import Student, Grade
from conf.conect import session

from sqlalchemy import func


def select_3():
    """
    SELECT s.group_id, ROUND(AVG(g.grade)) AS average_grade
    FROM grades g
    JOIN students s ON g.student_id = s.id
    WHERE g.subject_id = 1
    GROUP BY s.group_id;
    """
    result = session.query(Student.group_id, func.round(func.avg(Grade.grade))).select_from(Grade).join(Student) \
        .filter(Grade.subject_id == 1).group_by(Student.group_id)
    return result


if __name__ == '__main__':
    print(select_3())
