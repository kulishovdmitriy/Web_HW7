from conf.models import Student, Teacher, Subject, Grade
from conf.conect import session

from sqlalchemy import func


def select_11():
    """
    SELECT ROUND(AVG(g.grade)) AS average_grade
    FROM grades g
    JOIN subjects s ON g.subject_id = s.id
    JOIN students st ON g.student_id = st.id
    JOIN teachers t ON s.teacher_id = t.id
    WHERE st.id = 1 AND t.id = 3;
    """

    student_id = 1
    teacher_id = 3

    result = session.query(func.round(func.avg(Grade.grade)).label('average_grade')) \
        .join(Subject, Grade.subject_id == Subject.id) \
        .join(Student, Grade.student_id == Student.id) \
        .join(Teacher, Subject.teacher_id == Teacher.id) \
        .filter(Student.id == student_id) \
        .filter(Teacher.id == teacher_id) \
        .scalar()
    return result


if __name__ == '__main__':
    print(select_11())
