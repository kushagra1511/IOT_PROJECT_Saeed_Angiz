# IoT Sensor System - Quick Reference Guide

**In The Name of God**

---

## Quick Import Reference

```python
# Import all sensor types
from sensor import (
    Sensor,              # Base class
    TemperatureSensor,   # Temperature measurement
    HumiditySensor,      # Humidity measurement
    MotionSensor,        # Motion detection
    LightSensor,         # Light intensity
    PressureSensor,      # Atmospheric pressure
    DHTSensor            # Combined temp + humidity
)
```

---

## Sensor Creation Cheat Sheet

### Temperature Sensor
```python
temp = TemperatureSensor(
    location='home',
    group='living_room',
    sensor_name='temp_001',
    min_temp=18,        # Optional, default: 18
    max_temp=30,        # Optional, default: 30
    unit='celsius'      # Optional, default: 'celsius'
)

# Read data
temp.read_data()              # Returns: 23.45
temp.read_data_with_unit()    # Returns: "23.45°C"
```

### Humidity Sensor
```python
humidity = HumiditySensor(
    location='home',
    group='bedroom',
    sensor_name='humid_001',
    min_humidity=30,    # Optional, default: 30
    max_humidity=80     # Optional, default: 80
)

# Read data
humidity.read_data()              # Returns: 65.32
humidity.read_data_with_unit()    # Returns: "65.32%"
humidity.get_comfort_level()      # Returns: "Comfortable"
```

### Motion Sensor
```python
motion = MotionSensor(
    location='home',
    group='hallway',
    sensor_name='motion_001',
    sensitivity=0.5     # Optional, default: 0.5 (range: 0.0-1.0)
)

# Read data
motion.read_data()                # Returns: True/False
motion.read_data_with_status()    # Returns: "Motion Detected!" or "No Motion"
motion.get_detection_count()      # Returns: 5
motion.reset_detection_count()    # Resets counter to 0
```

### Light Sensor
```python
light = LightSensor(
    location='home',
    group='kitchen',
    sensor_name='light_001',
    min_lux=0,          # Optional, default: 0
    max_lux=1000        # Optional, default: 1000
)

# Read data
light.read_data()              # Returns: 450.23
light.read_data_with_unit()    # Returns: "450.23 lux"
light.get_brightness_level()   # Returns: "Normal"
```

### Pressure Sensor
```python
pressure = PressureSensor(
    location='home',
    group='balcony',
    sensor_name='pressure_001',
    min_pressure=980,   # Optional, default: 980
    max_pressure=1050   # Optional, default: 1050
)

# Read data
pressure.read_data()              # Returns: 1013.25
pressure.read_data_with_unit()    # Returns: "1013.25 hPa"
pressure.get_weather_prediction() # Returns: "Fair"
```

### DHT Sensor (Combined)
```python
dht = DHTSensor(
    location='home',
    group='garage',
    sensor_name='dht_001',
    min_temp=18,        # Optional, default: 18
    max_temp=30,        # Optional, default: 30
    min_humidity=30,    # Optional, default: 30
    max_humidity=80     # Optional, default: 80
)

# Read data
dht.read_data()              # Returns: (23.45, 65.32)
dht.read_temperature()       # Returns: 23.45
dht.read_humidity()          # Returns: 65.32
dht.read_data_formatted()    # Returns: "Temperature: 23.45°C | Humidity: 65.32%"
```

---

## Common Methods (All Sensors)

```python
# Get sensor information
sensor.get_info()
# Returns: {
#     'sensor_name': 'temp_001',
#     'sensor_type': 'temperature',
#     'location': 'home',
#     'group': 'living_room'
# }

# String representation
print(sensor)
# Output: "Sensor: temp_001 | Type: temperature | Location: home/living_room"

# Access attributes
sensor.location       # 'home'
sensor.group          # 'living_room'
sensor.sensor_name    # 'temp_001'
sensor.sensor_type    # 'temperature'
```

---

## Common Patterns

### Pattern 1: Create Multiple Sensors
```python
sensors = {
    'temp': TemperatureSensor('home', 'living_room', 'temp_001'),
    'humid': HumiditySensor('home', 'living_room', 'humid_001'),
    'motion': MotionSensor('home', 'living_room', 'motion_001'),
    'light': LightSensor('home', 'living_room', 'light_001')
}

# Read all sensors
for name, sensor in sensors.items():
    print(f"{name}: {sensor.read_data()}")
```

### Pattern 2: Sensor Loop
```python
import time

temp = TemperatureSensor('home', 'room', 'temp_001')

# Read every 5 seconds
while True:
    temperature = temp.read_data()
    print(f"Temperature: {temperature}°C")
    time.sleep(5)
```

### Pattern 3: Conditional Actions
```python
light = LightSensor('home', 'room', 'light_001')

brightness = light.get_brightness_level()

if brightness == "Dark":
    print("Turn on lights")
elif brightness == "Very Bright":
    print("Close blinds")
```

### Pattern 4: Data Logging
```python
import datetime

def log_reading(sensor):
    timestamp = datetime.datetime.now()
    data = sensor.read_data()
    print(f"[{timestamp}] {sensor.sensor_name}: {data}")

# Log temperature
temp = TemperatureSensor('home', 'room', 'temp_001')
log_reading(temp)
```

### Pattern 5: Weather Station
```python
# Create weather sensors
temp = TemperatureSensor('home', 'outdoor', 'temp_outdoor')
humid = HumiditySensor('home', 'outdoor', 'humid_outdoor')
pressure = PressureSensor('home', 'outdoor', 'pressure_outdoor')

# Read all data
print(f"Temperature: {temp.read_data_with_unit()}")
print(f"Humidity: {humid.read_data_with_unit()}")
print(f"Pressure: {pressure.read_data_with_unit()}")
print(f"Forecast: {pressure.get_weather_prediction()}")
```

---

## Return Value Reference

| Sensor Type | Method | Return Type | Example |
|------------|--------|-------------|---------|
| Temperature | `read_data()` | float | `23.45` |
| Temperature | `read_data_with_unit()` | str | `"23.45°C"` |
| Humidity | `read_data()` | float | `65.32` |
| Humidity | `read_data_with_unit()` | str | `"65.32%"` |
| Humidity | `get_comfort_level()` | str | `"Comfortable"` |
| Motion | `read_data()` | bool | `True` |
| Motion | `read_data_with_status()` | str | `"Motion Detected!"` |
| Motion | `get_detection_count()` | int | `5` |
| Light | `read_data()` | float | `450.23` |
| Light | `read_data_with_unit()` | str | `"450.23 lux"` |
| Light | `get_brightness_level()` | str | `"Normal"` |
| Pressure | `read_data()` | float | `1013.25` |
| Pressure | `read_data_with_unit()` | str | `"1013.25 hPa"` |
| Pressure | `get_weather_prediction()` | str | `"Fair"` |
| DHT | `read_data()` | tuple | `(23.45, 65.32)` |
| DHT | `read_temperature()` | float | `23.45` |
| DHT | `read_humidity()` | float | `65.32` |
| DHT | `read_data_formatted()` | str | `"Temperature: 23.45°C..."` |

---

## Classification Values

### Humidity Comfort Levels
- **"Too Dry"** - Humidity < 30%
- **"Comfortable"** - Humidity 30-60%
- **"Humid"** - Humidity 60-70%
- **"Too Humid"** - Humidity > 70%

### Light Brightness Levels
- **"Dark"** - Light < 50 lux
- **"Dim"** - Light 50-200 lux
- **"Normal"** - Light 200-500 lux
- **"Bright"** - Light 500-800 lux
- **"Very Bright"** - Light > 800 lux

### Pressure Weather Predictions
- **"Stormy"** - Pressure < 1000 hPa
- **"Rainy"** - Pressure 1000-1010 hPa
- **"Changing"** - Pressure 1010-1020 hPa
- **"Fair"** - Pressure 1020-1030 hPa
- **"Very Dry"** - Pressure > 1030 hPa

---

## Default Parameter Values

| Sensor | Parameter | Default Value |
|--------|-----------|---------------|
| Temperature | min_temp | 18 |
| Temperature | max_temp | 30 |
| Temperature | unit | 'celsius' |
| Humidity | min_humidity | 30 |
| Humidity | max_humidity | 80 |
| Motion | sensitivity | 0.5 |
| Light | min_lux | 0 |
| Light | max_lux | 1000 |
| Pressure | min_pressure | 980 |
| Pressure | max_pressure | 1050 |
| DHT | min_temp | 18 |
| DHT | max_temp | 30 |
| DHT | min_humidity | 30 |
| DHT | max_humidity | 80 |

---

## One-Liner Examples

```python
# Quick temperature reading
print(TemperatureSensor('home', 'room', 'temp1').read_data())

# Quick motion check
if MotionSensor('home', 'hall', 'motion1', sensitivity=0.7).read_data():
    print("Motion!")

# Quick light level
print(LightSensor('home', 'room', 'light1').get_brightness_level())

# Quick weather
print(PressureSensor('home', 'outdoor', 'press1').get_weather_prediction())

# Quick DHT reading
temp, humid = DHTSensor('home', 'room', 'dht1').read_data()
```

---

## Troubleshooting Quick Fixes

### Problem: Import Error
```python
# Solution: Check file location
import sys
sys.path.append('/path/to/sensor/directory')
from sensor import TemperatureSensor
```

### Problem: NumPy Not Found
```bash
# Solution: Install NumPy
pip install numpy
```

### Problem: Wrong Temperature Range
```python
# Solution: Adjust min/max parameters
temp = TemperatureSensor('home', 'room', 'temp1', min_temp=15, max_temp=35)
```

### Problem: Motion Too Sensitive
```python
# Solution: Lower sensitivity
motion = MotionSensor('home', 'room', 'motion1', sensitivity=0.3)
```

---

## Complete Example Script

```python
"""
Complete IoT Sensor System Example
"""

from sensor import (
    TemperatureSensor,
    HumiditySensor,
    MotionSensor,
    LightSensor,
    PressureSensor,
    DHTSensor
)

# Create sensors
temp = TemperatureSensor('home', 'living_room', 'temp_001')
humid = HumiditySensor('home', 'living_room', 'humid_001')
motion = MotionSensor('home', 'hallway', 'motion_001', sensitivity=0.6)
light = LightSensor('home', 'kitchen', 'light_001')
pressure = PressureSensor('home', 'balcony', 'pressure_001')
dht = DHTSensor('home', 'bedroom', 'dht_001')

# Read all sensors
print("=== Sensor Readings ===")
print(f"Temperature: {temp.read_data_with_unit()}")
print(f"Humidity: {humid.read_data_with_unit()} ({humid.get_comfort_level()})")
print(f"Motion: {motion.read_data_with_status()}")
print(f"Light: {light.read_data_with_unit()} ({light.get_brightness_level()})")
print(f"Pressure: {pressure.read_data_with_unit()} ({pressure.get_weather_prediction()})")
print(f"DHT: {dht.read_data_formatted()}")
```

---

**In The Name of God**

*Quick Reference Guide - IoT Sensor System*  
*Author: Saeed Angiz | Course: IoT Programming with Python | Instructor: Aghaye Pilehvar*
