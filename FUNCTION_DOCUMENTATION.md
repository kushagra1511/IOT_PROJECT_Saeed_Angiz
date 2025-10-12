# IoT Security System - Function Documentation

## Project Overview
This is an IoT security system designed for Jetson Nano Super that uses AI to detect unknown people and cars, automatically capturing images for security purposes. The system manages multiple smart devices and sensors through a centralized control panel.

---

## Table of Contents
1. [Device Class](#device-class)
2. [Sensor Class](#sensor-class)
3. [JetsonNano Class](#jetsonnano-class)
4. [ControlPanel Class](#controlpanel-class)
5. [Utility Functions](#utility-functions)

---

## Device Class

### `__init__(self, location, group, device_type, device_name)`
**Purpose:** Initializes a new smart device object.

**Parameters:**
- `location` (str): Physical location of the device (e.g., "home", "office")
- `group` (str): Group name the device belongs to (e.g., "living_room", "security")
- `device_type` (str): Type of device (e.g., "lamp", "tv", "jetson_nano")
- `device_name` (str): Unique name for the device

**What it does:**
- Creates a new device instance with the specified properties
- Automatically sets the device status to 'off' when created
- Stores all device information for later use

---

### `turn_on(self)`
**Purpose:** Turns the device ON.

**What it does:**
- Checks if the device is currently OFF
- If OFF, changes status to 'on' and prints confirmation message
- If already ON, prints a message indicating the device is already ON
- Prevents redundant operations

---

### `turn_off(self)`
**Purpose:** Turns the device OFF.

**What it does:**
- Checks if the device is currently ON
- If ON, changes status to 'off' and prints confirmation message
- If already OFF, prints a message indicating the device is already OFF
- Ensures safe device shutdown

---

### `get_status(self)`
**Purpose:** Returns the current status of the device.

**Returns:** Boolean value (True if device is ON, False if OFF)

**What it does:**
- Provides a simple way to check if a device is currently active
- Used by other functions to determine device state

---

### `__str__(self)`
**Purpose:** Provides a human-readable string representation of the device.

**Returns:** Formatted string with device information

**What it does:**
- Creates a formatted string showing device name, type, and current status
- Used when printing device information
- Example output: "main_lamp (lamp) - Status: on"

---

## Sensor Class

### `__init__(self, location, group, sensor_type, sensor_name)`
**Purpose:** Initializes a new sensor object.

**Parameters:**
- `location` (str): Physical location of the sensor
- `group` (str): Group name the sensor belongs to
- `sensor_type` (str): Type of sensor (e.g., "temperature", "humidity", "motion")
- `sensor_name` (str): Unique name for the sensor

**What it does:**
- Creates a new sensor instance with specified properties
- Stores sensor configuration for data collection

---

### `read_data(self)`
**Purpose:** Simulates reading data from the sensor.

**Returns:** Sensor reading based on sensor type

**What it does:**
- Generates simulated sensor data based on sensor type:
  - Temperature sensors: Returns random value between 18-30°C
  - Humidity sensors: Returns random value between 30-80%
  - Motion sensors: Returns True (motion detected) or False (no motion)
  - Other sensors: Returns random value between 0-100
- In a real implementation, this would read actual sensor hardware

---

### `__str__(self)`
**Purpose:** Provides a human-readable string representation of the sensor.

**Returns:** Formatted string with sensor information

**What it does:**
- Creates a formatted string showing sensor name, type, and location
- Example output: "temp_sensor_1 (temperature) - Location: home"

---

## JetsonNano Class

### `__init__(self, location, group, device_name)`
**Purpose:** Initializes a Jetson Nano security device.

**Parameters:**
- `location` (str): Physical location of the Jetson Nano
- `group` (str): Group name the device belongs to
- `device_name` (str): Unique name for the Jetson Nano device

**What it does:**
- Inherits from Device class (gets all basic device functionality)
- Automatically sets device_type to 'jetson_nano'
- Initializes detection system as disabled
- Creates empty lists for:
  - Known people (authorized persons)
  - Known cars (authorized vehicles)
  - Captured images (security photos)
  - Detection log (security events)

---

### `turn_on(self)`
**Purpose:** Activates the Jetson Nano and enables AI detection system.

**What it does:**
- Calls the parent Device class turn_on() method
- Enables the AI detection system (sets detection_enabled to True)
- Prints confirmation that AI detection is now ACTIVE
- Makes the device ready to detect and capture unknown entities

---

### `turn_off(self)`
**Purpose:** Deactivates the Jetson Nano and disables AI detection system.

**What it does:**
- Calls the parent Device class turn_off() method
- Disables the AI detection system (sets detection_enabled to False)
- Prints confirmation that AI detection is now INACTIVE
- Stops security monitoring

---

### `add_known_person(self, person_id, name)`
**Purpose:** Adds an authorized person to the security database.

**Parameters:**
- `person_id` (str): Unique identifier for the person (e.g., "PERSON_1001")
- `name` (str): Name of the person (e.g., "John Doe")

**What it does:**
- Creates a dictionary with person's ID and name
- Checks if person is already in the database
- If new, adds person to known_people list
- If already exists, prints message indicating person is already registered
- Prevents duplicate entries

---

### `add_known_car(self, license_plate, owner)`
**Purpose:** Adds an authorized vehicle to the security database.

**Parameters:**
- `license_plate` (str): Vehicle license plate number (e.g., "ABC-123")
- `owner` (str): Name of the vehicle owner

**What it does:**
- Creates a dictionary with car's license plate and owner name
- Checks if car is already in the database
- If new, adds car to known_cars list
- If already exists, prints message indicating car is already registered
- Prevents duplicate entries

---

### `detect_and_capture(self)`
**Purpose:** Main AI detection function that identifies and captures unknown people and cars.

**What it does:**
1. **Checks if detection is enabled** - If disabled, prints message and exits
2. **Simulates AI detection** - Randomly detects: person, car, both, or none
3. **Gets current timestamp** - Records exact time of detection
4. **For person detection:**
   - Generates a random person ID
   - Checks if person is in known_people database
   - If UNKNOWN:
     - Triggers ALERT
     - Captures image with unique filename
     - Logs detection event with timestamp, ID, image filename, and location
     - Prints alert message with person ID and image filename
   - If KNOWN:
     - Prints OK message with person's name
     - No alert or image capture
5. **For car detection:**
   - Generates a random license plate
   - Checks if car is in known_cars database
   - If UNKNOWN:
     - Triggers ALERT
     - Captures image with unique filename
     - Logs detection event with timestamp, license plate, image filename, and location
     - Prints alert message with license plate and image filename
   - If KNOWN:
     - Prints OK message with owner's name
     - No alert or image capture
6. **Logs security event** - If any unknown entity detected, logs the event with timestamp

**This is the core security function that protects your property!**

---

### `capture_image(self, filename, detection_type)`
**Purpose:** Simulates capturing and saving an image of detected entity.

**Parameters:**
- `filename` (str): Name for the saved image file
- `detection_type` (str): Type of detection ("unknown_person" or "unknown_car")

**What it does:**
- Creates an image data dictionary containing:
  - Filename
  - Detection type
  - Timestamp
  - Location
- Adds image data to captured_images list
- Prints confirmation that image was saved
- In real implementation, this would save actual camera image to filesystem

---

### `get_detection_log(self, limit=10)`
**Purpose:** Displays recent security detection events.

**Parameters:**
- `limit` (int): Maximum number of recent logs to display (default: 10)

**What it does:**
- Checks if any detection logs exist
- If no logs, prints message and exits
- Retrieves the most recent logs (up to limit specified)
- For each log entry, displays:
  - Timestamp of detection
  - Type (unknown person or unknown car)
  - ID or license plate
  - Image filename
  - Location
- Provides quick overview of recent security events

---

### `get_captured_images(self)`
**Purpose:** Displays list of all captured security images.

**What it does:**
- Checks if any images have been captured
- If no images, prints message and exits
- For each captured image, displays:
  - Filename
  - Type (unknown_person or unknown_car)
  - Timestamp when captured
  - Location where captured
- Helps review all security evidence collected

---

### `clear_old_data(self, days_old=30)`
**Purpose:** Removes old detection logs and images to free up storage space.

**Parameters:**
- `days_old` (int): Number of days to keep data (default: 30 days)

**What it does:**
- Calculates cutoff date (current date minus days_old)
- Filters detection_log to keep only recent entries
- Filters captured_images to keep only recent images
- Counts how many logs and images were removed
- Prints summary of cleanup operation
- Helps manage storage space on Jetson Nano

---

### `get_statistics(self)`
**Purpose:** Displays comprehensive statistics about the security device.

**What it does:**
- Calculates and displays:
  - Current status (ACTIVE or INACTIVE)
  - Total number of unknown detections
  - Number of unknown people detected
  - Number of unknown cars detected
  - Number of known people in database
  - Number of known cars in database
  - Total images captured
- Provides overview of security system performance

---

## ControlPanel Class

### `__init__(self)`
**Purpose:** Initializes the central control panel for managing all devices and sensors.

**What it does:**
- Creates empty dictionary for device groups
- Creates empty dictionary for sensor groups
- Sets up the foundation for managing entire smart home system

---

### `create_group(self, group_name)`
**Purpose:** Creates a new group for organizing devices.

**Parameters:**
- `group_name` (str): Name for the new group (e.g., "living_room", "security")

**What it does:**
- Checks if group already exists
- If new, creates empty list for the group
- If exists, prints message that group already exists
- Allows logical organization of devices by location or function

---

### `create_device(self, group_name, device_type, device_name)`
**Purpose:** Creates a new smart device and adds it to a group.

**Parameters:**
- `group_name` (str): Group to add device to
- `device_type` (str): Type of device
- `device_name` (str): Name for the device

**Returns:** The created Device object, or None if group doesn't exist

**What it does:**
- Checks if specified group exists
- If exists:
  - Creates new Device object
  - Adds device to the group
  - Prints confirmation message
  - Returns the device object
- If group doesn't exist, prints error message

---

### `create_multiple_device(self, group_name, device_type, device_number)`
**Purpose:** Creates multiple devices of the same type at once.

**Parameters:**
- `group_name` (str): Group to add devices to
- `device_type` (str): Type of devices to create
- `device_number` (int): How many devices to create

**Returns:** List of created Device objects

**What it does:**
- Checks if group exists
- Creates specified number of devices
- Automatically names them (e.g., lamp_1, lamp_2, lamp_3)
- Adds all devices to the group
- Prints summary of how many devices were created
- Saves time when setting up multiple similar devices

---

### `create_jetson_nano(self, group_name, device_name)`
**Purpose:** Creates a Jetson Nano security device and adds it to a group.

**Parameters:**
- `group_name` (str): Group to add Jetson Nano to
- `device_name` (str): Name for the Jetson Nano device

**Returns:** The created JetsonNano object, or None if group doesn't exist

**What it does:**
- Checks if specified group exists
- If exists:
  - Creates new JetsonNano object
  - Adds it to the group
  - Prints confirmation message
  - Returns the Jetson Nano object
- If group doesn't exist, prints error message

---

### `setup_known_entities(self, jetson_device)`
**Purpose:** Helper function to quickly setup known people and cars for a Jetson Nano.

**Parameters:**
- `jetson_device`: The JetsonNano object to configure

**What it does:**
- Verifies the device is actually a JetsonNano
- Adds example known people:
  - John Doe (PERSON_1001)
  - Jane Smith (PERSON_1002)
  - Bob Johnson (PERSON_1003)
- Adds example known cars:
  - ABC-123 (John Doe's car)
  - XYZ-789 (Jane Smith's car)
  - DEF-456 (Bob Johnson's car)
- Prints confirmation message
- Provides quick way to initialize security database

---

### `add_device_to_group(self, group_name, device)`
**Purpose:** Adds an existing device to a group.

**Parameters:**
- `group_name` (str): Group to add device to
- `device`: Device object to add

**What it does:**
- Checks if group exists
- Verifies the object is a valid Device
- Adds device to the group
- Updates device's group property
- Prints confirmation message

---

### `get_devices(self, group_name)`
**Purpose:** Retrieves all devices in a specific group.

**Parameters:**
- `group_name` (str): Name of the group

**Returns:** List of devices in the group, or empty list if group doesn't exist

**What it does:**
- Checks if group exists
- Returns list of all devices in that group
- If group doesn't exist, prints error and returns empty list

---

### `turn_on_in_group(self, group_name)`
**Purpose:** Turns ON all devices in a specific group.

**Parameters:**
- `group_name` (str): Name of the group

**What it does:**
- Checks if group exists
- Gets all devices in the group
- Calls turn_on() for each device
- Prints status messages for each device
- Useful for controlling multiple devices at once (e.g., turn on all living room lights)

---

### `turn_off_in_group(self, group_name)`
**Purpose:** Turns OFF all devices in a specific group.

**Parameters:**
- `group_name` (str): Name of the group

**What it does:**
- Checks if group exists
- Gets all devices in the group
- Calls turn_off() for each device
- Prints status messages for each device
- Useful for controlling multiple devices at once

---

### `turn_on_all(self)`
**Purpose:** Turns ON every device in all groups.

**What it does:**
- Iterates through all groups
- Turns on every device found
- Counts total devices turned on
- Prints summary message
- Master switch for entire system

---

### `turn_off_all(self)`
**Purpose:** Turns OFF every device in all groups.

**What it does:**
- Iterates through all groups
- Turns off every device found
- Counts total devices turned off
- Prints summary message
- Master switch to shut down entire system

---

### `get_status_in_group(self, group_name)`
**Purpose:** Displays status of all devices in a specific group.

**Parameters:**
- `group_name` (str): Name of the group

**What it does:**
- Checks if group exists
- Gets all devices in the group
- For each device, displays name and status (ON or OFF)
- Provides quick overview of group status

---

### `get_status_in_device_type(self, device_type)`
**Purpose:** Displays status of all devices of a specific type across all groups.

**Parameters:**
- `device_type` (str): Type of device to check (e.g., "lamp", "jetson_nano")

**What it does:**
- Searches through all groups
- Finds all devices matching the specified type
- Displays each device's name, group, and status
- Counts total devices found
- Useful for checking all devices of same type at once

---

### `run_security_scan(self, group_name=None)`
**Purpose:** Runs security detection on Jetson Nano devices.

**Parameters:**
- `group_name` (str, optional): Specific group to scan, or None to scan all groups

**What it does:**
- If group_name specified:
  - Scans only Jetson Nano devices in that group
- If no group specified:
  - Scans all Jetson Nano devices in all groups
- Calls detect_and_capture() for each Jetson Nano
- Prints summary of how many devices were scanned
- This is the main function to trigger security monitoring

---

### `get_security_alerts(self, group_name=None)`
**Purpose:** Retrieves and displays security alerts from Jetson Nano devices.

**Parameters:**
- `group_name` (str, optional): Specific group to check, or None to check all groups

**What it does:**
- If group_name specified:
  - Shows alerts only from Jetson Nano devices in that group
  - Displays last 5 detection logs for each device
- If no group specified:
  - Shows alerts from all Jetson Nano devices
  - Displays last 3 detection logs for each device
- Organizes alerts by group and device
- Provides quick security overview

---

### `create_sensor(self, group_name, sensor_type, sensor_name)`
**Purpose:** Creates a new sensor and adds it to a group.

**Parameters:**
- `group_name` (str): Group to add sensor to
- `sensor_type` (str): Type of sensor (e.g., "temperature", "motion")
- `sensor_name` (str): Name for the sensor

**Returns:** The created Sensor object

**What it does:**
- Creates sensor group if it doesn't exist
- Creates new Sensor object
- Adds sensor to the group
- Prints confirmation message
- Returns the sensor object

---

### `create_multiple_sensor(self, group_name, sensor_type, sensor_number)`
**Purpose:** Creates multiple sensors of the same type at once.

**Parameters:**
- `group_name` (str): Group to add sensors to
- `sensor_type` (str): Type of sensors to create
- `sensor_number` (int): How many sensors to create

**Returns:** List of created Sensor objects

**What it does:**
- Creates sensor group if it doesn't exist
- Creates specified number of sensors
- Automatically names them (e.g., temperature_1, temperature_2)
- Adds all sensors to the group
- Prints summary message
- Returns list of sensor objects

---

### `get_sensors(self, group_name)`
**Purpose:** Retrieves all sensors in a specific group.

**Parameters:**
- `group_name` (str): Name of the group

**Returns:** List of sensors in the group, or empty list if no sensors found

**What it does:**
- Checks if group has sensors
- Returns list of all sensors in that group
- If no sensors found, prints message and returns empty list

---

### `read_all_sensors(self, group_name=None)`
**Purpose:** Reads data from sensors.

**Parameters:**
- `group_name` (str, optional): Specific group to read, or None to read all sensors

**What it does:**
- If group_name specified:
  - Reads only sensors in that group
- If no group specified:
  - Reads all sensors in all groups
- Calls read_data() for each sensor
- Displays sensor name and reading
- Provides environmental monitoring data

---

### `display_all_groups(self)`
**Purpose:** Displays comprehensive overview of entire system.

**What it does:**
- Lists all groups
- For each group, shows:
  - All devices with their type and status
  - All sensors with their type
- Provides complete system status at a glance
- Useful for system overview and debugging

---

## Utility Functions

### `simulate_continuous_monitoring(control_panel, duration_minutes=1)`
**Purpose:** Simulates continuous security monitoring for a specified duration.

**Parameters:**
- `control_panel`: ControlPanel object to use
- `duration_minutes` (int): How long to monitor (default: 1 minute)

**What it does:**
- Runs security scans repeatedly
- Waits 10 seconds between each scan
- Counts total scans performed
- Can be stopped early with Ctrl+C
- Displays final security alerts when complete
- Simulates real-world continuous monitoring

---

### `create_security_report(control_panel, filename="security_report.txt")`
**Purpose:** Generates a comprehensive security report file.

**Parameters:**
- `control_panel`: ControlPanel object to generate report from
- `filename` (str): Name for the report file (default: "security_report.txt")

**What it does:**
- Creates formatted security report
- Includes timestamp of report generation
- Finds all Jetson Nano devices
- For each device, includes:
  - Device name and group
  - Status (active/inactive)
  - Detection statistics
  - Recent detection logs
- Saves report to text file
- Provides documentation for security review

---

## Summary

This IoT security system provides:
- **Automated Detection**: AI-powered detection of unknown people and cars
- **Image Capture**: Automatic photography of unknown entities
- **Database Management**: Maintains lists of authorized people and vehicles
- **Alert System**: Real-time alerts for security events
- **Logging**: Comprehensive logs of all detection events
- **Multi-Device Support**: Manages multiple Jetson Nano devices simultaneously
- **Group Organization**: Logical grouping of devices by location
- **Statistics**: Detailed statistics and reporting
- **Storage Management**: Automatic cleanup of old data

The system is designed to be expandable, maintainable, and easy to use for home or business security applications.
