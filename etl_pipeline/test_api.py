
from unittest.mock import patch, Mock
import pytest
import requests

from api_client import fetch_posts, fetch_users


@patch("api_client.requests.get")
def test_fetch_posts(mock_get):
    mock_response = Mock()
    mock_response.json.return_value = [
        {"id": 1, "title": "Test post", "body": "Hello"}
    ]
    mock_get.return_value = mock_response

    posts = fetch_posts()

    assert len(posts) == 1
    assert posts[0]["id"] == 1


@patch("api_client.requests.get")
def test_fetch_users(mock_get):
    mock_response = Mock()
    mock_response.json.return_value = [
        {"id": 1, "name": "Test User"}
    ]
    mock_get.return_value = mock_response

    users = fetch_users()

    assert len(users) == 1
    assert users[0]["name"] == "Test User"


@patch("api_client.requests.get")
def test_api_error_handling(mock_get):
    mock_response = Mock()
    mock_response.raise_for_status.side_effect = requests.HTTPError(
        "API request failed"
    )
    mock_get.return_value = mock_response

    with pytest.raises(requests.HTTPError):
        fetch_posts()
