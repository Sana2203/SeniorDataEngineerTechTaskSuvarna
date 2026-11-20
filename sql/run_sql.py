
import sqlite3

# Connect to SQLite database
conn = sqlite3.connect("senior_data.db")
cursor = conn.cursor()

# Execute database schema
with open("sql/schema.sql", "r") as file:
    schema = file.read()

cursor.executescript(schema)
conn.commit()

print("Database schema verified successfully!")

# SQL analysis queries
queries = {

    "Q1 - Top 5 users by average post body length": """
        SELECT
            u.id,
            u.name,
            AVG(LENGTH(p.body)) AS avg_body_length
        FROM KS_users u
        JOIN KS_posts p
            ON u.id = p.userId
        GROUP BY u.id, u.name
        ORDER BY avg_body_length DESC
        LIMIT 5;
    """,

    "Q2 - Average total post length for top 5 users": """
        WITH top_users AS (
            SELECT
                u.id,
                u.name
            FROM KS_users u
            JOIN KS_posts p
                ON u.id = p.userId
            GROUP BY u.id, u.name
            ORDER BY AVG(LENGTH(p.body)) DESC
            LIMIT 5
        )

        SELECT
            u.id,
            u.name,
            AVG(LENGTH(p.title) + LENGTH(p.body))
                AS avg_total_post_length
        FROM top_users u
        JOIN KS_posts p
            ON u.id = p.userId
        GROUP BY u.id, u.name
        ORDER BY avg_total_post_length DESC;
    """,

    "Q3 - Weekday with most lengthy posts": """
        SELECT
            CASE strftime(
                '%w',
                date('1970-01-01', '+' || id || ' days')
            )
                WHEN '0' THEN 'Sunday'
                WHEN '1' THEN 'Monday'
                WHEN '2' THEN 'Tuesday'
                WHEN '3' THEN 'Wednesday'
                WHEN '4' THEN 'Thursday'
                WHEN '5' THEN 'Friday'
                WHEN '6' THEN 'Saturday'
            END AS weekday,
            COUNT(*) AS lengthy_post_count
        FROM KS_posts
        WHERE status = 'lengthy'
        GROUP BY weekday
        ORDER BY lengthy_post_count DESC
        LIMIT 1;
    """
}

# Execute and display results
for title, query in queries.items():

    print("\n" + title)
    print("-" * 50)

    cursor.execute(query)

    for row in cursor.fetchall():
        print(row)

# Close database connection
conn.close()

print("\nSQL analysis completed successfully!")
