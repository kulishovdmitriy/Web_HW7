from conf.models import Grade
from conf.conect import session

from sqlalchemy import func


def select_4():
    """
    SELECT AVG(grade) AS average_grade
    FROM grades;
    """
    result = session.query(func.avg(Grade.grade).label('average_grade')).scalar()
    return result


if __name__ == '__main__':
    print(select_4())
