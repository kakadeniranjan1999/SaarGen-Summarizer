from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)


def test_query():
    response = client.get("/query")
    assert response.status_code == 200
    assert response.json() == {
        "description": "Hello! I am SaarGen! Your AI summary generator. My name is a combination of Sanskrit word "
                       "Saaransh (meaning Summary in English) and Generator!",
    }

def test_summarize():
    req = {
        "text": "The Inflation Reduction Act lowers prescription drug costs, health care costs, and energy costs. "
                "It's the most aggressive action on tackling the climate crisis in American history which will lift up "
                "American workers and create good-paying, union jobs across the country. It'll lower the deficit and "
                "ask the ultra-wealthy and corporations to pay their fair share. And no one making under $400,000 per "
                "year will pay a penny more in taxes."
    }
    response = client.post("/summarize", json=req)
    assert response.status_code == 200
