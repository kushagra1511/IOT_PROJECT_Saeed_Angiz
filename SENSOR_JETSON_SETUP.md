# IoT Sensor System - Jetson Nano Setup Guide

**In The Name of God**

---

## Table of Contents

1. [Introduction](#introduction)
2. [Hardware Requirements](#hardware-requirements)
3. [Software Requirements](#software-requirements)
4. [Jetson Nano Setup](#jetson-nano-setup)
5. [Installing Dependencies](#installing-dependencies)
6. [Deploying Sensor System](#deploying-sensor-system)
7. [Connecting Real Sensors](#connecting-real-sensors)
8. [Testing and Verification](#testing-and-verification)
9. [Troubleshooting](#troubleshooting)
10. [Advanced Configuration](#advanced-configuration)

---

## Introduction

This guide will help you deploy the IoT Sensor System on NVIDIA Jetson Nano, a powerful edge computing platform perfect for IoT applications. The Jetson Nano provides GPIO pins for connecting real sensors and enough computing power for data processing and machine learning.

### Why Jetson Nano?

- **Powerful Processing:** 128-core NVIDIA GPU
- **GPIO Support:** Compatible with Raspberry Pi sensors
- **AI Capabilities:** Run machine learning models on sensor data
- **Linux-Based:** Full Ubuntu environment
- **Low Power:** Suitable for always-on IoT applications

---

## Hardware Requirements

### Essential Components

1. **NVIDIA Jetson Nano Developer Kit**
   - 4GB RAM version recommended
   - Includes carrier board with GPIO pins

2. **Power Supply**
   - 5V 4A barrel jack power adapter (recommended)
   - Or 5V 2.5A micro-USB (for basic operation)

3. **MicroSD Card**
   - 32GB minimum (64GB or 128GB recommended)
   - Class 10 or UHS-1 speed rating

4. **Cooling**
   - Heatsink (usually included)
   - Fan (5V, recommended for continuous operation)

### Optional Components

5. **Display and Input**
   - HDMI monitor
   - USB keyboard and mouse
   - Or use SSH for headless operation

6. **Network**
   - Ethernet cable (recommended)
   - Or WiFi adapter (USB)

### Sensors (for real hardware integration)

7. **Temperature & Humidity**
   - DHT11 or DHT22 sensor
   - Cost: $2-5

8. **Motion Detection**
   - PIR motion sensor (HC-SR501)
   - Cost: $1-3

9. **Light Sensor**
   - BH1750 light sensor (I2C)
   - Or photoresistor with resistor
   - Cost: $1-5

10. **Pressure Sensor**
    - BMP180 or BMP280 (I2C)
    - Cost: $2-8

### Wiring Components

11. **Breadboard and Jumper Wires**
    - 400-point breadboard
    - Male-to-female jumper wires
    - Cost: $5-10

---

## Software Requirements

### Operating System

- **JetPack SDK** (includes Ubuntu 18.04/20.04)
- Download from: https://developer.nvidia.com/jetpack

### Python Environment

- Python 3.6 or higher (pre-installed)
- pip package manager

### Required Libraries

- NumPy (for sensor simulation)
- Jetson.GPIO (for hardware access)
- Adafruit libraries (for specific sensors)

---

## Jetson Nano Setup

### Step 1: Flash JetPack to MicroSD Card

**On Windows:**

1. Download and install **Etcher** (https://www.balena.io/etcher/)
2. Download **JetPack image** from NVIDIA website
3. Insert microSD card into computer
4. Open Etcher:
   - Select JetPack image file
   - Select microSD card
   - Click "Flash"
5. Wait for flashing to complete (10-20 minutes)

**On Linux/Mac:**

```bash
# Download JetPack image
wget https://developer.nvidia.com/jetson-nano-sd-card-image

# Unzip image
unzip jetson-nano-sd-card-image.zip

# Flash to SD card (replace /dev/sdX with your SD card)
sudo dd if=sd-blob.img of=/dev/sdX bs=4M status=progress
sync
```

### Step 2: First Boot

1. Insert microSD card into Jetson Nano
2. Connect HDMI monitor, keyboard, mouse
3. Connect Ethernet cable (recommended)
4. Connect power supply
5. Wait for boot (first boot takes 2-3 minutes)

### Step 3: Initial Configuration

Follow on-screen setup wizard:

1. **Language:** Select your language
2. **Keyboard:** Select keyboard layout
3. **Location:** Select timezone
4. **User Account:**
   - Username: `jetson` (or your choice)
   - Password: Create strong password
5. **Network:** Configure if using WiFi
6. **Updates:** Let system update (recommended)

### Step 4: System Update

```bash
# Update package lists
sudo apt update

# Upgrade installed packages
sudo apt upgrade -y

# Reboot
sudo reboot
```

---

## Installing Dependencies

### Step 1: Install Python and pip

```bash
# Check Python version (should be 3.6+)
python3 --version

# Install pip if not present
sudo apt install python3-pip -y

# Verify pip installation
pip3 --version
```

### Step 2: Install NumPy

```bash
# Install NumPy
pip3 install numpy

# Verify installation
python3 -c "import numpy; print(numpy.__version__)"
```

### Step 3: Install Jetson.GPIO

```bash
# Install Jetson GPIO library
sudo pip3 install Jetson.GPIO

# Add user to gpio group
sudo groupadd -f -r gpio
sudo usermod -a -G gpio $USER

# Reboot for changes to take effect
sudo reboot
```

### Step 4: Install Sensor Libraries (Optional)

For real hardware sensors:

```bash
# Install Adafruit libraries
sudo pip3 install adafruit-circuitpython-dht
sudo pip3 install adafruit-circuitpython-bmp280
sudo pip3 install adafruit-circuitpython-bh1750

# Install additional dependencies
sudo apt install libgpiod2 -y
```

---

## Deploying Sensor System

### Step 1: Transfer sensor.py to Jetson Nano

**Method 1: Using SCP (from your computer)**

```bash
# Copy file to Jetson Nano
scp sensor.py jetson@<jetson-ip-address>:~/

# Example:
scp sensor.py jetson@192.168.1.100:~/
```

**Method 2: Using USB Drive**

1. Copy `sensor.py` to USB drive
2. Insert USB drive into Jetson Nano
3. Copy file:
```bash
cp /media/jetson/USB_DRIVE/sensor.py ~/
```

**Method 3: Using Git**

```bash
# Clone repository (if hosted on GitHub)
git clone https://github.com/yourusername/iot-sensor-system.git
cd iot-sensor-system
```

**Method 4: Direct Download**

```bash
# Download directly (if hosted online)
wget https://your-url.com/sensor.py
```

### Step 2: Verify Installation

```bash
# Navigate to directory
cd ~

# Check file exists
ls -l sensor.py

# Test import
python3 -c "from sensor import TemperatureSensor; print('Success!')"
```

### Step 3: Create Project Directory

```bash
# Create project directory
mkdir -p ~/iot_project
cd ~/iot_project

# Copy sensor.py
cp ~/sensor.py .

# Create test script
nano test_sensors.py
```

### Step 4: Create Test Script

```python
# test_sensors.py
"""
Test script for IoT Sensor System on Jetson Nano
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
    print("=" * 70)
    print("IoT SENSOR SYSTEM - JETSON NANO TEST")
    print("=" * 70)
    
    # Create sensors
    temp = TemperatureSensor('jetson', 'test_room', 'temp_001')
    humid = HumiditySensor('jetson', 'test_room', 'humid_001')
    motion = MotionSensor('jetson', 'test_room', 'motion_001')
    light = LightSensor('jetson', 'test_room', 'light_001')
    pressure = PressureSensor('jetson', 'test_room', 'pressure_001')
    dht = DHTSensor('jetson', 'test_room', 'dht_001')
    
    # Test each sensor
    print("\n1. Temperature Sensor")
    print(f"   Reading: {temp.read_data_with_unit()}")
    
    print("\n2. Humidity Sensor")
    print(f"   Reading: {humid.read_data_with_unit()}")
    print(f"   Comfort: {humid.get_comfort_level()}")
    
    print("\n3. Motion Sensor")
    print(f"   Status: {motion.read_data_with_status()}")
    
    print("\n4. Light Sensor")
    print(f"   Reading: {light.read_data_with_unit()}")
    print(f"   Level: {light.get_brightness_level()}")
    
    print("\n5. Pressure Sensor")
    print(f"   Reading: {pressure.read_data_with_unit()}")
    print(f"   Weather: {pressure.get_weather_prediction()}")
    
    print("\n6. DHT Sensor")
    print(f"   Reading: {dht.read_data_formatted()}")
    
    print("\n" + "=" * 70)
    print("TEST COMPLETE - All sensors working!")
    print("=" * 70)

if __name__ == "__main__":
    main()
```

### Step 5: Run Test

```bash
# Make script executable
chmod +x test_sensors.py

# Run test
python3 test_sensors.py
```

---

## Connecting Real Sensors

### GPIO Pin Reference

Jetson Nano uses 40-pin GPIO header (compatible with Raspberry Pi):

```
Pin Layout (Physical Pin Numbers):
1  [3.3V]     2  [5V]
3  [GPIO2]    4  [5V]
5  [GPIO3]    6  [GND]
7  [GPIO4]    8  [GPIO14]
9  [GND]      10 [GPIO15]
11 [GPIO17]   12 [GPIO18]
13 [GPIO27]   14 [GND]
15 [GPIO22]   16 [GPIO23]
17 [3.3V]     18 [GPIO24]
19 [GPIO10]   20 [GND]
... (continues to pin 40)
```

### DHT11/DHT22 Temperature & Humidity Sensor

**Wiring:**
```
DHT Sensor    Jetson Nano
VCC    --->   Pin 1 (3.3V)
DATA   --->   Pin 7 (GPIO4)
GND    --->   Pin 6 (GND)
```

**Code Example:**
```python
import Jetson.GPIO as GPIO
import adafruit_dht
import board

# Setup
dht_sensor = adafruit_dht.DHT22(board.D4)  # GPIO4

try:
    temperature = dht_sensor.temperature
    humidity = dht_sensor.humidity
    print(f"Temp: {temperature}°C, Humidity: {humidity}%")
except RuntimeError as e:
    print(f"Error: {e}")
finally:
    dht_sensor.exit()
```

### PIR Motion Sensor (HC-SR501)

**Wiring:**
```
PIR Sensor    Jetson Nano
VCC    --->   Pin 2 (5V)
OUT    --->   Pin 11 (GPIO17)
GND    --->   Pin 9 (GND)
```

**Code Example:**
```python
import Jetson.GPIO as GPIO
import time

# Setup
GPIO.setmode(GPIO.BOARD)
PIR_PIN = 11

GPIO.setup(PIR_PIN, GPIO.IN)

try:
    while True:
        if GPIO.input(PIR_PIN):
            print("Motion Detected!")
        else:
            print("No Motion")
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
```

### BH1750 Light Sensor (I2C)

**Wiring:**
```
BH1750        Jetson Nano
VCC    --->   Pin 1 (3.3V)
GND    --->   Pin 6 (GND)
SCL    --->   Pin 5 (I2C SCL)
SDA    --->   Pin 3 (I2C SDA)
```

**Enable I2C:**
```bash
# Install i2c-tools
sudo apt install i2c-tools -y

# Check I2C devices
sudo i2cdetect -y -r 1
```

**Code Example:**
```python
import board
import adafruit_bh1750

# Setup
i2c = board.I2C()
sensor = adafruit_bh1750.BH1750(i2c)

# Read light level
lux = sensor.lux
print(f"Light: {lux} lux")
```

### BMP280 Pressure Sensor (I2C)

**Wiring:**
```
BMP280        Jetson Nano
VCC    --->   Pin 1 (3.3V)
GND    --->   Pin 6 (GND)
SCL    --->   Pin 5 (I2C SCL)
SDA    --->   Pin 3 (I2C SDA)
```

**Code Example:**
```python
import board
import adafruit_bmp280

# Setup
i2c = board.I2C()
sensor = adafruit_bmp280.Adafruit_BMP280_I2C(i2c)

# Read pressure
pressure = sensor.pressure
temperature = sensor.temperature
print(f"Pressure: {pressure} hPa, Temp: {temperature}°C")
```

---

## Testing and Verification

### System Health Check

```bash
# Check CPU temperature
cat /sys/devices/virtual/thermal/thermal_zone*/temp

# Check memory usage
free -h

# Check disk space
df -h

# Check running processes
top
```

### GPIO Test

```bash
# Test GPIO access
sudo python3 -c "import Jetson.GPIO as GPIO; print('GPIO OK')"
```

### Sensor Test Script

Create `verify_sensors.py`:

```python
#!/usr/bin/env python3
"""
Comprehensive sensor verification script
"""

import sys

def test_imports():
    """Test if all required modules can be imported"""
    print("Testing imports...")
    
    try:
        import numpy
        print("✓ NumPy imported successfully")
    except ImportError:
        print("✗ NumPy import failed")
        return False
    
    try:
        from sensor import TemperatureSensor
        print("✓ Sensor module imported successfully")
    except ImportError:
        print("✗ Sensor module import failed")
        return False
    
    return True

def test_sensor_creation():
    """Test sensor object creation"""
    print("\nTesting sensor creation...")
    
    try:
        from sensor import TemperatureSensor
        temp = TemperatureSensor('jetson', 'test', 'temp_test')
        print("✓ Sensor created successfully")
        return True
    except Exception as e:
        print(f"✗ Sensor creation failed: {e}")
        return False

def test_sensor_reading():
    """Test sensor data reading"""
    print("\nTesting sensor reading...")
    
    try:
        from sensor import TemperatureSensor
        temp = TemperatureSensor('jetson', 'test', 'temp_test')
        data = temp.read_data()
        print(f"✓ Sensor reading successful: {data}°C")
        return True
    except Exception as e:
        print(f"✗ Sensor reading failed: {e}")
        return False

def main():
    print("=" * 60)
    print("JETSON NANO SENSOR SYSTEM VERIFICATION")
    print("=" * 60)
    
    tests = [
        test_imports,
        test_sensor_creation,
        test_sensor_reading
    ]
    
    results = []
    for test in tests:
        results.append(test())
    
    print("\n" + "=" * 60)
    if all(results):
        print("✓ ALL TESTS PASSED")
        print("=" * 60)
        return 0
    else:
        print("✗ SOME TESTS FAILED")
        print("=" * 60)
        return 1

if __name__ == "__main__":
    sys.exit(main())
```

Run verification:
```bash
python3 verify_sensors.py
```

---

## Troubleshooting

### Issue 1: Permission Denied (GPIO)

**Problem:** `RuntimeError: Permission denied`

**Solution:**
```bash
# Add user to gpio group
sudo groupadd -f -r gpio
sudo usermod -a -G gpio $USER

# Reboot
sudo reboot
```

### Issue 2: I2C Not Working

**Problem:** I2C sensors not detected

**Solution:**
```bash
# Install i2c-tools
sudo apt install i2c-tools -y

# Check I2C bus
sudo i2cdetect -y -r 1

# If no devices shown, check wiring
```

### Issue 3: DHT Sensor Timeout

**Problem:** DHT sensor returns timeout errors

**Solution:**
- Check wiring connections
- Add 10kΩ pull-up resistor between DATA and VCC
- Try different GPIO pin
- Increase read delay in code

### Issue 4: High CPU Temperature

**Problem:** Jetson Nano overheating

**Solution:**
```bash
# Install fan control
sudo apt install jetson-stats -y

# Monitor temperature
sudo jtop

# Enable fan (if connected to Pin 1)
sudo sh -c 'echo 255 > /sys/devices/pwm-fan/target_pwm'
```

### Issue 5: NumPy Import Error

**Problem:** `ImportError: No module named 'numpy'`

**Solution:**
```bash
# Reinstall NumPy
pip3 uninstall numpy
pip3 install numpy

# Or use system package
sudo apt install python3-numpy
```

---

## Advanced Configuration

### Auto-Start Sensor System on Boot

Create systemd service:

```bash
# Create service file
sudo nano /etc/systemd/system/iot-sensors.service
```

Add content:
```ini
[Unit]
Description=IoT Sensor System
After=network.target

[Service]
Type=simple
User=jetson
WorkingDirectory=/home/jetson/iot_project
ExecStart=/usr/bin/python3 /home/jetson/iot_project/main.py
Restart=always

[Install]
WantedBy=multi-user.target
```

Enable service:
```bash
# Reload systemd
sudo systemctl daemon-reload

# Enable service
sudo systemctl enable iot-sensors.service

# Start service
sudo systemctl start iot-sensors.service

# Check status
sudo systemctl status iot-sensors.service
```

### Remote Access via SSH

```bash
# Enable SSH (usually enabled by default)
sudo systemctl enable ssh
sudo systemctl start ssh

# Find IP address
hostname -I

# From another computer:
ssh jetson@<jetson-ip-address>
```

### Data Logging to File

Create logging script:

```python
import datetime
from sensor import TemperatureSensor, HumiditySensor

def log_data():
    temp = TemperatureSensor('jetson', 'room', 'temp_001')
    humid = HumiditySensor('jetson', 'room', 'humid_001')
    
    timestamp = datetime.datetime.now()
    temp_data = temp.read_data()
    humid_data = humid.read_data()
    
    with open('sensor_log.csv', 'a') as f:
        f.write(f"{timestamp},{temp_data},{humid_data}\n")

if __name__ == "__main__":
    log_data()
```

Add to crontab for periodic logging:
```bash
# Edit crontab
crontab -e

# Add line to log every 5 minutes
*/5 * * * * /usr/bin/python3 /home/jetson/iot_project/log_data.py
```

---

## Performance Optimization

### Reduce Power Consumption

```bash
# Set power mode to 5W (lower performance, lower power)
sudo nvpmodel -m 1

# Set to 10W (default)
sudo nvpmodel -m 0
```

### Monitor System Resources

```bash
# Install jetson-stats
sudo pip3 install jetson-stats

# Run monitoring tool
sudo jtop
```

---

## Next Steps

1. **Integrate Real Sensors:** Connect physical sensors to GPIO pins
2. **Add Data Visualization:** Use matplotlib or web dashboard
3. **Implement MQTT:** Send data to cloud services
4. **Add Machine Learning:** Use TensorFlow for predictions
5. **Create Web Interface:** Build Flask/Django dashboard

---

**In The Name of God**

*Jetson Nano Setup Guide - IoT Sensor System*  
*Author: Saeed Angiz | Course: IoT Programming with Python | Instructor: Aghaye Pilehvar*
