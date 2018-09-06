# wt.pygardena
Python library to communicate with Gardana Smart
It gives an object oriented interface towards the Gardena Smart API (API usage is not officially supported by Gardena).
T
his library is written to be used to support gardena devices in https://www.home-assistant.io currently using my custom_component https://github.com/wijnandtop/home_assistant_gardena. It can be used for other purposes as well, since it doesn't have any home assistent specific implementations.

Inspired by: 
https://github.com/rcastberg/gardena_smart 

It is build to have limited interaction with the API of gardena. Fetching information is done via 2 call's.

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

## GardenaSmartAccount

Available methods:
* get_locations() - returns list of GardenaSmartLocation objects, if there is no internal state it will call the Gardena API
* update_devices() - Loops over all locations and updates the internal state.
* get_all_mowers() - Get all mowers from all locations.
* get_all_sensors() - Get all sensors from all locations.
* get_all_watering_computers() - Get all watering computers from all locations.

## devices
All devices are represented by an object, all object do have a method to expose all details as a named list. 
```python
object.get_info()
```
All devices have these details: category, battery_level, radio_quality, radio_connection_status
All details are available via getters so:
```python
#[detail] needs to be replaced by the detail name.
object.get_[detail].() 
```

### mower
Actions:
```python
mower.start() #starts mowing for a full day (can be specified)
mower.park_until_timer() #stop mowing and  wait for next schedule
mower.park() #stop mower, don't continue schedule

```
Available info: manual_operation, status, error, battery_charging, last_error_code, source_for_next_start, 
timestamp_next_start, cutting_time, charging_cycles, collisions, running_time

## sensor
Actions: none
Available info: ambient_temperature, ambient_frost_warning, soil_temperature, soil_humidity, light

## watering computer
Actions:
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

* Smart pressure pump
* smart power adapter
* smart battery
* smart irrigation control (is on my wishlist)



