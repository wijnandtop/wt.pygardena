import requests
from urllib.parse import urljoin

class RestAPI(requests.Session):
    """
    Encapsulates all REST calls to the Gardena API.
    """
    
    # The base URL for all Gardena requests. Change this if you want to fire the requests against other services
    base_url = "https://smart.gardena.com/sg-1/"
    
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        self.headers["Accept"] = "application/json"
    
    def request(self, method, url, *args, **kw):
        return super().request(method, urljoin(self.base_url, url), *args, **kw)
    
    def post_sessions(self, email_address, password):
        """
        Posts session data to the server.
        """
        response = self.post('sessions', json={
            'sessions': {
                'email': email_address,
                'password': password,
            }
        })
        return response.json()
    
    def get_locations(self, user_id):
        """
        Gets all the locations that are associated with a given user ID.
        """
        response = self.get("locations", params={
            'user_id': user_id,
        })
        return response.json()
    
    def get_devices(self, location_id):
        """
        Loads the devices from a given location ID.
        """
        response = self.get('devices', params={
            'locationId': location_id
        })
        return response.json()
    
    def post_command(self, device, command_name, parameters=None):
        data = {'name': command_name}
        if parameters is not None:
            data['parameters'] = parameters

        url = 'devices/{device.id}/abilities/{device.category}/command'.format(device=device)
        return self.post(url, params={
            'locationId': device.location.id
        }, json=data)