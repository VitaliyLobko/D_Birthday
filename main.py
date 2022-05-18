from datetime import datetime
from collections import defaultdict

users = [
    {"name": "Alex", "birthday": '2005-05-15T00:00:00'},
    {"name": "Dave", "birthday": '2005-05-15T00:00:00'},
    {"name": "Bill", "birthday": '1978-05-17T00:00:00'},
    {"name": "Mark", "birthday": '2021-05-14T00:00:00'},
    {"name": "Ilon", "birthday": '2001-05-22T00:00:00'}]


def get_birthdays_per_week(_users):
    week = ['Monday',
            'Tuesday',
            'Wednesday',
            'Thursday',
            'Friday',
            'Saturday',
            'Sunday']

    d_now = datetime.now()
    year_start = datetime(year=d_now.year, month=1, day=1)
    days_now = (d_now - year_start).days
    days_plus_week = days_now + 7

    db_list = defaultdict(list)

    for user in _users:
        db = datetime.fromisoformat(user['birthday'])
        days_db = (datetime(year=d_now.year, month=db.month, day=db.day) - year_start).days

        if (days_db >= days_now) and (days_db <= days_plus_week):
            if (db.weekday() == 5) or (db.weekday() == 6):
                weekday = week[0]
            else:
                weekday = week[db.weekday()]
            db_list[weekday].append(user['name'])

    return db_list


lst = get_birthdays_per_week(users)

for i in lst:
    print(i+":", *lst[i])

