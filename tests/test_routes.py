from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_create_user_story():
    response = client.post(
        "/stories/",
        json={
            "title": "Test Story",
            "description": "This is a test user story.",
        },
    )
    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    assert data["title"] == "Test Story"
    assert data["description"] == "This is a test user story."


def test_get_all_stories():
    response = client.get("/stories/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
