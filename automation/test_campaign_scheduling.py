import requests
import pytest

BASE_URL = "http://localhost:7070"

def test_create_campaign():
    payload = {"name": "Test Campaign", "schedule": "2025-01-01T12:00:00Z"}
    response = requests.post(f"{BASE_URL}/campaigns", json=payload)
    assert response.status_code == 201
    assert response.json()["name"] == "Test Campaign"

def test_cancel_campaign():
    campaign_id = 1  # Replace with a valid campaign ID
    response = requests.delete(f"{BASE_URL}/campaigns/{campaign_id}")
    assert response.status_code == 200
