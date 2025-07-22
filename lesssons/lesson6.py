import sqlite3

#  A4
connect = sqlite3.connect("users.db")

# Рука с ручкой
cursor = connect.cursor()

cursor.execute('''
        CREATE TABLE IF NOT EXISTS users(
            fio VARCAHR (100) NOT NULL,
            age INTEGER NOT NULL,
            hobby TEXT
        )
''')

connect.commit()


#  CRUD
# Create - Read - Update - Delete

def add_user(fio_par, age_par, hobby_par):
    cursor.execute(
        'INSERT INTO users(fio, age, hobby) VALUES(?,?,?)',
        (fio_par, age_par, hobby_par)
    )
    connect.commit()
    print(f"{fio_par} добавлен")

add_user("Ardager Kartanbekov", 26, "Спать!!")



