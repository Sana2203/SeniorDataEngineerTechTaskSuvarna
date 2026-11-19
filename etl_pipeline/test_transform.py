
from transform_data import add_post_status


def test_add_post_status():
    posts = [
        {
            "id": 1,
            "title": "Short post",
            "body": "A" * 100
        },
        {
            "id": 2,
            "title": "Long post",
            "body": "B" * 160
        }
    ]

    result = add_post_status(posts)

    assert len(result) == 2
    assert result[0]["status"] == "concise"
    assert result[1]["status"] == "lengthy"


def test_original_posts_are_not_modified():
    posts = [
        {
            "id": 1,
            "title": "Short post",
            "body": "Hello"
        }
    ]

    add_post_status(posts)

    assert "status" not in posts[0]

