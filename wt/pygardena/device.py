from .account import *

class GardenaSmartDevice:
    def __init__(self, rest_api, location, raw_data):
        self.rest_api = rest_api
        self.location = location
        self.raw_data = raw_data
        self.name = raw_data['name']
        self.zone = None
        self.id = raw_data['id']
        self.category = 'unknown'
        self.update()

    def get_value_of_property(self, ability, property):
        for data_ability in self.raw_data['abilities']:
            if data_ability['type'] != ability:
                continue
            for data_property in data_ability['properties']:
                if data_property['name'] == property:
                    return data_property['value']
        return None

    def update(self):
        self.raw_data = self.location.get_raw_device_data(self.id)

    def get_category(self):
        return self.category

    def get_battery_level(self):
        return self.get_value_of_property('battery_power', 'level')

    def get_radio_quality(self):
        return self.get_value_of_property('radio_link', 'quality')

    def get_radio_connection_status(self):
        return self.get_value_of_property('radio_link', 'connection_status')

    def get_radio_state(self):
        return self.get_value_of_property('radio_link', 'state')

    def get_info(self):
        device_info = {}
        device_info['category'] = self.get_category()
        device_info['battery_level'] = self.get_battery_level()
        device_info['radio_quality'] = self.get_radio_quality()
        device_info['radio_connection_status'] = self.get_radio_connection_status()
        device_info['radio_state'] = self.get_radio_state()
        return device_info

    def send_command(self, name, parameters=None):
        self.rest_api.post_command(self, name, parameters)