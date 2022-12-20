import unittest
from run_test import app
import json

class TestIndex(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_index_should_return_200_when_receive_get(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_index_should_return_welcome_content_when_receive_get(self):
        response = self.app.get('/')
        escape_response = json.loads(response.data)
        self.assertEqual(escape_response, 'Welcome to Cervejas API')