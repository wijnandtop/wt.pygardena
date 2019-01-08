from .location import *
from .rest_api import RestAPI

class GardenaSmartAccount:
    
    def __init__(self, email_address, password):
        self.email_address = email_address
        self.password = password
        
        self.rest_api = RestAPI()
        
        self.locations = set()
        self.raw_locations = None
        self.update_authtokens()


    def load_locations(self):
        self.raw_locations = response_data = self.rest_api.get_locations(self.userID)
        for location in response_data['locations']:
            self.locations.add(GardenaSmartLocation(self.rest_api, location))

    def get_locations(self):
        if len(self.locations) == 0:
            self.load_locations()
        return self.locations

    def get_raw_location_data(self, location_id):
        for location in self.raw_locations:
            if location.id == location_id:
                return location
        raise KeyError(location_id)

    def update_devices(self):
        for location in self.locations:
            location.update_devices()
    
    def update_authtokens(self):
        """
        Get authentication token from servers and store it as the session in the Rest API.
        """
        response_data = self.rest_api.post_sessions(self.email_address, self.password)
        self.AuthToken = response_data['sessions']['token']
        self.refreshToken = response_data['sessions']['refresh_token']
        self.userID = response_data['sessions']['user_id']
        self.rest_api.headers['X-Session'] = self.AuthToken

    def get_all_mowers(self):
        all_mowers = set()
        for location in self.get_locations():
            for mower in location.get_mowers():
                all_mowers.add(mower)
        return all_mowers

    def get_all_sensors(self):
        all_sensors = set()
        for location in self.get_locations():
            for sensor in location.get_sensors():
                all_sensors.add(sensor)
        return all_sensors

    def get_all_watering_computers(self):
        all_sensors = set()
        for location in self.get_locations():
            for watering_computer in location.get_watering_computers():
                all_sensors.add(watering_computer)
        return all_sensors


