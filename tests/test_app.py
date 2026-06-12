import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from app import app


def test_home_page():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200


def test_valid_submission():
    client = app.test_client()

    response = client.post(
        "/",
        data={
            "travel": "20",
            "electricity": "100",
            "diet": "vegetarian"
        }
    )

    assert response.status_code == 200


def test_zero_values():
    client = app.test_client()

    response = client.post(
        "/",
        data={
            "travel": "0",
            "electricity": "0",
            "diet": "vegetarian"
        }
    )

    assert response.status_code == 200


def test_non_vegetarian():
    client = app.test_client()

    response = client.post(
        "/",
        data={
            "travel": "50",
            "electricity": "200",
            "diet": "non-vegetarian"
        }
    )

    assert response.status_code == 200


def test_page_contains_title():
    client = app.test_client()

    response = client.get("/")

    assert b"EcoTrack AI" in response.data