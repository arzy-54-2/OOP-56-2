from sqlite3 import connect
from string import digits
from decimal import __libmpdec_version__

import random
import importlib



connect=connect("users.db")

# Рука с ручкой
cursor=connect.cursor()

cursor.execute('''
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fio VARCAHR (100) NOT NULL,
            age INTEGER NOT NULL,
            hobby TEXT
        )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS grades(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        subject VARCAHR (100) NOT NULL,
        grade INTEGER NOT NULL,
        description TEXT,
        FOREIGN KEY (user_id) REFERENCES users(id)
    )
''')

connect.commit()


#  CRUD
# Create - Read - Update - Delete

def add_user(fio_par,age_par,hobby_par):
    cursor.execute(
        'INSERT INTO users(fio, age, hobby) VALUES(?,?,?)',
        (fio_par, age_par, hobby_par)
    )
    connect.commit()
    print(f"{fio_par} добавлен")

def add_grade(user_id, subject, grade):
    cursor.execute(
        'INSERT INTO grades(user_id, subject, grade) VALUES (?,?,?)',
        (user_id, subject, grade)
    )
    connect.commit()
    print('grade added!!')

add_grade(1, "Химия", 5)
# add_grade(2, "Алгебра", 5)
# add_grade(3, "Алгебра", 5)
# add_grade(4, "Алгебра", 5)

# add_user("Iskhak Razakov", 10, "Спать!!")
# add_user("Do ro ro", 33, "отдых")
# add_user("Kirito", 15, "Спать!!")

def get_users_with_grade():
    cursor.execute(
        '''
        SELECT users.fio, grades.subject, grades.grade
        FROM users LEFT JOIN grades ON users.id = grades.user_id
        '''
    )

    users = cursor.fetchall()
    for i in users:
        print(f"FIO: {i[0]}, SUBJECT: {i[1]}, GRADE: {i[2]}")

get_users_with_grade()

def get_users():
    cursor.execute("SELECT fio, age FROM users")

    users = cursor.fetchall()

    for i in users:
        print(f"FIO: {i[0]}, AGE: {i[1]}")


# get_users()

def get_user_detail(user_id):
    cursor.execute(
        'SELECT * FROM users WHERE id = ?',
        (user_id,)
    )

    user = cursor.fetchone()
    print(user)


# get_user_detail(3)

def update_user(name:str="John Doe",id_obj:int=1):
    cursor.execute(
        "UPDATE users SET fio = ? WHERE rowid = ?",
        (name, id_obj)
    )
    connect.commit()
    print('Пользователь обнавлен!!')

# update_user("Oleg Smirnov", 4)


def delete_user(row_id):
    cursor.execute(
        'DELETE FROM users WHERE rowid = ?',
        (row_id,)
    )
    connect.commit()
    print('user deleted!!')


# delete_user(2)
