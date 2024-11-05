import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

# Создайте таблицу Users, если она ещё не создана.
cursor.execute("""
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
""")

# Заполните её 10 записями:
# for i in range(1, 11):
#     cursor.execute('INSERT INTO USERS (username, email, age, balance) VALUES (?, ?, ?, ?)', (f'User{i}', f'example{i}@gmail.com', f'{i*10}', '1000'))
# connection.commit()

# Обновите balance у каждой 2ой записи начиная с 1ой на 500:
cursor.execute('UPDATE Users set balance = ? WHERE id % 2 != ?', ('500', 0))
connection.commit()

# Удалите каждую 3ую запись в таблице начиная с 1ой:
cursor.execute('DELETE FROM USERS WHERE id % 3 = ?', (1,))
connection.commit()

# Сделайте выборку всех записей при помощи fetchall(), где возраст не равен 60 и выведите их в консоль в
# следующем формате (без id):
# Имя: <username> | Почта: <email> | Возраст: <age> | Баланс: <balance>
cursor.execute('SELECT username, email, age, balance FROM Users WHERE age != ?', (60,))
users = cursor.fetchall()
for user in users:
    print(f"Имя: {user[0]} | Почта: {user[1]} | Возраст: {user[2]} | Баланс: {user[3]}")

# Удалите из базы данных not_telegram.db запись с id = 6.
cursor.execute('DELETE FROM USERS WHERE id = ?', ('6',))
connection.commit()

# Подсчитать общее количество записей.
cursor.execute('SELECT COUNT(*) FROM Users')
total_users = cursor.fetchone()[0]

# Посчитать сумму всех балансов.
cursor.execute('SELECT SUM(balance) FROM USERS')
all_balances = cursor.fetchone()[0]

# Подсчёт суммы всех балансов
print(all_balances / total_users)
connection.close()