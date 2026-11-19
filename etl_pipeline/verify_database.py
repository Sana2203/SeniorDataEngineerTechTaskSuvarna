
from pathlib import Path
import sqlite3

base_path = Path(__file__).resolve().parent

db_path = base_path / "senior_data.db"
sql_path = base_path.parent / "sql" / "analysis_queries.sql"

conn = sqlite3.connect(db_path)

with open(sql_path, "r", encoding="utf-8") as file:
    query = file.read()

cursor = conn.execute(query)

print("\nSQL Analysis Results:")

for row in cursor.fetchall():
    print(row)

cursor.execute("""
    SELECT status, COUNT(*)
    FROM KS_posts
    GROUP BY status
""")

print("\nPost status summary:")

for row in cursor.fetchall():
    print(row)


# Verify duplicate users

cursor.execute("""
    SELECT id, COUNT(*)
    FROM KS_users
    GROUP BY id
    HAVING COUNT(*) > 1
""")

duplicates = cursor.fetchall()

print("\nDuplicate users:")

if duplicates:
    for row in duplicates:
        print(row)
else:
    print("No duplicate users found")


# Verify duplicate posts

cursor.execute("""
    SELECT id, COUNT(*)
    FROM KS_posts
    GROUP BY id
    HAVING COUNT(*) > 1
""")

duplicates = cursor.fetchall()

print("\nDuplicate posts:")

if duplicates:
    for row in duplicates:
        print(row)
else:
    print("No duplicate posts found")

# Verify total record counts

cursor.execute("SELECT COUNT(*) FROM KS_users")
user_count = cursor.fetchone()[0]

cursor.execute("SELECT COUNT(*) FROM KS_posts")
post_count = cursor.fetchone()[0]

print("\nRecord Count Validation:")
print("Total users:", user_count)
print("Total posts:", post_count)

# Validate NULL values in users

cursor.execute("""
    SELECT COUNT(*)
    FROM KS_users
    WHERE name IS NULL
       OR email IS NULL
""")

null_users = cursor.fetchone()[0]

print("\nNULL Value Validation:")
print("Users with missing name or email:", null_users)

# Validate orphan posts

cursor.execute("""
    SELECT COUNT(*)
    FROM KS_posts p
    LEFT JOIN KS_users u
        ON p.userId = u.id
    WHERE u.id IS NULL
""")

orphan_posts = cursor.fetchone()[0]

print("\nForeign Key Validation:")
print("Posts without valid users:", orphan_posts)
cursor.close()
conn.close()

print("\nDatabase verification completed!")


