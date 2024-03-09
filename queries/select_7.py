from conf.models import Student, Grade
from conf.conect import session


def select_7():
    """
    SELECT s.fullname AS student_name, g.grade
    FROM grades g
    JOIN students s ON g.student_id = s.id
    WHERE s.group_id = 3
        AND g.subject_id = 6;
    """
    result = session.query(Student.fullname, Grade.grade) \
        .join(Grade, Student.id == Grade.student_id) \
        .filter(Student.group_id == 3) \
        .filter(Grade.subject_id == 6) \
        .all()
    return result


if __name__ == '__main__':
    print(select_7())
