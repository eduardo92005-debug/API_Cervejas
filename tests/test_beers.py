import unittest
from unittest.mock import patch, MagicMock
from run_test import app
from run_test import beer_entity
from run_test import beer_factory
import json

class TestBeers(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def create_mock_beers(self):
        be = beer_entity.Beer('Pilsen', 1)
        beers = beer_factory.Factory(be).create_mock(3)
        return beers

    def test_get_beers_should_return_200_when_receive_get(self):
        response = self.app.get('/beers')
        self.assertEqual(response.status_code, 200)

    def test_beers_should_return_valid_json_when_have_at_least_one_beer(self):
        response = self.app.get('/beers')
        self.assertTrue(isinstance(response.json, list))
    
    def test_beers_should_return_correctly_attributes_when_have_at_least_one_beer(self):
        response = self.app.get('/beers')
        beers = response.json
        self.assertIn('style_beer' and 'id_beer' and 'id_best_beer_temperature' and 'created_at' and 'updated_at', beers[0])
    
    def test_beers_when_get_beers_should_return_correctly_numbers_of_beers(self):
        mock_beers = self.create_mock_beers()
        with patch('src.repositories.beer_repository.list_beers') as mock_beer:
            mock_beer.return_value = mock_beers
            response = self.app.get('/beers')
            beers = response.json
            self.assertEqual(len(beers), len(mock_beers))

    def test_beers_when_get_beers_should_return_data(self):
        mock_beers = self.create_mock_beers()
        with patch('src.repositories.beer_repository.list_beers') as mock_beer:
            mock_beer.return_value = mock_beers
            response = self.app.get('/beers')
            beers = response.json
            self.assertTrue(len(beers) > 0 and len(mock_beers) > 0)
            self.assertNotEqual(beers, mock_beers)

