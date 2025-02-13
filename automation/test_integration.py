import requests
import pytest

RECIPIENTS_URL = "http://localhost:7072"
EMAIL_TEMPLATES_URL = "http://localhost:7071"

def test_fetch_recipients():
    response = requests.get(f"{RECIPIENTS_URL}/recipients")
    assert response.status_code == 200

def test_fetch_email_template():
    response = requests.get(f"{EMAIL_TEMPLATES_URL}/templates/1")
    assert response.status_code == 200
