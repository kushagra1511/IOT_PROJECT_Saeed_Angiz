# IoT Security System - Quick Reference Guide

## Project Summary

**Project Name:** Jetson Nano Super IoT Security System  
**Purpose:** Automated detection and capture of unknown people and vehicles  
**Platform:** NVIDIA Jetson Nano Super  
**Language:** Python 3  
**AI Framework:** TensorFlow Lite / OpenCV

---

## System Architecture

```
┌─────────────────────────────────────────────────────────┐
│                  Control Panel                          │
│  (Central management system for all devices)            │
└─────────────────┬───────────────────────────────────────┘
                  │
        ┌─────────┴─────────┐
        │                   │
┌───────▼────────┐  ┌──────▼──────────┐
│  Device Groups │  │  Sensor Groups  │
│  (by location) │  │  (by location)  │
└───────┬────────┘  └─────────────────┘
        │
┌───────▼──────────────────────────────────────────┐
│           Jetson Nano Devices                    │
│  - AI Detection System                           │
│  - Camera Interface                              │
│  - Image Capture                                 │
│  - Known Entity Database                         │
│  - Alert System                                  │
└──────────────────────────────────────────────────┘
```

---

## Key Features

### 1. Automated Detection
- Real-time person detection
- Real-time vehicle detection
- AI-powered recognition

### 2. Smart Filtering
- Maintains database of known people
- Maintains database of known vehicles
- Only alerts on unknown entities

### 3. Evidence Collection
- Automatic image capture
- Timestamped photos
- Organized storage

### 4. Logging System
- Comprehensive event logs
- Detection timestamps
- Location tracking

### 5. Multi-Device Support
- Multiple Jetson Nano devices
- Group organization
- Centralized control

---

## Class Structure

### Device Class (Base Class)
- Basic device functionality
- ON/OFF control
- Status monitoring

### Sensor Class
- Environmental monitoring
- Data collection
- Multiple sensor types

### JetsonNano Class (Inherits from Device)
- AI detection capabilities
- Camera interface
- Image capture
- Security logging
- Known entity management

### ControlPanel Class
- Central management
- Group organization
- Multi-device control
- Security monitoring

---

## Main Functions Overview

### Security Functions
| Function | Purpose |
|----------|---------|
| `detect_and_capture()` | Main AI detection and image capture |
| `add_known_person()` | Register authorized person |
| `add_known_car()` | Register authorized vehicle |
| `get_detection_log()` | View security alerts |
| `get_statistics()` | View detection statistics |
| `capture_image()` | Save security photo |

### Management Functions
| Function | Purpose |
|----------|---------|
| `create_jetson_nano()` | Create new security device |
| `run_security_scan()` | Trigger detection on all devices |
| `get_security_alerts()` | View all security alerts |
| `setup_known_entities()` | Quick setup of authorized entities |
| `turn_on_in_group()` | Activate device group |
| `turn_off_in_group()` | Deactivate device group |

---

## Quick Start Commands

### Start the System
```bash
cd ~/jetson_security
source security_env/bin/activate
python3 security_system.py
```

### Check System Status
```bash
sudo systemctl status jetson-security.service
```

### View Live Logs
```bash
sudo journalctl -u jetson-security.service -f
```

### Stop the System
```bash
sudo systemctl stop jetson-security.service
```

### Restart the System
```bash
sudo systemctl restart jetson-security.service
```

---

## Python Usage Examples

### Example 1: Basic Setup
```python
from security_system import *

# Create control panel
cp = ControlPanel()

# Create security group
cp.create_group('security')

# Create Jetson Nano device
jetson = cp.create_jetson_nano('security', 'front_door')

# Add known people
jetson.add_known_person("PERSON_1001", "John Doe")
jetson.add_known_person("PERSON_1002", "Jane Smith")

# Add known cars
jetson.add_known_car("ABC-123", "John Doe")
jetson.add_known_car("XYZ-789", "Jane Smith")

# Turn on the device
jetson.turn_on()
```

### Example 2: Run Security Scan
```python
# Single scan
jetson.detect_and_capture()

# Multiple scans
for i in range(5):
    print(f"Scan #{i+1}")
    jetson.detect_and_capture()
    time.sleep(5)  # Wait 5 seconds between scans
```

### Example 3: View Results
```python
# View statistics
jetson.get_statistics()

# View recent alerts
jetson.get_detection_log(10)  # Last 10 alerts

# View captured images
jetson.get_captured_images()
```

### Example 4: Multi-Device Setup
```python
# Create multiple locations
cp.create_group('front_door')
cp.create_group('back_door')
cp.create_group('garage')

# Create Jetson Nano for each location
jetson1 = cp.create_jetson_nano('front_door', 'front_camera')
jetson2 = cp.create_jetson_nano('back_door', 'back_camera')
jetson3 = cp.create_jetson_nano('garage', 'garage_camera')

# Setup all devices
for jetson in [jetson1, jetson2, jetson3]:
    cp.setup_known_entities(jetson)
    jetson.turn_on()

# Run scan on all devices
cp.run_security_scan()

# View all alerts
cp.get_security_alerts()
```

---

## File Structure

```
~/jetson_security/
├── security_system.py          # Main security system code
├── config.py                   # Configuration file
├── test_camera.py              # Camera test script
├── test_detection.py           # AI detection test
├── start_security.sh           # Startup script
├── security_env/               # Python virtual environment
├── models/                     # AI models
│   ├── detect.tflite          # Detection model
│   └── labelmap.txt           # Object labels
├── captured_images/            # Stored security photos
│   ├── unknown_people/        # Photos of unknown people
│   └── unknown_cars/          # Photos of unknown cars
└── logs/                       # System logs
    └── security_log.txt       # Detection log file
```

---

## Configuration Options

### Camera Settings (config.py)
```python
CAMERA_TYPE = "CSI"              # "CSI" or "USB"
CAMERA_WIDTH = 1920              # Resolution width
CAMERA_HEIGHT = 1080             # Resolution height
CAMERA_FPS = 30                  # Frames per second
```

### Detection Settings
```python
DETECTION_CONFIDENCE_THRESHOLD = 0.5    # 0.0 to 1.0
SCAN_INTERVAL_SECONDS = 5               # Seconds between scans
```

### Storage Settings
```python
IMAGE_STORAGE_PATH = "/path/to/images"
LOG_FILE_PATH = "/path/to/logs"
```

---

## Troubleshooting Quick Fixes

### Camera Not Working
```bash
# Restart camera daemon
sudo systemctl restart nvargus-daemon

# Test camera
nvgstcapture-1.0
```

### System Running Slow
```bash
# Set maximum performance
sudo nvpmodel -m 0
sudo jetson_clocks

# Check memory
free -h
```

### Service Won't Start
```bash
# Check logs
sudo journalctl -u jetson-security.service -n 50

# Check file permissions
ls -l ~/jetson_security/security_system.py

# Fix permissions
chmod +x ~/jetson_security/security_system.py
```

### Out of Disk Space
```bash
# Check disk usage
df -h

# Clean old images (older than 30 days)
find ~/jetson_security/captured_images/ -type f -mtime +30 -delete

# Clean system cache
sudo apt clean
sudo apt autoclean
```

---

## Performance Tips

1. **Optimize Camera Resolution**
   - Use 720p instead of 1080p if performance is slow
   - Lower FPS if needed (15-20 FPS is often sufficient)

2. **Adjust Scan Frequency**
   - Don't scan every second
   - 5-10 second intervals are usually adequate

3. **Use Motion Detection**
   - Only run AI detection when motion is detected
   - Saves CPU and power

4. **Limit Stored Images**
   - Automatically delete old images
   - Use compression for storage

5. **Monitor System Resources**
   ```bash
   # Check CPU/GPU usage
   tegrastats
   
   # Check memory
   free -h
   
   # Check disk space
   df -h
   ```

---

## Maintenance Schedule

### Daily
- Check system is running: `sudo systemctl status jetson-security.service`
- Review recent alerts: `jetson.get_detection_log(10)`

### Weekly
- Review captured images
- Check disk space: `df -h`
- Review system logs: `sudo journalctl -u jetson-security.service -n 100`

### Monthly
- Update system: `sudo apt update && sudo apt upgrade`
- Update Python packages: `pip list --outdated`
- Clean old images: `find ~/jetson_security/captured_images/ -mtime +30 -delete`
- Backup configuration: `cp config.py config_backup.py`

### Quarterly
- Full system backup
- Review and update known entities
- Check hardware (camera, connections)
- Update AI models if available

---

## Important File Locations

| Item | Location |
|------|----------|
| Main Code | `~/jetson_security/security_system.py` |
| Configuration | `~/jetson_security/config.py` |
| Virtual Environment | `~/jetson_security/security_env/` |
| Captured Images | `~/jetson_security/captured_images/` |
| System Service | `/etc/systemd/system/jetson-security.service` |
| System Logs | `sudo journalctl -u jetson-security.service` |
| AI Models | `~/jetson_security/models/` |

---

## Useful Commands Reference

### System Control
```bash
# Start service
sudo systemctl start jetson-security.service

# Stop service
sudo systemctl stop jetson-security.service

# Restart service
sudo systemctl restart jetson-security.service

# Enable auto-start
sudo systemctl enable jetson-security.service

# Disable auto-start
sudo systemctl disable jetson-security.service

# Check status
sudo systemctl status jetson-security.service
```

### Monitoring
```bash
# View live logs
sudo journalctl -u jetson-security.service -f

# View last 50 log entries
sudo journalctl -u jetson-security.service -n 50

# View logs from today
sudo journalctl -u jetson-security.service --since today

# Check system resources
tegrastats

# Check memory usage
free -h

# Check disk usage
df -h

# Check CPU temperature
cat /sys/devices/virtual/thermal/thermal_zone*/temp
```

### File Management
```bash
# List captured images
ls -lh ~/jetson_security/captured_images/

# Count captured images
find ~/jetson_security/captured_images/ -type f | wc -l

# Find large files
du -h ~/jetson_security/ | sort -rh | head -20

# Delete old images (30+ days)
find ~/jetson_security/captured_images/ -type f -mtime +30 -delete
```

---

## Network Access

### Find Jetson IP Address
```bash
hostname -I
```

### SSH Access (from another computer)
```bash
ssh jetson@<JETSON_IP_ADDRESS>
```

### Copy Files from Jetson (from another computer)
```bash
# Copy single file
scp jetson@<JETSON_IP>:~/jetson_security/captured_images/image.jpg ./

# Copy entire directory
scp -r jetson@<JETSON_IP>:~/jetson_security/captured_images/ ./
```

### Copy Files to Jetson (from another computer)
```bash
scp local_file.py jetson@<JETSON_IP>:~/jetson_security/
```

---

## Emergency Procedures

### System Frozen
1. Try SSH access from another computer
2. If accessible, restart service: `sudo systemctl restart jetson-security.service`
3. If not accessible, power cycle the Jetson Nano

### Camera Stopped Working
```bash
# Restart camera daemon
sudo systemctl restart nvargus-daemon

# Restart security service
sudo systemctl restart jetson-security.service

# If still not working, reboot
sudo reboot
```

### Disk Full
```bash
# Check what's using space
du -h ~/jetson_security/ | sort -rh | head -20

# Delete old images
find ~/jetson_security/captured_images/ -type f -mtime +7 -delete

# Clean system cache
sudo apt clean
sudo apt autoclean

# Remove old logs
sudo journalctl --vacuum-time=7d
```

### System Won't Boot
1. Remove power
2. Remove microSD card
3. Insert microSD into computer
4. Backup important files
5. Re-flash OS image if necessary

---

## Support Resources

### Official Documentation
- NVIDIA Jetson: https://developer.nvidia.com/embedded/jetson-nano-developer-kit
- JetPack SDK: https://developer.nvidia.com/embedded/jetpack

### Community Forums
- NVIDIA Developer Forums: https://forums.developer.nvidia.com/
- Jetson Projects: https://developer.nvidia.com/embedded/community/jetson-projects

### Python Libraries
- OpenCV: https://docs.opencv.org/
- TensorFlow: https://www.tensorflow.org/lite

---

## Project Specifications

### Hardware Requirements
- **Processor:** NVIDIA Jetson Nano Super
- **RAM:** 4GB (8GB recommended)
- **Storage:** 32GB microSD minimum (64GB+ recommended)
- **Camera:** CSI or USB camera (1080p or higher)
- **Power:** 5V 4A power supply

### Software Requirements
- **OS:** Ubuntu 18.04/20.04 (JetPack)
- **Python:** 3.6+
- **OpenCV:** 4.x
- **TensorFlow Lite:** Latest
- **NumPy:** Latest

### Performance Metrics
- **Detection Speed:** 1-3 seconds per frame
- **Image Capture:** < 1 second
- **Storage:** ~2-5 MB per captured image
- **Power Consumption:** 5-10W typical

---

## Customization Ideas

### Add Email Alerts
```python
import smtplib
from email.mime.text import MIMEText

def send_alert_email(subject, message):
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = 'security@yourdomain.com'
    msg['To'] = 'your@email.com'
    
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('your@email.com', 'your_password')
    server.send_message(msg)
    server.quit()
```

### Add Telegram Notifications
```python
import requests

def send_telegram_alert(message):
    bot_token = 'YOUR_BOT_TOKEN'
    chat_id = 'YOUR_CHAT_ID'
    url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
    data = {'chat_id': chat_id, 'text': message}
    requests.post(url, data=data)
```

### Add Web Dashboard
- Use Flask or Django to create web interface
- Display live camera feed
- Show recent alerts
- View captured images
- Control system remotely

---

## Conclusion

This IoT security system provides comprehensive protection through:
- ✅ Automated detection of unknown people and vehicles
- ✅ Real-time image capture and logging
- ✅ Multi-device support
- ✅ Easy management and monitoring
- ✅ Expandable and customizable

**Your property is now protected by AI-powered security!**

For detailed information, refer to:
- **FUNCTION_DOCUMENTATION.md** - Complete function descriptions
- **JETSON_NANO_SETUP_GUIDE.md** - Step-by-step setup instructions
