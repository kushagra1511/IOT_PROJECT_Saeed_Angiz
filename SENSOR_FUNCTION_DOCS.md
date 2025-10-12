# IoT Sensor System - Complete Function Documentation

**In The Name of God**

---

## Table of Contents

1. [Base Sensor Class](#base-sensor-class)
2. [TemperatureSensor Class](#temperaturesensor-class)
3. [HumiditySensor Class](#humiditysensor-class)
4. [MotionSensor Class](#motionsensor-class)
5. [LightSensor Class](#lightsensor-class)
6. [PressureSensor Class](#pressuresensor-class)
7. [DHTSensor Class](#dhtsensor-class)

---

## Base Sensor Class

### Class: `Sensor`

**Description:**  
Base class for all sensors in the IoT system. Provides fundamental sensor functionality including location tracking, grouping, and basic data reading.

**Inheritance:**  
None (base class)

**Attributes:**

| Attribute | Type | Description |
|-----------|------|-------------|
| `location` | str | Physical location of the sensor (e.g., 'home', 'office') |
| `group` | str | Group/room where sensor is located (e.g., 'living_room') |
| `sensor_name` | str | Unique identifier for the sensor |
| `sensor_type` | str | Type of sensor (e.g., 'temperature', 'humidity') |

---

### Method: `__init__(location, group, sensor_type, sensor_name)`

**Description:**  
Initialize a new Sensor object.

**Parameters:**

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `location` | str | Yes | - | Physical location of the sensor |
| `group` | str | Yes | - | Group/room where sensor is located |
| `sensor_type` | str | Yes | - | Type of sensor |
| `sensor_name` | str | Yes | - | Unique identifier for the sensor |

**Returns:**  
None

**Example:**
```python
sensor = Sensor('home', 'living_room', 'generic', 'sensor_001')
```

---

### Method: `read_data()`

**Description:**  
Read data from the sensor. This is a basic implementation that returns a default value. Specific sensor types should override this method.

**Parameters:**  
None

**Returns:**

| Type | Description |
|------|-------------|
| int | Default sensor reading value (25) |

**Example:**
```python
data = sensor.read_data()
print(data)  # Output: 25
```

---

### Method: `get_info()`

**Description:**  
Get complete information about the sensor.

**Parameters:**  
None

**Returns:**

| Type | Description |
|------|-------------|
| dict | Dictionary containing all sensor information |

**Dictionary Keys:**
- `sensor_name` (str): Sensor's unique name
- `sensor_type` (str): Type of sensor
- `location` (str): Physical location
- `group` (str): Group/room name

**Example:**
```python
info = sensor.get_info()
print(info)
# Output: {
#     'sensor_name': 'sensor_001',
#     'sensor_type': 'generic',
#     'location': 'home',
#     'group': 'living_room'
# }
```

---

### Method: `__str__()`

**Description:**  
String representation of the sensor.

**Parameters:**  
None

**Returns:**

| Type | Description |
|------|-------------|
| str | Formatted string with sensor details |

**Example:**
```python
print(sensor)
# Output: "Sensor: sensor_001 | Type: generic | Location: home/living_room"
```

---

## TemperatureSensor Class

### Class: `TemperatureSensor`

**Description:**  
Specialized sensor for measuring temperature. Provides realistic temperature readings with configurable range and unit conversion capabilities.

**Inheritance:**  
Inherits from `Sensor`

**Additional Attributes:**

| Attribute | Type | Description |
|-----------|------|-------------|
| `min_temp` | float | Minimum temperature value (default: 18°C) |
| `max_temp` | float | Maximum temperature value (default: 30°C) |
| `unit` | str | Temperature unit ('celsius' or 'fahrenheit') |

---

### Method: `__init__(location, group, sensor_name, min_temp=18, max_temp=30, unit='celsius')`

**Description:**  
Initialize a Temperature Sensor.

**Parameters:**

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `location` | str | Yes | - | Physical location of the sensor |
| `group` | str | Yes | - | Group/room where sensor is located |
| `sensor_name` | str | Yes | - | Unique identifier for the sensor |
| `min_temp` | float | No | 18 | Minimum temperature reading |
| `max_temp` | float | No | 30 | Maximum temperature reading |
| `unit` | str | No | 'celsius' | Temperature unit |

**Returns:**  
None

**Example:**
```python
# Default range (18-30°C)
temp1 = TemperatureSensor('home', 'living_room', 'temp_001')

# Custom range
temp2 = TemperatureSensor('home', 'freezer', 'temp_002', min_temp=-20, max_temp=-10)

# Fahrenheit
temp3 = TemperatureSensor('home', 'room', 'temp_003', unit='fahrenheit')
```

---

### Method: `read_data()`

**Description:**  
Read temperature data from the sensor. Generates a random temperature value within the configured range.

**Parameters:**  
None

**Returns:**

| Type | Description |
|------|-------------|
| float | Temperature reading in specified unit |

**Example:**
```python
temperature = temp_sensor.read_data()
print(temperature)  # Output: 23.45
```

---

### Method: `read_data_with_unit()`

**Description:**  
Read temperature data with unit label.

**Parameters:**  
None

**Returns:**

| Type | Description |
|------|-------------|
| str | Temperature reading with unit (e.g., "23.45°C") |

**Example:**
```python
temp_str = temp_sensor.read_data_with_unit()
print(temp_str)  # Output: "23.45°C"
```

---

### Method: `convert_to_fahrenheit(celsius)`

**Description:**  
Convert Celsius to Fahrenheit.

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `celsius` | float | Yes | Temperature in Celsius |

**Returns:**

| Type | Description |
|------|-------------|
| float | Temperature in Fahrenheit |

**Formula:**  
`F = (C × 9/5) + 32`

**Example:**
```python
fahrenheit = temp_sensor.convert_to_fahrenheit(25)
print(fahrenheit)  # Output: 77.0
```

---

### Method: `convert_to_celsius(fahrenheit)`

**Description:**  
Convert Fahrenheit to Celsius.

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `fahrenheit` | float | Yes | Temperature in Fahrenheit |

**Returns:**

| Type | Description |
|------|-------------|
| float | Temperature in Celsius |

**Formula:**  
`C = (F - 32) × 5/9`

**Example:**
```python
celsius = temp_sensor.convert_to_celsius(77)
print(celsius)  # Output: 25.0
```

---

## HumiditySensor Class

### Class: `HumiditySensor`

**Description:**  
Specialized sensor for measuring humidity levels. Provides humidity readings as percentage with comfort level assessment.

**Inheritance:**  
Inherits from `Sensor`

**Additional Attributes:**

| Attribute | Type | Description |
|-----------|------|-------------|
| `min_humidity` | float | Minimum humidity percentage (default: 30%) |
| `max_humidity` | float | Maximum humidity percentage (default: 80%) |

---

### Method: `__init__(location, group, sensor_name, min_humidity=30, max_humidity=80)`

**Description:**  
Initialize a Humidity Sensor.

**Parameters:**

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `location` | str | Yes | - | Physical location of the sensor |
| `group` | str | Yes | - | Group/room where sensor is located |
| `sensor_name` | str | Yes | - | Unique identifier for the sensor |
| `min_humidity` | float | No | 30 | Minimum humidity reading |
| `max_humidity` | float | No | 80 | Maximum humidity reading |

**Returns:**  
None

**Example:**
```python
# Default range (30-80%)
humid1 = HumiditySensor('home', 'bedroom', 'humid_001')

# Custom range
humid2 = HumiditySensor('home', 'bathroom', 'humid_002', min_humidity=40, max_humidity=90)
```

---

### Method: `read_data()`

**Description:**  
Read humidity data from the sensor. Generates a random humidity value within the configured range.

**Parameters:**  
None

**Returns:**

| Type | Description |
|------|-------------|
| float | Humidity reading as percentage |

**Example:**
```python
humidity = humid_sensor.read_data()
print(humidity)  # Output: 65.32
```

---

### Method: `read_data_with_unit()`

**Description:**  
Read humidity data with percentage symbol.

**Parameters:**  
None

**Returns:**

| Type | Description |
|------|-------------|
| str | Humidity reading with % symbol (e.g., "65.32%") |

**Example:**
```python
humid_str = humid_sensor.read_data_with_unit()
print(humid_str)  # Output: "65.32%"
```

---

### Method: `get_comfort_level()`

**Description:**  
Determine comfort level based on humidity reading.

**Parameters:**  
None

**Returns:**

| Type | Description |
|------|-------------|
| str | Comfort level description |

**Return Values:**

| Range | Return Value |
|-------|--------------|
| < 30% | "Too Dry" |
| 30-60% | "Comfortable" |
| 60-70% | "Humid" |
| > 70% | "Too Humid" |

**Example:**
```python
comfort = humid_sensor.get_comfort_level()
print(comfort)  # Output: "Comfortable"
```

---

## MotionSensor Class

### Class: `MotionSensor`

**Description:**  
Specialized sensor for detecting motion/movement. Returns boolean values indicating motion detection with configurable sensitivity.

**Inheritance:**  
Inherits from `Sensor`

**Additional Attributes:**

| Attribute | Type | Description |
|-----------|------|-------------|
| `sensitivity` | float | Detection sensitivity (0.0 to 1.0) |
| `detection_count` | int | Number of times motion was detected |

---

### Method: `__init__(location, group, sensor_name, sensitivity=0.5)`

**Description:**  
Initialize a Motion Sensor.

**Parameters:**

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `location` | str | Yes | - | Physical location of the sensor |
| `group` | str | Yes | - | Group/room where sensor is located |
| `sensor_name` | str | Yes | - | Unique identifier for the sensor |
| `sensitivity` | float | No | 0.5 | Detection sensitivity (0.0-1.0) |

**Sensitivity Guide:**
- `0.0-0.3`: Low sensitivity (fewer false positives)
- `0.4-0.6`: Medium sensitivity (balanced)
- `0.7-1.0`: High sensitivity (more detections)

**Returns:**  
None

**Example:**
```python
# Default sensitivity (50%)
motion1 = MotionSensor('home', 'hallway', 'motion_001')

# High sensitivity (80%)
motion2 = MotionSensor('home', 'entrance', 'motion_002', sensitivity=0.8)

# Low sensitivity (30%)
motion3 = MotionSensor('home', 'garage', 'motion_003', sensitivity=0.3)
```

---

### Method: `read_data()`

**Description:**  
Read motion detection data. Simulates motion detection based on sensitivity level. Higher sensitivity = more likely to detect motion.

**Parameters:**  
None

**Returns:**

| Type | Description |
|------|-------------|
| bool | True if motion detected, False otherwise |

**Side Effects:**  
Increments `detection_count` when motion is detected.

**Example:**
```python
if motion_sensor.read_data():
    print("Motion detected!")
else:
    print("No motion")
```

---

### Method: `read_data_with_status()`

**Description:**  
Read motion data with status message.

**Parameters:**  
None

**Returns:**

| Type | Description |
|------|-------------|
| str | Motion status message |

**Return Values:**
- `"Motion Detected!"` - When motion is detected
- `"No Motion"` - When no motion is detected

**Example:**
```python
status = motion_sensor.read_data_with_status()
print(status)  # Output: "Motion Detected!" or "No Motion"
```

---

### Method: `get_detection_count()`

**Description:**  
Get total number of motion detections since sensor creation or last reset.

**Parameters:**  
None

**Returns:**

| Type | Description |
|------|-------------|
| int | Total detection count |

**Example:**
```python
count = motion_sensor.get_detection_count()
print(f"Total detections: {count}")  # Output: "Total detections: 5"
```

---

### Method: `reset_detection_count()`

**Description:**  
Reset the motion detection counter to zero.

**Parameters:**  
None

**Returns:**  
None

**Side Effects:**  
Prints confirmation message and resets `detection_count` to 0.

**Example:**
```python
motion_sensor.reset_detection_count()
# Output: "Detection count reset for motion_001"
```

---

## LightSensor Class

### Class: `LightSensor`

**Description:**  
Specialized sensor for measuring light intensity. Measures in Lux (light intensity unit) with brightness level classification.

**Inheritance:**  
Inherits from `Sensor`

**Additional Attributes:**

| Attribute | Type | Description |
|-----------|------|-------------|
| `min_lux` | float | Minimum light intensity (default: 0 lux) |
| `max_lux` | float | Maximum light intensity (default: 1000 lux) |

---

### Method: `__init__(location, group, sensor_name, min_lux=0, max_lux=1000)`

**Description:**  
Initialize a Light Sensor.

**Parameters:**

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `location` | str | Yes | - | Physical location of the sensor |
| `group` | str | Yes | - | Group/room where sensor is located |
| `sensor_name` | str | Yes | - | Unique identifier for the sensor |
| `min_lux` | float | No | 0 | Minimum light reading |
| `max_lux` | float | No | 1000 | Maximum light reading |

**Lux Reference:**
- 0-50: Dark
- 50-200: Dim indoor lighting
- 200-500: Normal indoor lighting
- 500-1000: Bright indoor lighting
- 1000+: Daylight

**Returns:**  
None

**Example:**
```python
# Default range (0-1000 lux)
light1 = LightSensor('home', 'living_room', 'light_001')

# Outdoor sensor (higher range)
light2 = LightSensor('home', 'outdoor', 'light_002', min_lux=0, max_lux=10000)
```

---

### Method: `read_data()`

**Description:**  
Read light intensity data. Generates a random light intensity value within the configured range.

**Parameters:**  
None

**Returns:**

| Type | Description |
|------|-------------|
| float | Light intensity in Lux |

**Example:**
```python
lux = light_sensor.read_data()
print(lux)  # Output: 450.23
```

---

### Method: `read_data_with_unit()`

**Description:**  
Read light data with unit label.

**Parameters:**  
None

**Returns:**

| Type | Description |
|------|-------------|
| str | Light intensity with unit (e.g., "450.23 lux") |

**Example:**
```python
light_str = light_sensor.read_data_with_unit()
print(light_str)  # Output: "450.23 lux"
```

---

### Method: `get_brightness_level()`

**Description:**  
Determine brightness level based on light reading.

**Parameters:**  
None

**Returns:**

| Type | Description |
|------|-------------|
| str | Brightness level description |

**Return Values:**

| Range | Return Value |
|-------|--------------|
| < 50 lux | "Dark" |
| 50-200 lux | "Dim" |
| 200-500 lux | "Normal" |
| 500-800 lux | "Bright" |
| > 800 lux | "Very Bright" |

**Example:**
```python
brightness = light_sensor.get_brightness_level()
print(brightness)  # Output: "Normal"
```

---

## PressureSensor Class

### Class: `PressureSensor`

**Description:**  
Specialized sensor for measuring atmospheric pressure. Measures in hPa (hectopascals) with weather prediction capability.

**Inheritance:**  
Inherits from `Sensor`

**Additional Attributes:**

| Attribute | Type | Description |
|-----------|------|-------------|
| `min_pressure` | float | Minimum pressure (default: 980 hPa) |
| `max_pressure` | float | Maximum pressure (default: 1050 hPa) |

---

### Method: `__init__(location, group, sensor_name, min_pressure=980, max_pressure=1050)`

**Description:**  
Initialize a Pressure Sensor.

**Parameters:**

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `location` | str | Yes | - | Physical location of the sensor |
| `group` | str | Yes | - | Group/room where sensor is located |
| `sensor_name` | str | Yes | - | Unique identifier for the sensor |
| `min_pressure` | float | No | 980 | Minimum pressure reading |
| `max_pressure` | float | No | 1050 | Maximum pressure reading |

**Pressure Reference:**
- < 1000 hPa: Low pressure (stormy)
- 1013 hPa: Standard atmospheric pressure at sea level
- > 1030 hPa: High pressure (fair weather)

**Returns:**  
None

**Example:**
```python
# Default range (980-1050 hPa)
pressure1 = PressureSensor('home', 'balcony', 'pressure_001')

# Custom range
pressure2 = PressureSensor('home', 'outdoor', 'pressure_002', min_pressure=950, max_pressure=1080)
```

---

### Method: `read_data()`

**Description:**  
Read atmospheric pressure data. Generates a random pressure value within the configured range.

**Parameters:**  
None

**Returns:**

| Type | Description |
|------|-------------|
| float | Atmospheric pressure in hPa |

**Example:**
```python
pressure = pressure_sensor.read_data()
print(pressure)  # Output: 1013.25
```

---

### Method: `read_data_with_unit()`

**Description:**  
Read pressure data with unit label.

**Parameters:**  
None

**Returns:**

| Type | Description |
|------|-------------|
| str | Pressure reading with unit (e.g., "1013.25 hPa") |

**Example:**
```python
pressure_str = pressure_sensor.read_data_with_unit()
print(pressure_str)  # Output: "1013.25 hPa"
```

---

### Method: `get_weather_prediction()`

**Description:**  
Predict weather based on pressure reading.

**Parameters:**  
None

**Returns:**

| Type | Description |
|------|-------------|
| str | Weather prediction |

**Return Values:**

| Range | Return Value |
|-------|--------------|
| < 1000 hPa | "Stormy" |
| 1000-1010 hPa | "Rainy" |
| 1010-1020 hPa | "Changing" |
| 1020-1030 hPa | "Fair" |
| > 1030 hPa | "Very Dry" |

**Example:**
```python
weather = pressure_sensor.get_weather_prediction()
print(weather)  # Output: "Fair"
```

---

## DHTSensor Class

### Class: `DHTSensor`

**Description:**  
Combined Temperature and Humidity Sensor. Simulates DHT11/DHT22 sensors that measure both temperature and humidity simultaneously. Commonly used in IoT projects with Raspberry Pi and Jetson Nano.

**Inheritance:**  
Inherits from `Sensor`

**Additional Attributes:**

| Attribute | Type | Description |
|-----------|------|-------------|
| `min_temp` | float | Minimum temperature (default: 18°C) |
| `max_temp` | float | Maximum temperature (default: 30°C) |
| `min_humidity` | float | Minimum humidity (default: 30%) |
| `max_humidity` | float | Maximum humidity (default: 80%) |

---

### Method: `__init__(location, group, sensor_name, min_temp=18, max_temp=30, min_humidity=30, max_humidity=80)`

**Description:**  
Initialize a DHT Sensor.

**Parameters:**

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `location` | str | Yes | - | Physical location of the sensor |
| `group` | str | Yes | - | Group/room where sensor is located |
| `sensor_name` | str | Yes | - | Unique identifier for the sensor |
| `min_temp` | float | No | 18 | Minimum temperature |
| `max_temp` | float | No | 30 | Maximum temperature |
| `min_humidity` | float | No | 30 | Minimum humidity |
| `max_humidity` | float | No | 80 | Maximum humidity |

**Returns:**  
None

**Example:**
```python
# Default ranges
dht1 = DHTSensor('home', 'bedroom', 'dht_001')

# Custom ranges
dht2 = DHTSensor('home', 'greenhouse', 'dht_002', 
                 min_temp=15, max_temp=35,
                 min_humidity=40, max_humidity=90)
```

---

### Method: `read_data()`

**Description:**  
Read both temperature and humidity data simultaneously.

**Parameters:**  
None

**Returns:**

| Type | Description |
|------|-------------|
| tuple | (temperature, humidity) as (float, float) |

**Example:**
```python
temp, humidity = dht_sensor.read_data()
print(f"Temperature: {temp}°C")
print(f"Humidity: {humidity}%")
# Output:
# Temperature: 23.45°C
# Humidity: 65.32%
```

---

### Method: `read_temperature()`

**Description:**  
Read only temperature data.

**Parameters:**  
None

**Returns:**

| Type | Description |
|------|-------------|
| float | Temperature in Celsius |

**Example:**
```python
temp = dht_sensor.read_temperature()
print(f"Temperature: {temp}°C")  # Output: "Temperature: 23.45°C"
```

---

### Method: `read_humidity()`

**Description:**  
Read only humidity data.

**Parameters:**  
None

**Returns:**

| Type | Description |
|------|-------------|
| float | Humidity percentage |

**Example:**
```python
humidity = dht_sensor.read_humidity()
print(f"Humidity: {humidity}%")  # Output: "Humidity: 65.32%"
```

---

### Method: `read_data_formatted()`

**Description:**  
Read data with formatted output combining both temperature and humidity.

**Parameters:**  
None

**Returns:**

| Type | Description |
|------|-------------|
| str | Formatted string with both readings |

**Example:**
```python
data = dht_sensor.read_data_formatted()
print(data)
# Output: "Temperature: 23.45°C | Humidity: 65.32%"
```

---

## Complete Usage Example

```python
"""
Complete example demonstrating all sensor classes and their methods
"""

from sensor import (
    TemperatureSensor,
    HumiditySensor,
    MotionSensor,
    LightSensor,
    PressureSensor,
    DHTSensor
)

# Create all sensor types
temp = TemperatureSensor('home', 'living_room', 'temp_001')
humid = HumiditySensor('home', 'bedroom', 'humid_001')
motion = MotionSensor('home', 'hallway', 'motion_001', sensitivity=0.7)
light = LightSensor('home', 'kitchen', 'light_001')
pressure = PressureSensor('home', 'balcony', 'pressure_001')
dht = DHTSensor('home', 'garage', 'dht_001')

# Temperature Sensor
print("=== Temperature Sensor ===")
print(f"Reading: {temp.read_data()}")
print(f"With unit: {temp.read_data_with_unit()}")
print(f"Info: {temp.get_info()}")

# Humidity Sensor
print("\n=== Humidity Sensor ===")
print(f"Reading: {humid.read_data()}")
print(f"With unit: {humid.read_data_with_unit()}")
print(f"Comfort: {humid.get_comfort_level()}")

# Motion Sensor
print("\n=== Motion Sensor ===")
print(f"Detected: {motion.read_data()}")
print(f"Status: {motion.read_data_with_status()}")
print(f"Count: {motion.get_detection_count()}")

# Light Sensor
print("\n=== Light Sensor ===")
print(f"Reading: {light.read_data()}")
print(f"With unit: {light.read_data_with_unit()}")
print(f"Brightness: {light.get_brightness_level()}")

# Pressure Sensor
print("\n=== Pressure Sensor ===")
print(f"Reading: {pressure.read_data()}")
print(f"With unit: {pressure.read_data_with_unit()}")
print(f"Weather: {pressure.get_weather_prediction()}")

# DHT Sensor
print("\n=== DHT Sensor ===")
temp_val, humid_val = dht.read_data()
print(f"Both: ({temp_val}, {humid_val})")
print(f"Temperature only: {dht.read_temperature()}")
print(f"Humidity only: {dht.read_humidity()}")
print(f"Formatted: {dht.read_data_formatted()}")
```

---

**In The Name of God**

*Complete Function Documentation - IoT Sensor System*  
*Author: Saeed Angiz | Course: IoT Programming with Python | Instructor: Aghaye Pilehvar*
