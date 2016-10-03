import datetime

if __name__ == '__main__':

    start = datetime.date(2016, 7, 11)
    today = datetime.date.today()

    print(start)
    print(today)

    diff = today - start

    print(diff.days / 30)