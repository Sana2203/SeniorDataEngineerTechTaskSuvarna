
import sqlite3
from load_to_database import load_data


def test_load_data(tmp_path, monkeypatch):
    # Use a temporary database for testing
    test_db = tmp_path / "test_database.db"

    monkeypatch.setattr(
        "load_to_database.DB_NAME",
        str(test_db)
    )

    users = [
        {
            "id": 1,
            "name": "Test User",
            "username": "testuser",
            "email": "test@example.com",
            "address": {
                "city": "Hyderabad",
                "zipcode": "500001"
            },
            "company": {
                "name": "Test Company"
            }
        }
    ]

    posts = [
        {
            "id": 1,
            "userId": 1,
            "title": "Test Post",
            "body": "Test body",
            "status": "concise"
        }
    ]

    # Load data
    load_data(posts, users)

    # Validate database records
    conn = sqlite3.connect(test_db)
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM KS_users")
    assert cursor.fetchone()[0] == 1

    cursor.execute("SELECT COUNT(*) FROM KS_posts")
    assert cursor.fetchone()[0] == 1

    cursor.execute("SELECT city FROM KS_users WHERE id = 1")
    assert cursor.fetchone()[0] == "Hyderabad"

    cursor.close()
    conn.close()

