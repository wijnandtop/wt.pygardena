from .account import *
from .mower import *
from .sensor import *
from .watering_computer import *
import json

class GardenaSmartLocation:
    def __init__(self, rest_api, raw_data):
        self.rest_api = rest_api
        self.raw_data = raw_data
        self.raw_devices = None
        self.name = raw_data['name']
        self.id = raw_data['id']
        self.devices_mower = set()
        self.devices_sensor = set()
        self.devices_watering_computer = set()
        self.load_devices()

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_latitude(self):
        return self.raw_data['geo_position']['latitude']

    def get_longitude(self):
        return self.raw_data['geo_position']['longitude']

    def get_address(self):
        return self.raw_data['geo_position']['address']

    def get_city(self):
        return self.raw_data['geo_position']['city']

    def get_sunrise(self):
        return self.raw_data['geo_position']['sunrise']

    def get_sunset(self):
        return self.raw_data['geo_position']['sunset']

    def get_info(self):
        location_info = {}
        location_info['id'] = self.get_id()
        location_info['name'] = self.get_name()
        location_info['latitude'] = self.get_latitude()
        location_info['longitude'] = self.get_longitude()
        location_info['address'] = self.get_address()
        location_info['city'] = self.get_city()
        location_info['sunrise'] = self.get_sunrise()
        location_info['sunset'] = self.get_sunset()
        return location_info

    def update_devices(self):
        self.update_raw_data()
        for device in self.devices_mower:
            device.update()
        for device in self.devices_sensor:
            device.update()
        for device in self.devices_watering_computer:
            device.update()

    def update_raw_data(self):
        self.raw_devices = self.rest_api.get_devices(self.id)

    def get_raw_device_data(self, device_id):
        for device in self.raw_devices['devices']:
            if device['id'] == device_id:
                return device
        _LOGGER.warn('raw data not found for device: '+device_id)

    def get_mowers(self):
        return self.devices_mower

    def get_sensors(self):
        return self.devices_sensor

    def get_watering_computers(self):
        return self.devices_watering_computer

    def load_devices(self):
        self.update_raw_data()
        for device in self.raw_devices['devices']:
            if device['category'] == 'mower':
                self.devices_mower.add(GardenaSmartMower(self.rest_api, self, device))
            if device['category'] == 'sensor':
                self.devices_sensor.add(GardenaSmartSensor(self.rest_api, self, device))
            if device['category'] == 'watering_computer':
                self.devices_watering_computer.add(GardenaSmartWateringComputer(self.rest_api, self, device))


