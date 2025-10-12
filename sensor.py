"""
In The Name of God

IoT Sensor System
Author: Saeed Angiz
Course: IoT Programming with Python
Instructor: Aghaye Pilehvar

This module contains all sensor classes for the IoT system.
Each sensor type is separated and organized for easy management.
"""

import numpy as np


# ============================================================================
# BASE SENSOR CLASS
# ============================================================================

class Sensor:
    """
    Base Sensor Class
    
    This is the foundation class for all sensors in the IoT system.
    It provides basic sensor functionality including location tracking,
    grouping, and data reading capabilities.
    
    Attributes:
        location (str): Physical location of the sensor (e.g., 'home', 'office')
        group (str): Group/room where sensor is located (e.g., 'living_room', 'bedroom')
        sensor_name (str): Unique identifier for the sensor
        sensor_type (str): Type of sensor (e.g., 'temperature', 'humidity', 'motion')
    """
    
    def __init__(self, location, group, sensor_type, sensor_name):
        """
        Initialize a new Sensor object.
        
        Parameters:
            location (str): Physical location of the sensor
            group (str): Group/room where sensor is located
            sensor_type (str): Type of sensor
            sensor_name (str): Unique identifier for the sensor
        """
        self.location = location
        self.group = group
        self.sensor_name = sensor_name
        self.sensor_type = sensor_type
    
    
    def read_data(self):
        """
        Read data from the sensor.
        
        This is a basic implementation that returns a default value.
        Specific sensor types should override this method.
        
        Returns:
            int: Default sensor reading value (25)
        """
        return 25
    
    
    def get_info(self):
        """
        Get complete information about the sensor.
        
        Returns:
            dict: Dictionary containing all sensor information
        """
        return {
            'sensor_name': self.sensor_name,
            'sensor_type': self.sensor_type,
            'location': self.location,
            'group': self.group
        }
    
    
    def __str__(self):
        """
        String representation of the sensor.
        
        Returns:
            str: Formatted string with sensor details
        """
        return f"Sensor: {self.sensor_name} | Type: {self.sensor_type} | Location: {self.location}/{self.group}"


# ============================================================================
# TEMPERATURE SENSOR
# ============================================================================

class TemperatureSensor(Sensor):
    """
    Temperature Sensor Class
    
    Specialized sensor for measuring temperature.
    Provides realistic temperature readings with configurable range.
    
    Attributes:
        min_temp (float): Minimum temperature value (default: 18°C)
        max_temp (float): Maximum temperature value (default: 30°C)
        unit (str): Temperature unit ('celsius' or 'fahrenheit')
    """
    
    def __init__(self, location, group, sensor_name, min_temp=18, max_temp=30, unit='celsius'):
        """
        Initialize a Temperature Sensor.
        
        Parameters:
            location (str): Physical location of the sensor
            group (str): Group/room where sensor is located
            sensor_name (str): Unique identifier for the sensor
            min_temp (float): Minimum temperature reading (default: 18)
            max_temp (float): Maximum temperature reading (default: 30)
            unit (str): Temperature unit (default: 'celsius')
        """
        super().__init__(location, group, 'temperature', sensor_name)
        self.min_temp = min_temp
        self.max_temp = max_temp
        self.unit = unit
    
    
    def read_data(self):
        """
        Read temperature data from the sensor.
        
        Generates a random temperature value within the configured range.
        
        Returns:
            float: Temperature reading in specified unit
        """
        temperature = np.random.uniform(self.min_temp, self.max_temp)
        return round(temperature, 2)
    
    
    def read_data_with_unit(self):
        """
        Read temperature data with unit label.
        
        Returns:
            str: Temperature reading with unit (e.g., "23.45°C")
        """
        temp = self.read_data()
        symbol = '°C' if self.unit == 'celsius' else '°F'
        return f"{temp}{symbol}"
    
    
    def convert_to_fahrenheit(self, celsius):
        """
        Convert Celsius to Fahrenheit.
        
        Parameters:
            celsius (float): Temperature in Celsius
            
        Returns:
            float: Temperature in Fahrenheit
        """
        return round((celsius * 9/5) + 32, 2)
    
    
    def convert_to_celsius(self, fahrenheit):
        """
        Convert Fahrenheit to Celsius.
        
        Parameters:
            fahrenheit (float): Temperature in Fahrenheit
            
        Returns:
            float: Temperature in Celsius
        """
        return round((fahrenheit - 32) * 5/9, 2)


# ============================================================================
# HUMIDITY SENSOR
# ============================================================================

class HumiditySensor(Sensor):
    """
    Humidity Sensor Class
    
    Specialized sensor for measuring humidity levels.
    Provides humidity readings as percentage.
    
    Attributes:
        min_humidity (float): Minimum humidity percentage (default: 30%)
        max_humidity (float): Maximum humidity percentage (default: 80%)
    """
    
    def __init__(self, location, group, sensor_name, min_humidity=30, max_humidity=80):
        """
        Initialize a Humidity Sensor.
        
        Parameters:
            location (str): Physical location of the sensor
            group (str): Group/room where sensor is located
            sensor_name (str): Unique identifier for the sensor
            min_humidity (float): Minimum humidity reading (default: 30)
            max_humidity (float): Maximum humidity reading (default: 80)
        """
        super().__init__(location, group, 'humidity', sensor_name)
        self.min_humidity = min_humidity
        self.max_humidity = max_humidity
    
    
    def read_data(self):
        """
        Read humidity data from the sensor.
        
        Generates a random humidity value within the configured range.
        
        Returns:
            float: Humidity reading as percentage
        """
        humidity = np.random.uniform(self.min_humidity, self.max_humidity)
        return round(humidity, 2)
    
    
    def read_data_with_unit(self):
        """
        Read humidity data with percentage symbol.
        
        Returns:
            str: Humidity reading with % symbol (e.g., "65.32%")
        """
        humidity = self.read_data()
        return f"{humidity}%"
    
    
    def get_comfort_level(self):
        """
        Determine comfort level based on humidity reading.
        
        Returns:
            str: Comfort level description
                - "Too Dry" (< 30%)
                - "Comfortable" (30-60%)
                - "Humid" (60-70%)
                - "Too Humid" (> 70%)
        """
        humidity = self.read_data()
        
        if humidity < 30:
            return "Too Dry"
        elif humidity <= 60:
            return "Comfortable"
        elif humidity <= 70:
            return "Humid"
        else:
            return "Too Humid"


# ============================================================================
# MOTION SENSOR
# ============================================================================

class MotionSensor(Sensor):
    """
    Motion Sensor Class
    
    Specialized sensor for detecting motion/movement.
    Returns boolean values indicating motion detection.
    
    Attributes:
        sensitivity (float): Detection sensitivity (0.0 to 1.0)
        detection_count (int): Number of times motion was detected
    """
    
    def __init__(self, location, group, sensor_name, sensitivity=0.5):
        """
        Initialize a Motion Sensor.
        
        Parameters:
            location (str): Physical location of the sensor
            group (str): Group/room where sensor is located
            sensor_name (str): Unique identifier for the sensor
            sensitivity (float): Detection sensitivity 0.0-1.0 (default: 0.5)
        """
        super().__init__(location, group, 'motion', sensor_name)
        self.sensitivity = sensitivity
        self.detection_count = 0
    
    
    def read_data(self):
        """
        Read motion detection data.
        
        Simulates motion detection based on sensitivity level.
        Higher sensitivity = more likely to detect motion.
        
        Returns:
            bool: True if motion detected, False otherwise
        """
        motion_detected = np.random.random() < self.sensitivity
        
        if motion_detected:
            self.detection_count += 1
        
        return motion_detected
    
    
    def read_data_with_status(self):
        """
        Read motion data with status message.
        
        Returns:
            str: Motion status message
        """
        if self.read_data():
            return "Motion Detected!"
        else:
            return "No Motion"
    
    
    def get_detection_count(self):
        """
        Get total number of motion detections.
        
        Returns:
            int: Total detection count
        """
        return self.detection_count
    
    
    def reset_detection_count(self):
        """
        Reset the motion detection counter to zero.
        """
        self.detection_count = 0
        print(f"Detection count reset for {self.sensor_name}")


# ============================================================================
# LIGHT SENSOR
# ============================================================================

class LightSensor(Sensor):
    """
    Light Sensor Class
    
    Specialized sensor for measuring light intensity.
    Measures in Lux (light intensity unit).
    
    Attributes:
        min_lux (float): Minimum light intensity (default: 0 lux)
        max_lux (float): Maximum light intensity (default: 1000 lux)
    """
    
    def __init__(self, location, group, sensor_name, min_lux=0, max_lux=1000):
        """
        Initialize a Light Sensor.
        
        Parameters:
            location (str): Physical location of the sensor
            group (str): Group/room where sensor is located
            sensor_name (str): Unique identifier for the sensor
            min_lux (float): Minimum light reading (default: 0)
            max_lux (float): Maximum light reading (default: 1000)
        """
        super().__init__(location, group, 'light', sensor_name)
        self.min_lux = min_lux
        self.max_lux = max_lux
    
    
    def read_data(self):
        """
        Read light intensity data.
        
        Generates a random light intensity value within the configured range.
        
        Returns:
            float: Light intensity in Lux
        """
        light_intensity = np.random.uniform(self.min_lux, self.max_lux)
        return round(light_intensity, 2)
    
    
    def read_data_with_unit(self):
        """
        Read light data with unit label.
        
        Returns:
            str: Light intensity with unit (e.g., "450.23 lux")
        """
        lux = self.read_data()
        return f"{lux} lux"
    
    
    def get_brightness_level(self):
        """
        Determine brightness level based on light reading.
        
        Returns:
            str: Brightness level description
                - "Dark" (< 50 lux)
                - "Dim" (50-200 lux)
                - "Normal" (200-500 lux)
                - "Bright" (500-800 lux)
                - "Very Bright" (> 800 lux)
        """
        lux = self.read_data()
        
        if lux < 50:
            return "Dark"
        elif lux < 200:
            return "Dim"
        elif lux < 500:
            return "Normal"
        elif lux < 800:
            return "Bright"
        else:
            return "Very Bright"


# ============================================================================
# PRESSURE SENSOR
# ============================================================================

class PressureSensor(Sensor):
    """
    Pressure Sensor Class
    
    Specialized sensor for measuring atmospheric pressure.
    Measures in hPa (hectopascals).
    
    Attributes:
        min_pressure (float): Minimum pressure (default: 980 hPa)
        max_pressure (float): Maximum pressure (default: 1050 hPa)
    """
    
    def __init__(self, location, group, sensor_name, min_pressure=980, max_pressure=1050):
        """
        Initialize a Pressure Sensor.
        
        Parameters:
            location (str): Physical location of the sensor
            group (str): Group/room where sensor is located
            sensor_name (str): Unique identifier for the sensor
            min_pressure (float): Minimum pressure reading (default: 980)
            max_pressure (float): Maximum pressure reading (default: 1050)
        """
        super().__init__(location, group, 'pressure', sensor_name)
        self.min_pressure = min_pressure
        self.max_pressure = max_pressure
    
    
    def read_data(self):
        """
        Read atmospheric pressure data.
        
        Generates a random pressure value within the configured range.
        
        Returns:
            float: Atmospheric pressure in hPa
        """
        pressure = np.random.uniform(self.min_pressure, self.max_pressure)
        return round(pressure, 2)
    
    
    def read_data_with_unit(self):
        """
        Read pressure data with unit label.
        
        Returns:
            str: Pressure reading with unit (e.g., "1013.25 hPa")
        """
        pressure = self.read_data()
        return f"{pressure} hPa"
    
    
    def get_weather_prediction(self):
        """
        Predict weather based on pressure reading.
        
        Returns:
            str: Weather prediction
                - "Stormy" (< 1000 hPa)
                - "Rainy" (1000-1010 hPa)
                - "Changing" (1010-1020 hPa)
                - "Fair" (1020-1030 hPa)
                - "Very Dry" (> 1030 hPa)
        """
        pressure = self.read_data()
        
        if pressure < 1000:
            return "Stormy"
        elif pressure < 1010:
            return "Rainy"
        elif pressure < 1020:
            return "Changing"
        elif pressure < 1030:
            return "Fair"
        else:
            return "Very Dry"


# ============================================================================
# COMBINED DHT SENSOR (Temperature + Humidity)
# ============================================================================

class DHTSensor(Sensor):
    """
    DHT Sensor Class (Combined Temperature and Humidity)
    
    Simulates DHT11/DHT22 sensors that measure both temperature and humidity.
    This is commonly used in IoT projects with Raspberry Pi.
    
    Attributes:
        min_temp (float): Minimum temperature (default: 18°C)
        max_temp (float): Maximum temperature (default: 30°C)
        min_humidity (float): Minimum humidity (default: 30%)
        max_humidity (float): Maximum humidity (default: 80%)
    """
    
    def __init__(self, location, group, sensor_name, min_temp=18, max_temp=30, 
                 min_humidity=30, max_humidity=80):
        """
        Initialize a DHT Sensor.
        
        Parameters:
            location (str): Physical location of the sensor
            group (str): Group/room where sensor is located
            sensor_name (str): Unique identifier for the sensor
            min_temp (float): Minimum temperature (default: 18)
            max_temp (float): Maximum temperature (default: 30)
            min_humidity (float): Minimum humidity (default: 30)
            max_humidity (float): Maximum humidity (default: 80)
        """
        super().__init__(location, group, 'dht', sensor_name)
        self.min_temp = min_temp
        self.max_temp = max_temp
        self.min_humidity = min_humidity
        self.max_humidity = max_humidity
    
    
    def read_data(self):
        """
        Read both temperature and humidity data.
        
        Returns:
            tuple: (temperature, humidity) as (float, float)
        """
        temperature = np.random.uniform(self.min_temp, self.max_temp)
        humidity = np.random.uniform(self.min_humidity, self.max_humidity)
        
        return round(temperature, 2), round(humidity, 2)
    
    
    def read_temperature(self):
        """
        Read only temperature data.
        
        Returns:
            float: Temperature in Celsius
        """
        temp, _ = self.read_data()
        return temp
    
    
    def read_humidity(self):
        """
        Read only humidity data.
        
        Returns:
            float: Humidity percentage
        """
        _, humidity = self.read_data()
        return humidity
    
    
    def read_data_formatted(self):
        """
        Read data with formatted output.
        
        Returns:
            str: Formatted string with both readings
        """
        temp, humidity = self.read_data()
        return f"Temperature: {temp}°C | Humidity: {humidity}%"


# ============================================================================
# EXAMPLE USAGE
# ============================================================================

if __name__ == "__main__":
    print("=" * 70)
    print("IoT SENSOR SYSTEM - DEMONSTRATION")
    print("=" * 70)
    
    # Create Temperature Sensor
    print("\n1. TEMPERATURE SENSOR")
    print("-" * 70)
    temp_sensor = TemperatureSensor('home', 'living_room', 'temp_sensor_001')
    print(temp_sensor)
    print(f"Reading: {temp_sensor.read_data_with_unit()}")
    print(f"Reading: {temp_sensor.read_data_with_unit()}")
    print(f"Reading: {temp_sensor.read_data_with_unit()}")
    
    # Create Humidity Sensor
    print("\n2. HUMIDITY SENSOR")
    print("-" * 70)
    humidity_sensor = HumiditySensor('home', 'bedroom', 'humidity_sensor_001')
    print(humidity_sensor)
    print(f"Reading: {humidity_sensor.read_data_with_unit()}")
    print(f"Comfort Level: {humidity_sensor.get_comfort_level()}")
    
    # Create Motion Sensor
    print("\n3. MOTION SENSOR")
    print("-" * 70)
    motion_sensor = MotionSensor('home', 'hallway', 'motion_sensor_001', sensitivity=0.7)
    print(motion_sensor)
    for i in range(5):
        print(f"Check {i+1}: {motion_sensor.read_data_with_status()}")
    print(f"Total Detections: {motion_sensor.get_detection_count()}")
    
    # Create Light Sensor
    print("\n4. LIGHT SENSOR")
    print("-" * 70)
    light_sensor = LightSensor('home', 'kitchen', 'light_sensor_001')
    print(light_sensor)
    print(f"Reading: {light_sensor.read_data_with_unit()}")
    print(f"Brightness: {light_sensor.get_brightness_level()}")
    
    # Create Pressure Sensor
    print("\n5. PRESSURE SENSOR")
    print("-" * 70)
    pressure_sensor = PressureSensor('home', 'balcony', 'pressure_sensor_001')
    print(pressure_sensor)
    print(f"Reading: {pressure_sensor.read_data_with_unit()}")
    print(f"Weather: {pressure_sensor.get_weather_prediction()}")
    
    # Create DHT Sensor
    print("\n6. DHT SENSOR (Temperature + Humidity)")
    print("-" * 70)
    dht_sensor = DHTSensor('home', 'garage', 'dht_sensor_001')
    print(dht_sensor)
    print(f"Reading: {dht_sensor.read_data_formatted()}")
    print(f"Temperature Only: {dht_sensor.read_temperature()}°C")
    print(f"Humidity Only: {dht_sensor.read_humidity()}%")
    
    print("\n" + "=" * 70)
    print("DEMONSTRATION COMPLETE")
    print("=" * 70)
