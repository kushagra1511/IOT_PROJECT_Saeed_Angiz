#!/usr/bin/env python3
"""
In The Name of God

Simple Example - IoT Sensor System
Author: Saeed Angiz
Course: IoT Programming with Python
Instructor: Aghaye Pilehvar

This is a simple example to get you started with the sensor system.
"""

from sensor import (
    TemperatureSensor,
    HumiditySensor,
    MotionSensor,
    LightSensor,
    PressureSensor,
    DHTSensor
)


def main():
    """Main function demonstrating basic sensor usage"""
    
    print("=" * 70)
    print("SIMPLE SENSOR EXAMPLE")
    print("=" * 70)
    
    # Example 1: Temperature Sensor
    print("\n1. Temperature Sensor Example")
    print("-" * 70)
    temp_sensor = TemperatureSensor('home', 'living_room', 'temp_001')
    print(f"Sensor: {temp_sensor}")
    print(f"Reading: {temp_sensor.read_data_with_unit()}")
    
    # Example 2: Humidity Sensor
    print("\n2. Humidity Sensor Example")
    print("-" * 70)
    humid_sensor = HumiditySensor('home', 'bedroom', 'humid_001')
    print(f"Sensor: {humid_sensor}")
    print(f"Reading: {humid_sensor.read_data_with_unit()}")
    print(f"Comfort Level: {humid_sensor.get_comfort_level()}")
    
    # Example 3: Motion Sensor
    print("\n3. Motion Sensor Example")
    print("-" * 70)
    motion_sensor = MotionSensor('home', 'hallway', 'motion_001', sensitivity=0.6)
    print(f"Sensor: {motion_sensor}")
    print("Checking for motion 5 times...")
    for i in range(5):
        status = motion_sensor.read_data_with_status()
        print(f"  Check {i+1}: {status}")
    print(f"Total Detections: {motion_sensor.get_detection_count()}")
    
    # Example 4: Light Sensor
    print("\n4. Light Sensor Example")
    print("-" * 70)
    light_sensor = LightSensor('home', 'kitchen', 'light_001')
    print(f"Sensor: {light_sensor}")
    print(f"Reading: {light_sensor.read_data_with_unit()}")
    print(f"Brightness Level: {light_sensor.get_brightness_level()}")
    
    # Example 5: Pressure Sensor
    print("\n5. Pressure Sensor Example")
    print("-" * 70)
    pressure_sensor = PressureSensor('home', 'balcony', 'pressure_001')
    print(f"Sensor: {pressure_sensor}")
    print(f"Reading: {pressure_sensor.read_data_with_unit()}")
    print(f"Weather Prediction: {pressure_sensor.get_weather_prediction()}")
    
    # Example 6: DHT Sensor (Combined)
    print("\n6. DHT Sensor Example (Temperature + Humidity)")
    print("-" * 70)
    dht_sensor = DHTSensor('home', 'garage', 'dht_001')
    print(f"Sensor: {dht_sensor}")
    print(f"Combined Reading: {dht_sensor.read_data_formatted()}")
    print(f"Temperature Only: {dht_sensor.read_temperature()}°C")
    print(f"Humidity Only: {dht_sensor.read_humidity()}%")
    
    # Example 7: Creating Multiple Sensors
    print("\n7. Multiple Sensors Example")
    print("-" * 70)
    sensors = {
        'temp': TemperatureSensor('home', 'office', 'temp_office'),
        'humid': HumiditySensor('home', 'office', 'humid_office'),
        'light': LightSensor('home', 'office', 'light_office')
    }
    
    print("Office Sensor Readings:")
    for name, sensor in sensors.items():
        print(f"  {name}: {sensor.read_data()}")
    
    # Example 8: Custom Temperature Range
    print("\n8. Custom Range Example")
    print("-" * 70)
    freezer = TemperatureSensor('home', 'kitchen', 'freezer_temp', 
                                min_temp=-20, max_temp=-10)
    print(f"Freezer Temperature: {freezer.read_data_with_unit()}")
    
    outdoor = TemperatureSensor('home', 'outdoor', 'outdoor_temp',
                                min_temp=-5, max_temp=40)
    print(f"Outdoor Temperature: {outdoor.read_data_with_unit()}")
    
    print("\n" + "=" * 70)
    print("EXAMPLE COMPLETE!")
    print("=" * 70)
    print("\nNext Steps:")
    print("1. Read SENSOR_README.md for complete documentation")
    print("2. Check SENSOR_QUICK_REFERENCE.md for quick reference")
    print("3. Modify this script to experiment with sensors")
    print("4. Create your own IoT projects!")
    print("\nIn The Name of God")


if __name__ == "__main__":
    main()
