from fastapi.testclient import TestClient
from main import app


client = TestClient(app)


def test_sample():
    assert 1 ==1

def test_say_hello():
    response = client.get("/say_hello")
    assert response.status_code == 200
    message = response.json()["message"]
    assert message == 'Hello World'


def test_fetch_url():
    response = client.post(
        url = "/fetch_url",
        json = {
            'year': 2022,
            'month': 2,
            'date': 6,
            'station': 'Pytest2'
            }
        )
    assert response.status_code == 200
    message = response.json()["url"]
    assert message == 'https://noaa-nexrad-level2.s3.amazonaws.com/index.html#2022/02/06/Pytest2'