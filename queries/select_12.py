from conf.models import Student, Grade
from conf.conect import session

from sqlalchemy import func


def select_12():
    """
     select max(date)
    from grades g
    join students s on s.id = g.student_id
    where g.subject_id = 2 and s.group_id  =3;

    select s.id, s.fullname, g.grade, g.date
    from grades g
    join students s on g.student_id = s.id
    where g.subject_id = 2 and s.group_id = 3 and g.date = (
        select max(date)
        from grades g2
        join students s2 on s2.id=g2.student_id
        where g2.subject_id = 2 and s2.group_id = 3);
    """

    max_date_query = session.query(func.max(Grade.date)) \
        .join(Student, Student.id == Grade.student_id) \
        .filter(Grade.subject_id == 2) \
        .filter(Student.group_id == 3)

    max_date = max_date_query.scalar()

    if max_date:
        result = session.query(Student.id, Student.fullname, Grade.grade, Grade.date) \
            .join(Grade, Student.id == Grade.student_id) \
            .filter(Grade.subject_id == 2) \
            .filter(Student.group_id == 3) \
            .filter(Grade.date == max_date) \
            .all()

        return result


if __name__ == '__main__':
    print(select_12())
