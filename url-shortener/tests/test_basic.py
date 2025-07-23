import pytest
from app.main import app

@pytest.fixture
def client():
    return app.test_client()

def test_shorten_and_redirect(client):
    res = client.post("/api/shorten", json={"url": "https://google.com"})
    assert res.status_code == 201
    data = res.get_json()
    short_code = data["short_code"]

    # Verify redirection
    res2 = client.get(f"/{short_code}")
    assert res2.status_code == 302
    assert res2.location == "https://google.com"

    # Verify stats
    stats = client.get(f"/api/stats/{short_code}")
    assert stats.status_code == 200
    body = stats.get_json()
    assert body["url"] == "https://google.com"
    assert body["clicks"] >= 1
