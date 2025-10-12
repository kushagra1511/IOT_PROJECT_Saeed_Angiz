# IoT Sensor System Documentation

**In The Name of God**

**Author:** Saeed Angiz  
**Course:** IoT Programming with Python  
**Instructor:** Aghaye Pilehvar  
**Date:** 2024

---

## Table of Contents

1. [Overview](#overview)
2. [System Architecture](#system-architecture)
3. [Sensor Types](#sensor-types)
4. [Installation](#installation)
5. [Quick Start Guide](#quick-start-guide)
6. [Detailed Usage Examples](#detailed-usage-examples)
7. [API Reference](#api-reference)
8. [Best Practices](#best-practices)
9. [Troubleshooting](#troubleshooting)
10. [Future Enhancements](#future-enhancements)

---

## Overview

This IoT Sensor System is a comprehensive Python-based framework for managing and monitoring various types of sensors in a smart home or IoT environment. The system provides a clean, object-oriented architecture that makes it easy to:

- Create and manage multiple sensor types
- Read sensor data in real-time
- Organize sensors by location and groups
- Extend functionality with custom sensor types

### Key Features

- **6 Sensor Types:** Temperature, Humidity, Motion, Light, Pressure, and DHT (combined)
- **Object-Oriented Design:** Clean inheritance structure with base Sensor class
- **Realistic Data Simulation:** Uses NumPy for realistic sensor readings
- **Flexible Configuration:** Customizable ranges and parameters for each sensor
- **Easy Integration:** Simple API for reading and managing sensor data
- **Comprehensive Documentation:** Detailed docstrings and examples

---

## System Architecture

### Class Hierarchy

```
Sensor (Base Class)
├── TemperatureSensor
├── HumiditySensor
├── MotionSensor
├── LightSensor
├── PressureSensor
└── DHTSensor (Temperature + Humidity)
```

### Base Sensor Class

All sensors inherit from the base `Sensor` class, which provides:

- **Location tracking:** Physical location (e.g., 'home', 'office')
- **Group management:** Room/area grouping (e.g., 'living_room', 'bedroom')
- **Sensor identification:** Unique name and type
- **Data reading:** Basic `read_data()` method
- **Information retrieval:** `get_info()` method for sensor details

---

## Sensor Types

### 1. Temperature Sensor

**Purpose:** Measures temperature in Celsius or Fahrenheit

**Features:**
- Configurable temperature range
- Unit conversion (Celsius ↔ Fahrenheit)
- Realistic temperature simulation

**Use Cases:**
- Room temperature monitoring
- HVAC control systems
- Weather stations

### 2. Humidity Sensor

**Purpose:** Measures relative humidity as percentage

**Features:**
- Configurable humidity range (0-100%)
- Comfort level assessment
- Humidity trend analysis

**Use Cases:**
- Indoor air quality monitoring
- Greenhouse automation
- Mold prevention systems

### 3. Motion Sensor

**Purpose:** Detects movement/motion

**Features:**
- Adjustable sensitivity (0.0 - 1.0)
- Detection counting
- Real-time motion status

**Use Cases:**
- Security systems
- Automatic lighting
- Occupancy detection

### 4. Light Sensor

**Purpose:** Measures light intensity in Lux

**Features:**
- Configurable light range (0-1000+ lux)
- Brightness level classification
- Day/night detection

**Use Cases:**
- Automatic lighting control
- Energy management
- Circadian rhythm monitoring

### 5. Pressure Sensor

**Purpose:** Measures atmospheric pressure in hPa

**Features:**
- Configurable pressure range
- Weather prediction
- Altitude estimation

**Use Cases:**
- Weather forecasting
- Altitude measurement
- Barometric trend analysis

### 6. DHT Sensor

**Purpose:** Combined temperature and humidity measurement

**Features:**
- Simultaneous temp + humidity reading
- Individual or combined data access
- Simulates DHT11/DHT22 sensors

**Use Cases:**
- Comprehensive climate monitoring
- Smart home automation
- Agricultural applications

---

## Installation

### Prerequisites

- Python 3.7 or higher
- NumPy library

### Step 1: Install Python

If you don't have Python installed:

**Windows:**
```bash
# Download from python.org and install
# Or use winget:
winget install Python.Python.3.11
```

**Linux/Mac:**
```bash
# Usually pre-installed, or use:
sudo apt install python3 python3-pip  # Ubuntu/Debian
brew install python3                   # macOS
```

### Step 2: Install NumPy

```bash
pip install numpy
```

### Step 3: Download sensor.py

Place the `sensor.py` file in your project directory.

### Step 4: Verify Installation

```python
# test_installation.py
from sensor import Sensor, TemperatureSensor

print("Installation successful!")
temp = TemperatureSensor('home', 'test', 'test_sensor')
print(f"Test reading: {temp.read_data()}°C")
```

---

## Quick Start Guide

### Example 1: Basic Temperature Sensor

```python
from sensor import TemperatureSensor

# Create a temperature sensor
temp_sensor = TemperatureSensor(
    location='home',
    group='living_room',
    sensor_name='temp_001'
)

# Read temperature
temperature = temp_sensor.read_data()
print(f"Temperature: {temperature}°C")

# Read with unit
print(temp_sensor.read_data_with_unit())  # "23.45°C"
```

### Example 2: Motion Detection

```python
from sensor import MotionSensor

# Create motion sensor with high sensitivity
motion = MotionSensor(
    location='home',
    group='hallway',
    sensor_name='motion_001',
    sensitivity=0.8  # 80% detection probability
)

# Check for motion
if motion.read_data():
    print("Motion detected!")
else:
    print("No motion")

# Get detection count
print(f"Total detections: {motion.get_detection_count()}")
```

### Example 3: DHT Sensor (Combined)

```python
from sensor import DHTSensor

# Create DHT sensor
dht = DHTSensor(
    location='home',
    group='bedroom',
    sensor_name='dht_001'
)

# Read both values
temp, humidity = dht.read_data()
print(f"Temperature: {temp}°C")
print(f"Humidity: {humidity}%")

# Or use formatted output
print(dht.read_data_formatted())
# Output: "Temperature: 23.45°C | Humidity: 65.32%"
```

---

## Detailed Usage Examples

### Creating Multiple Sensors

```python
from sensor import (
    TemperatureSensor,
    HumiditySensor,
    MotionSensor,
    LightSensor
)

# Create sensor network for living room
living_room_sensors = {
    'temperature': TemperatureSensor('home', 'living_room', 'temp_lr_001'),
    'humidity': HumiditySensor('home', 'living_room', 'humid_lr_001'),
    'motion': MotionSensor('home', 'living_room', 'motion_lr_001'),
    'light': LightSensor('home', 'living_room', 'light_lr_001')
}

# Read all sensors
for sensor_type, sensor in living_room_sensors.items():
    print(f"{sensor_type}: {sensor.read_data()}")
```

### Custom Temperature Range

```python
from sensor import TemperatureSensor

# Freezer temperature sensor (-20°C to -10°C)
freezer_sensor = TemperatureSensor(
    location='home',
    group='kitchen',
    sensor_name='freezer_temp',
    min_temp=-20,
    max_temp=-10
)

print(f"Freezer: {freezer_sensor.read_data()}°C")

# Outdoor sensor (wider range)
outdoor_sensor = TemperatureSensor(
    location='home',
    group='outdoor',
    sensor_name='outdoor_temp',
    min_temp=-10,
    max_temp=40
)

print(f"Outdoor: {outdoor_sensor.read_data()}°C")
```

### Motion Sensor with Logging

```python
from sensor import MotionSensor
import time

motion = MotionSensor('home', 'entrance', 'motion_entrance', sensitivity=0.6)

print("Monitoring for 10 seconds...")
for i in range(10):
    if motion.read_data():
        print(f"[{i}s] Motion detected!")
    time.sleep(1)

print(f"\nTotal detections: {motion.get_detection_count()}")
```

### Light-Based Automation

```python
from sensor import LightSensor

light = LightSensor('home', 'living_room', 'light_001')

# Read light level
lux = light.read_data()
brightness = light.get_brightness_level()

print(f"Light: {lux} lux ({brightness})")

# Automation logic
if brightness == "Dark":
    print("Action: Turn on lights")
elif brightness == "Very Bright":
    print("Action: Close blinds")
else:
    print("Action: No change needed")
```

### Weather Station with Pressure Sensor

```python
from sensor import PressureSensor, TemperatureSensor, HumiditySensor

# Create weather station sensors
pressure = PressureSensor('home', 'balcony', 'pressure_001')
temp = TemperatureSensor('home', 'balcony', 'temp_outdoor')
humidity = HumiditySensor('home', 'balcony', 'humid_outdoor')

# Read weather data
print("=== Weather Station ===")
print(f"Temperature: {temp.read_data_with_unit()}")
print(f"Humidity: {humidity.read_data_with_unit()}")
print(f"Pressure: {pressure.read_data_with_unit()}")
print(f"Forecast: {pressure.get_weather_prediction()}")
print(f"Comfort: {humidity.get_comfort_level()}")
```

---

## API Reference

### Base Sensor Class

#### `__init__(location, group, sensor_type, sensor_name)`
Initialize a sensor.

**Parameters:**
- `location` (str): Physical location
- `group` (str): Group/room name
- `sensor_type` (str): Type of sensor
- `sensor_name` (str): Unique identifier

#### `read_data()`
Read sensor data (returns default value of 25).

**Returns:** int

#### `get_info()`
Get sensor information dictionary.

**Returns:** dict with keys: sensor_name, sensor_type, location, group

---

### TemperatureSensor

#### `__init__(location, group, sensor_name, min_temp=18, max_temp=30, unit='celsius')`

**Additional Parameters:**
- `min_temp` (float): Minimum temperature
- `max_temp` (float): Maximum temperature
- `unit` (str): 'celsius' or 'fahrenheit'

#### `read_data()`
**Returns:** float (temperature value)

#### `read_data_with_unit()`
**Returns:** str (e.g., "23.45°C")

#### `convert_to_fahrenheit(celsius)`
**Returns:** float

#### `convert_to_celsius(fahrenheit)`
**Returns:** float

---

### HumiditySensor

#### `__init__(location, group, sensor_name, min_humidity=30, max_humidity=80)`

**Additional Parameters:**
- `min_humidity` (float): Minimum humidity %
- `max_humidity` (float): Maximum humidity %

#### `read_data()`
**Returns:** float (humidity percentage)

#### `read_data_with_unit()`
**Returns:** str (e.g., "65.32%")

#### `get_comfort_level()`
**Returns:** str ("Too Dry", "Comfortable", "Humid", "Too Humid")

---

### MotionSensor

#### `__init__(location, group, sensor_name, sensitivity=0.5)`

**Additional Parameters:**
- `sensitivity` (float): Detection sensitivity (0.0 - 1.0)

#### `read_data()`
**Returns:** bool (True if motion detected)

#### `read_data_with_status()`
**Returns:** str ("Motion Detected!" or "No Motion")

#### `get_detection_count()`
**Returns:** int (total detections)

#### `reset_detection_count()`
Resets counter to 0.

---

### LightSensor

#### `__init__(location, group, sensor_name, min_lux=0, max_lux=1000)`

**Additional Parameters:**
- `min_lux` (float): Minimum light intensity
- `max_lux` (float): Maximum light intensity

#### `read_data()`
**Returns:** float (light intensity in lux)

#### `read_data_with_unit()`
**Returns:** str (e.g., "450.23 lux")

#### `get_brightness_level()`
**Returns:** str ("Dark", "Dim", "Normal", "Bright", "Very Bright")

---

### PressureSensor

#### `__init__(location, group, sensor_name, min_pressure=980, max_pressure=1050)`

**Additional Parameters:**
- `min_pressure` (float): Minimum pressure (hPa)
- `max_pressure` (float): Maximum pressure (hPa)

#### `read_data()`
**Returns:** float (pressure in hPa)

#### `read_data_with_unit()`
**Returns:** str (e.g., "1013.25 hPa")

#### `get_weather_prediction()`
**Returns:** str ("Stormy", "Rainy", "Changing", "Fair", "Very Dry")

---

### DHTSensor

#### `__init__(location, group, sensor_name, min_temp=18, max_temp=30, min_humidity=30, max_humidity=80)`

**Additional Parameters:**
- `min_temp` (float): Minimum temperature
- `max_temp` (float): Maximum temperature
- `min_humidity` (float): Minimum humidity
- `max_humidity` (float): Maximum humidity

#### `read_data()`
**Returns:** tuple (temperature, humidity)

#### `read_temperature()`
**Returns:** float (temperature only)

#### `read_humidity()`
**Returns:** float (humidity only)

#### `read_data_formatted()`
**Returns:** str (formatted output)

---

## Best Practices

### 1. Sensor Naming Convention

Use descriptive, consistent names:

```python
# Good
temp_living_room_001 = TemperatureSensor('home', 'living_room', 'temp_lr_001')
motion_entrance_main = MotionSensor('home', 'entrance', 'motion_ent_main')

# Avoid
sensor1 = TemperatureSensor('home', 'living_room', 's1')
x = MotionSensor('home', 'entrance', 'x')
```

### 2. Group Organization

Organize sensors by physical location:

```python
# Create sensor groups
bedroom_sensors = [
    TemperatureSensor('home', 'bedroom', 'temp_bed_001'),
    HumiditySensor('home', 'bedroom', 'humid_bed_001'),
    LightSensor('home', 'bedroom', 'light_bed_001')
]

kitchen_sensors = [
    TemperatureSensor('home', 'kitchen', 'temp_kit_001'),
    MotionSensor('home', 'kitchen', 'motion_kit_001')
]
```

### 3. Error Handling

Always handle potential errors:

```python
try:
    temp = temp_sensor.read_data()
    if temp < 0:
        print("Warning: Temperature below freezing!")
except Exception as e:
    print(f"Error reading sensor: {e}")
```

### 4. Data Logging

Log sensor data for analysis:

```python
import datetime

def log_sensor_data(sensor):
    timestamp = datetime.datetime.now()
    data = sensor.read_data()
    
    with open('sensor_log.txt', 'a') as f:
        f.write(f"{timestamp},{sensor.sensor_name},{data}\n")
```

### 5. Sensor Calibration

Adjust ranges based on real-world conditions:

```python
# Calibrate based on actual environment
bedroom_temp = TemperatureSensor(
    'home', 'bedroom', 'temp_bed_001',
    min_temp=18,  # Typical night temperature
    max_temp=26   # Typical day temperature
)
```

---

## Troubleshooting

### Issue 1: Import Error

**Problem:** `ModuleNotFoundError: No module named 'sensor'`

**Solution:**
- Ensure `sensor.py` is in the same directory as your script
- Or add the directory to Python path:
```python
import sys
sys.path.append('/path/to/sensor/directory')
from sensor import TemperatureSensor
```

### Issue 2: NumPy Not Found

**Problem:** `ModuleNotFoundError: No module named 'numpy'`

**Solution:**
```bash
pip install numpy
# or
pip3 install numpy
```

### Issue 3: Unrealistic Sensor Values

**Problem:** Sensor readings don't match expected range

**Solution:**
- Check min/max parameters in constructor
- Verify unit settings (Celsius vs Fahrenheit)
```python
# Correct
temp = TemperatureSensor('home', 'room', 'temp1', min_temp=18, max_temp=30)

# Check current settings
print(f"Range: {temp.min_temp}°C to {temp.max_temp}°C")
```

### Issue 4: Motion Sensor Always Detecting

**Problem:** Motion sensor returns True too frequently

**Solution:**
- Reduce sensitivity parameter
```python
# Too sensitive
motion = MotionSensor('home', 'room', 'motion1', sensitivity=0.9)

# Better
motion = MotionSensor('home', 'room', 'motion1', sensitivity=0.3)
```

---

## Future Enhancements

### Planned Features

1. **Data Persistence**
   - Save sensor readings to database
   - Historical data analysis
   - Trend visualization

2. **Real Hardware Integration**
   - Raspberry Pi GPIO support
   - Arduino serial communication
   - MQTT protocol support

3. **Advanced Analytics**
   - Machine learning predictions
   - Anomaly detection
   - Pattern recognition

4. **Web Interface**
   - Real-time dashboard
   - Remote monitoring
   - Mobile app integration

5. **Additional Sensor Types**
   - Gas sensors (CO2, CO, etc.)
   - Sound/noise sensors
   - Vibration sensors
   - Proximity sensors

6. **Automation Rules**
   - Trigger-based actions
   - Conditional logic
   - Scene management

---

## Contributing

This project was created as part of an IoT programming course. Suggestions and improvements are welcome!

### How to Contribute

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

---

## License

This project is created for educational purposes as part of the IoT Programming course taught by Aghaye Pilehvar.

---

## Contact

**Author:** Saeed Angiz  
**Course:** IoT Programming with Python  
**Instructor:** Aghaye Pilehvar

---

## Acknowledgments

- **Instructor:** Aghaye Pilehvar for excellent teaching and guidance
- **NumPy:** For providing powerful numerical computing capabilities
- **Python Community:** For comprehensive documentation and support

---

**In The Name of God**

*Last Updated: 2024*
