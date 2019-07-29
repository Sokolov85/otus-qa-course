"""Module for unittest Openbrewerydb JSON API class"""
from unittest import TestCase
from unittest.mock import patch


class TestOpenbrewerydb(TestCase):
    def setUp(self):
        """Fixrure"""
        self.return_value = [
            {
                'name': 'Alosta Brewing Co',
                'city': 'Covina',
                'longitude': '-117.878146550423',
                'tag_list': ['patio'],
                'state': 'California',
                'street': '692 Arrow Grand Cir',
                'latitude': '34.1036502643654',
                'id': 300,
                'postal_code': '91722-2122',
                'updated_at': '2018-08-23T23:24:12.610Z',
                'country': 'United States',
                'website_url': 'http://www.alostabrewing.com',
                'brewery_type': 'micro',
                'phone': '9094558707'
            }
        ]

    @patch('openbrewerydb.Openbrewerydb')
    def test_get_brewery(self, MockGetBrewery):
        """get_brewery test"""
        brewery = MockGetBrewery()
        brewery.posts.return_value = self.return_value
        response = brewery.posts()
        self.assertIsNotNone(response)
        self.assertIsInstance(response[0], dict)
        self.assertEqual(response[0]['id'], 300)

    @patch('openbrewerydb.Openbrewerydb')
    def test_filter_by_state(self, MockFilterByState):
        """filter_by_state test"""
        brewery = MockFilterByState()
        brewery.posts.return_value = self.return_value
        response = brewery.posts()
        self.assertIsNotNone(response)
        self.assertIsInstance(response[0], dict)
        self.assertEqual(response[0]['state'], 'California')

    @patch('openbrewerydb.Openbrewerydb')
    def test_filter_by_name(self, MockFilterByName):
        """filter_by_name test"""
        brewery = MockFilterByName()
        brewery.posts.return_value = self.return_value
        response = brewery.posts()
        self.assertIsNotNone(response)
        self.assertIsInstance(response[0], dict)
        self.assertEqual(response[0]['name'], 'Alosta Brewing Co')

    @patch('openbrewerydb.Openbrewerydb')
    def test_autocomplete_name(self, MockAutocompleteName):
        """autocomplete_name test"""
        brewery = MockAutocompleteName()
        brewery.posts.return_value = self.return_value
        response = brewery.posts()
        self.assertIsNotNone(response)
        self.assertIsInstance(response[0], dict)
        self.assertIn('Alosta', response[0]['name'])

    @patch('openbrewerydb.Openbrewerydb')
    def test_search_name(self, MockSearchName):
        """search_name test"""
        brewery = MockSearchName()
        brewery.posts.return_value = self.return_value
        response = brewery.posts()
        self.assertIsNotNone(response)
        self.assertIsInstance(response[0], dict)
        self.assertIn('patio', response[0]['tag_list'])

    @patch('openbrewerydb.Openbrewerydb')
    def test_filter_by_type(self, MockFilterByType):
        """filter_by_type test"""
        brewery = MockFilterByType()
        brewery.posts.return_value = self.return_value
        response = brewery.posts()
        self.assertIsNotNone(response)
        self.assertIsInstance(response[0], dict)
        self.assertIn('micro', response[0]['brewery_type'])
