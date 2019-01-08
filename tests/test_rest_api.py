from wt.pygardena.rest_api import *

import unittest
import requests
import requests_mock
    
class MockLocation:
    id = 'washington'

class MockDevice:
    location = MockLocation()
    id = 'black-box'
    category = 'code-breaker'

@requests_mock.mock()
class TestRestAPI(unittest.TestCase):

    verified = {'result': 'verified'}
    
    def setUp(self):
        self.under_test = RestAPI()

    def test_relative_url(self, mock):
        mock.get('https://smart.gardena.com/sg-1/test', json=self.verified)
        self.assertEqual(self.under_test.get('test').json(), self.verified)
    
    def test_accepts_json(self, mock):
        mock.get('https://smart.gardena.com/sg-1/test', request_headers={'Accept': 'application/json'}, json=self.verified)
        self.assertEqual(self.under_test.get('test').json(), self.verified)
    
    def test_post_sessions(self, mock):
        def match_sessions(request):
            return request.json() == { 'sessions': {
                'email': 'werner.brandes@playtronics.example',
                'password': 'MyVoiceIsMyPassport',
            }}
        mock.post('https://smart.gardena.com/sg-1/sessions', additional_matcher=match_sessions, json=self.verified)
        self.assertEqual(self.under_test.post_sessions('werner.brandes@playtronics.example', 'MyVoiceIsMyPassport'), self.verified)
    
    def test_get_locations(self, mock):
        mock.get('https://smart.gardena.com/sg-1/locations?user_id=martin-bishop', json=self.verified)
        self.assertEqual(self.under_test.get_locations('martin-bishop'), self.verified)
    
    def test_get_devices(self, mock):
        mock.get('https://smart.gardena.com/sg-1/devices?locationId=washington', json=self.verified)
        self.assertEqual(self.under_test.get_devices('washington'), self.verified)
    
    def test_post_command_without_parameters(self, mock):
        def match_body(request):
            return request.json() == {
                'name': 'open'
            }
        mock.post('https://smart.gardena.com/sg-1/devices/black-box/abilities/code-breaker/command?locationId=washington', additional_matcher=match_body, json=self.verified)
        self.assertEqual(self.under_test.post_command(MockDevice(), 'open').json(), self.verified)
    
    def test_post_command_with_parameters(self, mock):
        def match_body(request):
            return request.json() == {
                'name': 'open',
                'parameters': {'force': True}
            }
        mock.post('https://smart.gardena.com/sg-1/devices/black-box/abilities/code-breaker/command?locationId=washington', additional_matcher=match_body, json=self.verified)
        self.assertEqual(self.under_test.post_command(MockDevice(), 'open', {'force': True}).json(), self.verified)
    