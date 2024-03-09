from conf.models import Student, Teacher, Subject, Grade
from conf.conect import session


def select_10():
    """
    SELECT DISTINCT s.name AS subject_name
    FROM students s
    JOIN grades g ON s.id = g.student_id
    JOIN subjects s ON g.subject_id = s.id
    JOIN teachers t ON s.teacher_id = t.id
    WHERE s.id = 23 AND t.id = 2;
    """

    student_id = 23
    teacher_id = 2

    result = session.query(Subject.name) \
        .join(Grade, Grade.subject_id == Subject.id) \
        .join(Student, Student.id == Grade.student_id) \
        .join(Teacher, Teacher.id == Subject.teacher_id) \
        .filter(Student.id == student_id) \
        .filter(Teacher.id == teacher_id) \
        .distinct() \
        .all()
    return result


if __name__ == '__main__':
    print(select_10())
