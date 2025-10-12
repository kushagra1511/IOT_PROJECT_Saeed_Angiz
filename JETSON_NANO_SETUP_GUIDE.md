# Jetson Nano Super Setup Guide for IoT Security System

## Complete Step-by-Step Installation and Configuration Guide

---

## Table of Contents
1. [Hardware Requirements](#hardware-requirements)
2. [Initial Jetson Nano Super Setup](#initial-jetson-nano-super-setup)
3. [Operating System Installation](#operating-system-installation)
4. [System Configuration](#system-configuration)
5. [Python Environment Setup](#python-environment-setup)
6. [Camera Setup and Configuration](#camera-setup-and-configuration)
7. [AI Model Installation](#ai-model-installation)
8. [Security System Installation](#security-system-installation)
9. [Testing the System](#testing-the-system)
10. [Running the Security System](#running-the-security-system)
11. [Troubleshooting](#troubleshooting)
12. [Maintenance and Updates](#maintenance-and-updates)

---

## Hardware Requirements

### Essential Components:
1. **Jetson Nano Super Developer Kit**
   - Main computing unit
   - Includes heatsink and fan

2. **Power Supply**
   - 5V 4A DC barrel jack power supply
   - USB-C power adapter (alternative)

3. **MicroSD Card**
   - Minimum: 32GB (64GB or 128GB recommended)
   - Class 10 or UHS-1 speed rating
   - For storing OS and captured images

4. **Camera Module**
   - **Option 1:** Raspberry Pi Camera Module V2 (8MP)
   - **Option 2:** USB Webcam (1080p or higher)
   - **Option 3:** CSI Camera compatible with Jetson Nano

5. **Network Connection**
   - Ethernet cable (recommended for initial setup)
   - OR WiFi adapter (if using wireless)

### Optional but Recommended:
6. **Display and Input Devices (for initial setup)**
   - HDMI monitor or TV
   - USB keyboard
   - USB mouse

7. **Case/Enclosure**
   - Protective case for Jetson Nano
   - Weather-resistant if used outdoors

8. **Additional Storage**
   - External USB drive or SSD for storing captured images
   - Recommended: 256GB or larger

---

## Initial Jetson Nano Super Setup

### Step 1: Prepare the MicroSD Card

**On Windows:**
1. Download **SD Card Formatter** from https://www.sdcard.org/downloads/formatter/
2. Insert microSD card into your computer
3. Open SD Card Formatter
4. Select your microSD card
5. Click "Format" (this will erase all data)
6. Wait for formatting to complete

**On Mac/Linux:**
1. Insert microSD card
2. Open Terminal
3. Find the disk identifier:
   ```bash
   diskutil list  # Mac
   lsblk          # Linux
   ```
4. Format the card:
   ```bash
   # Mac
   sudo diskutil eraseDisk FAT32 JETSON /dev/diskX
   
   # Linux
   sudo mkfs.vfat -F 32 /dev/sdX
   ```

### Step 2: Download Jetson Nano OS Image

1. Go to NVIDIA's official website: https://developer.nvidia.com/embedded/downloads
2. Download **JetPack SDK** (latest version)
   - File name: `jetson-nano-jp461-sd-card-image.zip` (or latest version)
   - Size: Approximately 6-8 GB
3. Extract the downloaded ZIP file
4. You'll get an `.img` file

### Step 3: Flash the OS Image to MicroSD Card

**Using Balena Etcher (Recommended - Works on Windows/Mac/Linux):**
1. Download Balena Etcher from https://www.balena.io/etcher/
2. Install and open Balena Etcher
3. Click "Flash from file" and select the extracted `.img` file
4. Click "Select target" and choose your microSD card
5. Click "Flash!"
6. Wait 10-20 minutes for flashing to complete
7. Safely eject the microSD card

**Using Command Line (Linux/Mac):**
```bash
# Find your SD card device
lsblk  # or diskutil list on Mac

# Flash the image (replace /dev/sdX with your SD card device)
sudo dd if=jetson-nano-image.img of=/dev/sdX bs=4M status=progress
sync
```

### Step 4: Assemble the Hardware

1. **Insert the microSD card** into the Jetson Nano (slot on bottom)
2. **Connect the camera:**
   - For CSI camera: Insert ribbon cable into CSI port (lift black tab, insert cable with contacts facing inward, press tab down)
   - For USB camera: Connect to USB port
3. **Connect peripherals:**
   - HDMI cable to monitor
   - USB keyboard and mouse
   - Ethernet cable (recommended)
4. **Connect power supply:**
   - Use 5V 4A barrel jack adapter
   - OR USB-C power (if supported)
5. **Power on** - The Jetson Nano will boot automatically

---

## Operating System Installation

### Step 5: First Boot Configuration

When you first boot the Jetson Nano, you'll see the Ubuntu setup wizard:

1. **Select Language**
   - Choose your preferred language
   - Click "Continue"

2. **Select Keyboard Layout**
   - Choose your keyboard layout
   - Click "Continue"

3. **Select Timezone**
   - Choose your timezone
   - Click "Continue"

4. **Create User Account**
   - Name: Your name
   - Computer name: `jetson-security` (or your choice)
   - Username: `jetson` (or your choice)
   - Password: Create a strong password
   - Click "Continue"

5. **Partition Selection**
   - Select "Use entire disk"
   - Click "Continue"

6. **Wait for Installation**
   - This takes 10-15 minutes
   - System will reboot automatically

7. **Login**
   - Enter your username and password
   - You'll see the Ubuntu desktop

---

## System Configuration

### Step 6: Update the System

Open Terminal (Ctrl+Alt+T) and run:

```bash
# Update package lists
sudo apt update

# Upgrade all packages
sudo apt upgrade -y

# This may take 20-30 minutes
# Reboot after completion
sudo reboot
```

### Step 7: Install Essential Tools

After reboot, open Terminal again:

```bash
# Install development tools
sudo apt install -y build-essential cmake git pkg-config

# Install system utilities
sudo apt install -y nano vim curl wget htop

# Install network tools
sudo apt install -y net-tools

# Install Python development tools
sudo apt install -y python3-dev python3-pip

# Install image processing libraries
sudo apt install -y libjpeg-dev libpng-dev libtiff-dev

# Install video processing libraries
sudo apt install -y libavcodec-dev libavformat-dev libswscale-dev libv4l-dev

# Install GUI libraries (if needed)
sudo apt install -y libgtk-3-dev
```

### Step 8: Configure Swap Space (Important for Performance)

The Jetson Nano has limited RAM, so we need to increase swap space:

```bash
# Disable current swap
sudo systemctl disable nvzramconfig

# Create 8GB swap file
sudo fallocate -l 8G /swapfile

# Set permissions
sudo chmod 600 /swapfile

# Make it a swap file
sudo mkswap /swapfile

# Enable swap
sudo swapon /swapfile

# Make it permanent
echo '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab

# Verify swap is active
free -h
```

### Step 9: Set Power Mode to Maximum Performance

```bash
# Set to maximum performance mode (10W mode)
sudo nvpmodel -m 0

# Set CPU to maximum frequency
sudo jetson_clocks

# Make it permanent (add to startup)
echo "sudo nvpmodel -m 0" | sudo tee -a /etc/rc.local
echo "sudo jetson_clocks" | sudo tee -a /etc/rc.local
```

---

## Python Environment Setup

### Step 10: Upgrade pip and Install Virtual Environment

```bash
# Upgrade pip
python3 -m pip install --upgrade pip

# Install virtual environment
sudo apt install -y python3-venv

# Create project directory
mkdir -p ~/jetson_security
cd ~/jetson_security

# Create virtual environment
python3 -m venv security_env

# Activate virtual environment
source security_env/bin/activate

# Your prompt should now show (security_env)
```

### Step 11: Install Python Dependencies

With the virtual environment activated:

```bash
# Install NumPy (optimized for Jetson)
pip install numpy

# Install OpenCV (this may take 10-15 minutes)
pip install opencv-python

# Install Pillow for image processing
pip install Pillow

# Install datetime utilities
pip install python-dateutil

# Install additional utilities
pip install pytz

# Verify installations
python3 -c "import cv2; print('OpenCV version:', cv2.__version__)"
python3 -c "import numpy; print('NumPy version:', numpy.__version__)"
```

---

## Camera Setup and Configuration

### Step 12: Test Camera Connection

**For CSI Camera (Raspberry Pi Camera Module):**

```bash
# Test camera with gstreamer
gst-launch-1.0 nvarguscamerasrc ! 'video/x-raw(memory:NVMM),width=1920,height=1080,framerate=30/1' ! nvvidconv ! nvegltransform ! nveglglessink

# If you see video feed, camera is working!
# Press Ctrl+C to stop

# Test with Python
python3 << EOF
import cv2

# For CSI camera
camera = cv2.VideoCapture("nvarguscamerasrc ! video/x-raw(memory:NVMM), width=1920, height=1080, format=NV12, framerate=30/1 ! nvvidconv ! video/x-raw, format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink", cv2.CAP_GSTREAMER)

if camera.isOpened():
    print("Camera is working!")
    ret, frame = camera.read()
    if ret:
        print(f"Frame captured: {frame.shape}")
    camera.release()
else:
    print("Camera failed to open")
EOF
```

**For USB Camera:**

```bash
# List video devices
ls -l /dev/video*

# Test USB camera
python3 << EOF
import cv2

# For USB camera (usually /dev/video0)
camera = cv2.VideoCapture(0)

if camera.isOpened():
    print("USB Camera is working!")
    ret, frame = camera.read()
    if ret:
        print(f"Frame captured: {frame.shape}")
    camera.release()
else:
    print("USB Camera failed to open")
EOF
```

### Step 13: Create Camera Test Script

Create a file to test camera capture:

```bash
nano ~/jetson_security/test_camera.py
```

Add this code:

```python
import cv2
import datetime

# For CSI Camera
CAMERA_PIPELINE = "nvarguscamerasrc ! video/x-raw(memory:NVMM), width=1920, height=1080, format=NV12, framerate=30/1 ! nvvidconv ! video/x-raw, format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink"

# For USB Camera, use: camera = cv2.VideoCapture(0)
camera = cv2.VideoCapture(CAMERA_PIPELINE, cv2.CAP_GSTREAMER)

if not camera.isOpened():
    print("Error: Could not open camera")
    exit()

print("Camera opened successfully!")
print("Press 'c' to capture image, 'q' to quit")

while True:
    ret, frame = camera.read()
    
    if not ret:
        print("Error: Could not read frame")
        break
    
    # Display frame
    cv2.imshow('Camera Test', frame)
    
    key = cv2.waitKey(1) & 0xFF
    
    if key == ord('c'):
        # Capture image
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"test_capture_{timestamp}.jpg"
        cv2.imwrite(filename, frame)
        print(f"Image saved: {filename}")
    
    elif key == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()
print("Camera test completed")
```

Save (Ctrl+O, Enter) and exit (Ctrl+X).

Run the test:
```bash
python3 test_camera.py
```

---

## AI Model Installation

### Step 14: Install TensorFlow Lite (Lightweight AI Framework)

```bash
# Activate virtual environment
cd ~/jetson_security
source security_env/bin/activate

# Install TensorFlow Lite
pip install tflite-runtime

# Or install full TensorFlow (larger, more features)
pip install tensorflow
```

### Step 15: Install Pre-trained Models

For person and car detection, we'll use MobileNet SSD:

```bash
# Create models directory
mkdir -p ~/jetson_security/models
cd ~/jetson_security/models

# Download MobileNet SSD model
wget https://storage.googleapis.com/download.tensorflow.org/models/tflite/coco_ssd_mobilenet_v1_1.0_quant_2018_06_29.zip

# Extract
unzip coco_ssd_mobilenet_v1_1.0_quant_2018_06_29.zip

# Download labels
wget https://raw.githubusercontent.com/tensorflow/models/master/research/object_detection/data/mscoco_label_map.pbtxt

# Verify files
ls -lh
# You should see: detect.tflite and labelmap.txt
```

### Step 16: Test AI Detection

Create a test script:

```bash
nano ~/jetson_security/test_detection.py
```

Add this code:

```python
import cv2
import numpy as np

# Load the model
model_path = "models/detect.tflite"

try:
    import tflite_runtime.interpreter as tflite
    interpreter = tflite.Interpreter(model_path=model_path)
    print("Using TensorFlow Lite Runtime")
except:
    import tensorflow as tf
    interpreter = tf.lite.Interpreter(model_path=model_path)
    print("Using TensorFlow")

interpreter.allocate_tensors()

# Get input and output details
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

print("Model loaded successfully!")
print(f"Input shape: {input_details[0]['shape']}")
print(f"Output shape: {output_details[0]['shape']}")

# Test with camera
camera = cv2.VideoCapture(0)  # Adjust for your camera

if camera.isOpened():
    ret, frame = camera.read()
    if ret:
        print("Camera and AI model are ready!")
    camera.release()
else:
    print("Camera not available")
```

Run the test:
```bash
python3 test_detection.py
```

---

## Security System Installation

### Step 17: Copy Your Security System Code

Create the main security system file:

```bash
cd ~/jetson_security
nano security_system.py
```

Copy your entire Python code into this file, then save and exit.

### Step 18: Create Configuration File

Create a configuration file for easy customization:

```bash
nano config.py
```

Add this configuration:

```python
# Camera Configuration
CAMERA_TYPE = "CSI"  # Options: "CSI" or "USB"
CAMERA_WIDTH = 1920
CAMERA_HEIGHT = 1080
CAMERA_FPS = 30

# For CSI Camera
CSI_PIPELINE = f"nvarguscamerasrc ! video/x-raw(memory:NVMM), width={CAMERA_WIDTH}, height={CAMERA_HEIGHT}, format=NV12, framerate={CAMERA_FPS}/1 ! nvvidconv ! video/x-raw, format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink"

# For USB Camera
USB_CAMERA_ID = 0

# Storage Configuration
IMAGE_STORAGE_PATH = "/home/jetson/jetson_security/captured_images"
LOG_FILE_PATH = "/home/jetson/jetson_security/security_log.txt"

# Detection Configuration
DETECTION_CONFIDENCE_THRESHOLD = 0.5
SCAN_INTERVAL_SECONDS = 5

# Known Entities (customize these)
KNOWN_PEOPLE = [
    {"id": "PERSON_1001", "name": "John Doe"},
    {"id": "PERSON_1002", "name": "Jane Smith"},
    {"id": "PERSON_1003", "name": "Bob Johnson"}
]

KNOWN_CARS = [
    {"plate": "ABC-123", "owner": "John Doe"},
    {"plate": "XYZ-789", "owner": "Jane Smith"},
    {"plate": "DEF-456", "owner": "Bob Johnson"}
]
```

Save and exit.

### Step 19: Create Image Storage Directory

```bash
# Create directory for captured images
mkdir -p ~/jetson_security/captured_images

# Create subdirectories
mkdir -p ~/jetson_security/captured_images/unknown_people
mkdir -p ~/jetson_security/captured_images/unknown_cars

# Set permissions
chmod 755 ~/jetson_security/captured_images
```

### Step 20: Create Startup Script

Create a script to easily start the security system:

```bash
nano ~/jetson_security/start_security.sh
```

Add this content:

```bash
#!/bin/bash

# Activate virtual environment
source /home/jetson/jetson_security/security_env/bin/activate

# Navigate to project directory
cd /home/jetson/jetson_security

# Run the security system
python3 security_system.py

# Keep script running
exec bash
```

Make it executable:
```bash
chmod +x ~/jetson_security/start_security.sh
```

---

## Testing the System

### Step 21: Run Initial Test

```bash
cd ~/jetson_security
source security_env/bin/activate
python3 security_system.py
```

You should see output like:
```
Group "security" created successfully!
Jetson Nano "front_door_security" created and added to "security"!
Added known person: John Doe (ID: PERSON_1001)
...
```

### Step 22: Test Security Scan

In Python interactive mode:

```bash
python3
```

```python
from security_system import *

# Create control panel
cp = ControlPanel()

# Create security group
cp.create_group('security')

# Create Jetson Nano device
jetson = cp.create_jetson_nano('security', 'test_camera')

# Setup known entities
cp.setup_known_entities(jetson)

# Turn on the device
jetson.turn_on()

# Run a security scan
jetson.detect_and_capture()

# Check statistics
jetson.get_statistics()

# View captured images
jetson.get_captured_images()
```

---

## Running the Security System

### Step 23: Run as Background Service

Create a systemd service for automatic startup:

```bash
sudo nano /etc/systemd/system/jetson-security.service
```

Add this content:

```ini
[Unit]
Description=Jetson Nano Security System
After=network.target

[Service]
Type=simple
User=jetson
WorkingDirectory=/home/jetson/jetson_security
ExecStart=/home/jetson/jetson_security/security_env/bin/python3 /home/jetson/jetson_security/security_system.py
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

Save and exit.

Enable and start the service:

```bash
# Reload systemd
sudo systemctl daemon-reload

# Enable service (start on boot)
sudo systemctl enable jetson-security.service

# Start service now
sudo systemctl start jetson-security.service

# Check status
sudo systemctl status jetson-security.service

# View logs
sudo journalctl -u jetson-security.service -f
```

### Step 24: Control the Service

```bash
# Stop the service
sudo systemctl stop jetson-security.service

# Restart the service
sudo systemctl restart jetson-security.service

# Disable auto-start
sudo systemctl disable jetson-security.service

# View recent logs
sudo journalctl -u jetson-security.service -n 50
```

---

## Troubleshooting

### Common Issues and Solutions

#### Issue 1: Camera Not Detected

**Solution:**
```bash
# Check if camera is connected
ls -l /dev/video*

# For CSI camera, check if driver is loaded
dmesg | grep -i camera

# Restart camera service
sudo systemctl restart nvargus-daemon

# Test with simple command
nvgstcapture-1.0
```

#### Issue 2: Out of Memory Errors

**Solution:**
```bash
# Check memory usage
free -h

# Increase swap space (if not done already)
sudo fallocate -l 8G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile

# Clear cache
sudo sh -c 'echo 3 > /proc/sys/vm/drop_caches'
```

#### Issue 3: Slow Performance

**Solution:**
```bash
# Set maximum performance mode
sudo nvpmodel -m 0
sudo jetson_clocks

# Check CPU usage
htop

# Monitor GPU usage
tegrastats
```

#### Issue 4: Python Module Not Found

**Solution:**
```bash
# Make sure virtual environment is activated
source ~/jetson_security/security_env/bin/activate

# Reinstall missing module
pip install <module_name>

# Check installed packages
pip list
```

#### Issue 5: Permission Denied Errors

**Solution:**
```bash
# Fix ownership of project directory
sudo chown -R jetson:jetson ~/jetson_security

# Fix permissions
chmod -R 755 ~/jetson_security

# For camera access
sudo usermod -a -G video jetson
```

---

## Maintenance and Updates

### Regular Maintenance Tasks

#### Weekly:
```bash
# Check system logs
sudo journalctl -u jetson-security.service -n 100

# Check disk space
df -h

# Check captured images
ls -lh ~/jetson_security/captured_images/
```

#### Monthly:
```bash
# Update system packages
sudo apt update
sudo apt upgrade -y

# Update Python packages
source ~/jetson_security/security_env/bin/activate
pip list --outdated
pip install --upgrade <package_name>

# Clean old images (older than 30 days)
find ~/jetson_security/captured_images/ -type f -mtime +30 -delete

# Backup configuration
cp ~/jetson_security/config.py ~/jetson_security/config_backup_$(date +%Y%m%d).py
```

### Backup Your System

```bash
# Create backup script
nano ~/backup_security.sh
```

Add:
```bash
#!/bin/bash

BACKUP_DIR="/home/jetson/backups"
DATE=$(date +%Y%m%d_%H%M%S)

mkdir -p $BACKUP_DIR

# Backup code and configuration
tar -czf $BACKUP_DIR/security_backup_$DATE.tar.gz \
    ~/jetson_security/*.py \
    ~/jetson_security/config.py \
    ~/jetson_security/captured_images/

echo "Backup completed: $BACKUP_DIR/security_backup_$DATE.tar.gz"
```

Make executable and run:
```bash
chmod +x ~/backup_security.sh
./backup_security.sh
```

---

## Remote Access Setup (Optional)

### Enable SSH for Remote Management

```bash
# Install SSH server (usually pre-installed)
sudo apt install openssh-server -y

# Start SSH service
sudo systemctl start ssh
sudo systemctl enable ssh

# Find your IP address
hostname -I

# From another computer, connect via:
# ssh jetson@<IP_ADDRESS>
```

### Setup VNC for Remote Desktop

```bash
# Install VNC server
sudo apt install vino -y

# Enable VNC
gsettings set org.gnome.Vino require-encryption false
gsettings set org.gnome.Vino prompt-enabled false

# Start VNC server
/usr/lib/vino/vino-server &

# Connect from another computer using VNC client
# Address: <JETSON_IP>:5900
```

---

## Performance Optimization Tips

1. **Use CSI camera instead of USB** - Better performance and lower CPU usage
2. **Reduce image resolution** - If 1080p is too slow, try 720p
3. **Adjust detection frequency** - Don't scan every second, use 5-10 second intervals
4. **Use TensorFlow Lite** - Lighter than full TensorFlow
5. **Enable GPU acceleration** - Make sure CUDA is being used
6. **Limit concurrent processes** - Don't run too many programs simultaneously
7. **Use efficient image formats** - JPEG instead of PNG for storage
8. **Implement motion detection** - Only run AI detection when motion is detected

---

## Security Best Practices

1. **Change default passwords** - Use strong, unique passwords
2. **Enable firewall** - Limit network access
3. **Keep system updated** - Regular security updates
4. **Encrypt sensitive data** - Especially stored images
5. **Limit physical access** - Secure the Jetson Nano device
6. **Monitor logs regularly** - Check for suspicious activity
7. **Backup regularly** - Don't lose your configuration and data

---

## Conclusion

Your Jetson Nano Super is now fully configured as an IoT security system! The system will:
- Automatically detect people and cars
- Capture images of unknown entities
- Log all security events
- Run continuously in the background
- Start automatically on boot

For questions or issues, refer to:
- NVIDIA Jetson Forums: https://forums.developer.nvidia.com/
- Jetson Nano Documentation: https://developer.nvidia.com/embedded/learn/get-started-jetson-nano-devkit

**Your security system is now operational!**
