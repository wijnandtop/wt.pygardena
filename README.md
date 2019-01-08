# wt.pygardena
Python library to communicate with Gardana Smart
It gives an object oriented interface towards the Gardena Smart API (API usage is not officially supported by Gardena).
This library is written to be used to support gardena devices in https://www.home-assistant.io currently using my custom_component https://github.com/wijnandtop/home_assistant_gardena. It can be used for other purposes as well, since it doesn't have any home assistent specific implementations.

Inspired by: 
https://github.com/rcastberg/gardena_smart 

It is build to have limited interaction with the API of gardena. Fetching information is done via 2 calls.

* get all locations
* get devices per location

Objects fetch data from the internal state, update of internal state has to be explicitly triggered. 
 
## usage

```python
hub = GardenaSmartAccount("username", "password")
for location in hub.get_locations(): 
    for mower in location.get_mowers():
        print (mower.get_info())
    for sensor in location.get_sensors():
        print (sensor.get_info())
    for watering_computer in location.get_watering_computers():
        print (watering_computer.get_info())
```

## Object information

All object (except GardenaSmartAccount) have attributes which can be retrieved by either:
```python
object.get_info()
```
Which retuns a named list, or:
```python
#[attribute] needs to be replaced by the detail name.
object.get_[attribute].() 
```


## GardenaSmartAccount

Available methods:
```python
account.get_locations() # returns list of GardenaSmartLocation objects, if there is no internal state it will call the Gardena API
account.update_devices() # Loops over all locations and updates the internal state.
account.get_all_mowers() # Get all mowers from all locations.
account.get_all_sensors() # Get all sensors from all locations.
account.get_all_watering_computers() # Get all watering computers from all locations.
```

## GardenaSmartLocation

Available methods:
```python
location.update_devices() # updates the internal state of all devices in this location.
location.get_mowers() # Get all mowers from this location.
location.get_sensors() # Get all sensors from this location.
location.get_watering_computers() # Get all watering computers from this location.
```

## All devices

Have these details: category, battery_level, radio_quality, radio_connection_status
Extend from GardenaSmartDevice.
Currently it is not possible to update the internal state from a device.

## GardenaSmartMower

Available methods:
```python
mower.start() #starts mowing for a full day (can be specified)
mower.park_until_timer() #stop mowing and  wait for next schedule
mower.park() #stop mower, don't continue schedule

```
Available info: manual_operation, status, error, battery_charging, last_error_code, source_for_next_start, 
timestamp_next_start, cutting_time, charging_cycles, collisions, running_time

## GardenaSmartSensor

Available methods: none
Available info: ambient_temperature, ambient_frost_warning, soil_temperature, soil_humidity, light

## GardenaSmartWateringComputer

Available methods:
 ```python
 watering_computer.start() #starts watering for a 30 (can be specified)
 watering_computer.stop() #stop watering and  wait for next schedule 
 ```
 Available info:
ambient_temperature, ambient_frost_warning, valve_open, manual_override, 
button_manual_override_time, last_manual_override_time, scheduled_watering_next_start, 
scheduled_watering_end, adaptive_scheduling_last_decision 


## tested with:
 
 * Mower: smart SILENO Set (Article No. : 19060-60)
 * Watering computer: GARDENA smart Water Control (Article No. : 19031-20)
 * Sensor: GARDENA smart Sensor (Article No. : 19030-20)
 
## not planned yet

Since I do not own the devices, but feel free to sponsor me ;-)

* smart irrigation control (on top of my wishlist)
* Smart pressure pump
* smart power adapter
* smart battery

## Changelog

###0.9.3

Initial version

###0.9.4 - broken

* Change license to Apache 2.0
* RestAPI class that encapsulates API access
* Removed object_path dependency that occured just once
* update metadata

###0.9.5

* Reverted: Removed object_path dependency that occured just once





