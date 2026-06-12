import sys
from pathlib import Path
import pytest
import requests

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


# =========================
# UI TESTS (keep these)
# =========================

def test_home_page(client):
    response = client.get("/")
    assert response.status_code == 200


def test_page_contains_title(client):
    response = client.get("/")
    assert b"EcoTrack" in response.data


def test_valid_submission(client):
    response = client.post("/", data={
        "travel": "20",
        "electricity": "100",
        "diet": "vegetarian"
    })

    assert response.status_code == 200


def test_zero_values(client):
    response = client.post("/", data={
        "travel": "0",
        "electricity": "0",
        "diet": "vegetarian"
    })

    assert response.status_code == 200


def test_high_impact(client):
    response = client.post("/", data={
        "travel": "1000",
        "electricity": "500",
        "diet": "non-vegetarian"
    })

    assert response.status_code == 200


def test_invalid_input(client):
    response = client.post("/", data={
        "travel": "abc",
        "electricity": "xyz",
        "diet": "vegetarian"
    })

    assert response.status_code == 200


# =========================
# API TESTS (NEW - IMPORTANT)
# =========================

def test_api_response():
    res = requests.post("http://127.0.0.1:5000/api/calculate", json={
        "travel": 50,
        "electricity": 100,
        "diet": "vegetarian"
    })

    data = res.json()

    assert res.status_code == 200
    assert "score" in data
    assert "category" in data
    assert "recommendation" in data
    assert "tips" in data