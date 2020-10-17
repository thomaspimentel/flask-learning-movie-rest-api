import json
from app import app
from tests.BaseCase import BaseCase


class SignupTest(BaseCase):
    def test_successful_signup(self):
        payload = json.dumps({
            "email": "thomas@webscaping.ca",
            "password": "mycoolpassword"
        })

        response = self.app.post(
            "/api/auth/signup", headers={"Content-Type": "application/json"}, data=payload)

        self.assertEqual(str, type(response.json['id']))
        self.assertEqual(200, response.status_code)
