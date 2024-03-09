from conf.models import Student, Subject, Grade
from conf.conect import session


def select_9():
    """
    SELECT DISTINCT s.name AS subject_name
    FROM students s
    JOIN grades g ON s.id = g.student_id
    JOIN subjects s ON g.subject_id = s.id
    WHERE s.id = 1;
    """

    student_id = 1

    result = session.query(Subject.name) \
        .join(Grade, Grade.subject_id == Subject.id) \
        .join(Student, Student.id == Grade.student_id) \
        .filter(Student.id == student_id) \
        .distinct() \
        .all()
    return result


if __name__ == '__main__':
    print(select_9())
