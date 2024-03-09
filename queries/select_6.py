from conf.models import Student
from conf.conect import session


def select_6():
    """
    SELECT fullname
    FROM students
    WHERE group_id = 3;
    """
    result = session.query(Student.fullname).filter(Student.group_id == 3).all()
    return result


if __name__ == '__main__':
    print(select_6())
