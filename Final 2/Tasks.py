import datetime
import argparse
from Connect_to_psql import connect_to_database


def task_1(tag, time_1, time_2):
    cur.execute("""
        SELECT Full_name, Name, Tag, Update_time
        FROM Repositories
        WHERE Tag = '{}' AND Update_time 
        BETWEEN '{}' AND '{}'
        """.format(tag, time_1, time_2))
    connect.commit()
    show_task_1()


def task_2(first_date, second_date):
    cur.execute("""
        SELECT Full_name, Star, Update_time 
        FROM Repositories
        WHERE update_time
        BETWEEN '{}' AND '{}'
        ORDER BY Star DESC
        """.format(first_date, second_date))
    connect.commit()
    show_task_2()


def task_3():
    cur.execute("""
        SELECT Tag, count(Full_name) 
        FROM Repositories
        GROUP BY Tag
        ORDER BY count(Full_name) DESC
        LIMIT 10
        """)
    connect.commit()
    show_task_3()


def task_4():
    cur.execute("""
        SELECT Login, Count_of_repositories 
        FROM Users
        ORDER BY Count_of_repositories DESC
    """)
    connect.commit()
    show_task_4()


def show_task_1():
    print("+" + "-"*40 + "+" + "-"*30 + "+" + "-"*15 + "+" + "-"*19 + "+")
    print("|{:>40}|{:>30}|{:>15}|{:>19}|".format("Full_name", "Name", "Tag", "Update_time"))
    print("+" + "-"*40 + "+" + "-"*30 + "+" + "-"*15 + "+" + "-"*19 + "+")

    rows = cur.fetchall()
    for full_name, name, tag, time in rows:
        print("|{:>40}|{:>30}|{:>15}|{}|".format(full_name, name, tag, time))

    print("+" + "-" * 40 + "+" + "-" * 30 + "+" + "-" * 15 + "+" + "-" * 19 + "+")


def show_task_2():
    print("+" + "-"*35 + "+" + "-"*15 + "+" + "-"*19 + "+")
    print("|{:>35}|{:>15}|{:>19}|".format("Full_name", "Star", "Update_time"))
    print("+" + "-"*35 + "+" + "-"*15 + "+" + "-"*19 + "+")

    rows = cur.fetchall()
    for name, star, time in rows:
        print("|{:>35}|{:>15}|{}|".format(name, star, time))

    print("+" + "-"*35 + "+" + "-"*15 + "+" + "-"*19 + "+")


def show_task_3():
    print("+" + "-"*15 + "+" + "-"*15 + "+")
    print("|{:>15}|{:>15}|".format("Tag", "Count"))
    print("+" + "-" * 15 + "+" + "-" * 15 + "+")

    rows = cur.fetchall()
    for tag, count in rows:
        print("|{:>15}|{:>15}|".format(tag, count))

    print("+" + "-"*15 + "+" + "-"*15 + "+")


def show_task_4():
    print("+" + "-"*35 + "+" + "-"*25 + "+")
    print("|{:>35}|{:>25}|".format("Login", "Count_of_repositories"))
    print("+" + "-"*35 + "+" + "-"*25 + "+")

    rows = cur.fetchall()
    for login, count in rows:
        print("|{:>35}|{:>25}|".format(login, count))

    print("+" + "-" * 35 + "+" + "-" * 25 + "+")


def create_argparse():
    parser = argparse.ArgumentParser()
    parser.add_argument("--task")
    parser.add_argument("--tag")
    parser.add_argument("--time1")
    parser.add_argument("--time2")

    return parser


def main():
    global connect
    global cur

    connect, cur = connect_to_database()
    parser = create_argparse()
    namespace = parser.parse_args()

    if namespace.task == "1":
        task_1(namespace.tag, namespace.time1, namespace.time2)
    elif namespace.task == "2":
        current_date = datetime.datetime.today()
        week_ago = current_date.replace(day=current_date.day - 7)
        task_2(week_ago, current_date)
    elif namespace.task == "3":
        task_3()
    elif namespace.task == "4":
        task_4()


if __name__ == "__main__":
    main()