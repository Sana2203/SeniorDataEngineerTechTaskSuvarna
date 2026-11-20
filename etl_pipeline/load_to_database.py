
import sqlite3


DB_NAME = "senior_data.db"


def load_data(posts, users):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS KS_users (
            id INTEGER PRIMARY KEY,
            name TEXT,
            username TEXT,
            email TEXT,
            city TEXT,
            zipcode TEXT,
            company_name TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS KS_posts (
            id INTEGER PRIMARY KEY,
            userId INTEGER,
            title TEXT,
            body TEXT,
            status TEXT,
            FOREIGN KEY (userId) REFERENCES KS_users(id)
        )
    """)

    user_data = []

    for user in users:
        user_data.append((
            user["id"],
            user["name"],
            user["username"],
            user["email"],
            user["address"]["city"],
            user["address"]["zipcode"],
            user["company"]["name"]
        ))

    cursor.executemany("""
        INSERT OR REPLACE INTO KS_users
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, user_data)

    post_data = []

    for post in posts:
        post_data.append((
            post["id"],
            post["userId"],
            post["title"],
            post["body"],
            post["status"]
        ))

    cursor.executemany("""
        INSERT OR REPLACE INTO KS_posts
        VALUES (?, ?, ?, ?, ?)
    """, post_data)

    conn.commit()

    print("Users loaded:", len(users))
    print("Posts loaded:", len(posts))

    cursor.close()
    conn.close()
