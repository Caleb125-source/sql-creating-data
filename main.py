import sqlite3
# import pandas as pd

conn = sqlite3.connect('my_db.sqlite')
cur = conn.cursor()

# cur.execute("""
#     CREATE TABLE users (
#         id INTEGER PRIMARY KEY,
#         name TEXT NOT NULL,
#         email TEXT UNIQUE NOT NULL,
#         signup_date DATE DEFAULT CURRENT_DATE
#     );  
# """)

cur.execute("""
    INSERT INTO users (name, email)
    VALUES 
        ('Caleb Munyoki', 'caleb.munyoki@gmail.com');
""")

# conn.commit()

# cur.execute("""
#     INSERT INTO users (name, email, phone_number)
#     VALUES 
#         ('John White', 'john.white@example.com', '123-456-7890');
# """)


# cur.execute("""
#     UPDATE users
#     SET email = 'sofia.ramirez@domain.com'
#     WHERE email = 'sofia.ramirez@example.com';
# """)

# cur.execute("""
#     INSERT INTO users (name, email)
#     VALUES 
#         ('Test User', 'test@test.com');
# """)

# conn.commit()

cur.execute("""
    DELETE FROM users
    WHERE name = 'Test User';
""")
conn.rollback()

cur.execute("""SELECT * FROM users;""")
print(cur.fetchall())

# cur.execute("""
#     ALTER TABLE users ADD COLUMN phone_number TEXT;
# """)

# print(cur.execute("""PRAGMA table_info(users);""").fetchall())