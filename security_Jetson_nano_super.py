'''
Besiar awlii
dakhele har function ya class , tozihe kamel bezarid mitoen proozhe va resumeye khoobi beshe


'''


#written with assistant
class Device:
    def __init__(self, location, group, device_type, device_name):
        self.location = location
        self.group = group
        self.device_type = device_type
        self.device_name = device_name 
        self.status = 'off'

    def turn_on(self):
        if self.status == 'off':
            print(f'{self.device_name} turned ON!')
            self.status = 'on'
        else:
            print(f'{self.device_name} is already ON!')

    def turn_off(self):
        if self.status == 'on':
            print(f'{self.device_name} turned OFF!')
            self.status = 'off'
        else:
            print(f'{self.device_name} is already OFF!')
       
    def get_status(self):
        return self.status == 'on'
    
    def __str__(self):
        return f"{self.device_name} ({self.device_type}) - Status: {self.status}"


class Sensor:
    def __init__(self, location, group, sensor_type, sensor_name):
        self.location = location
        self.group = group
        self.sensor_name = sensor_name
        self.sensor_type = sensor_type
        
    def read_data(self):
        # Simulating different sensor data based on type
        import random
        if self.sensor_type.lower() == 'temperature':
            return random.randint(18, 30)  # Temperature in Celsius
        elif self.sensor_type.lower() == 'humidity':
            return random.randint(30, 80)  # Humidity percentage
        elif self.sensor_type.lower() == 'motion':
            return random.choice([True, False])  # Motion detected or not
        else:
            return random.randint(0, 100)  # Generic sensor value
    
    def __str__(self):
        return f"{self.sensor_name} ({self.sensor_type}) - Location: {self.location}"


class ControlPanel:
    def __init__(self):
        self.groups = {}
        self.sensors = {}
    def setup_known_entities(self, jetson_device):
        """Helper method to setup known people and cars for a Jetson Nano device"""
        if isinstance(jetson_device, JetsonNano):
        # Add some example known people
            jetson_device.add_known_person("PERSON_1001", "John Doe")
            jetson_device.add_known_person("PERSON_1002", "Jane Smith")
            jetson_device.add_known_person("PERSON_1003", "Bob Johnson")
            
        # Add some example known cars
            jetson_device.add_known_car("ABC-123", "John Doe")
            jetson_device.add_known_car("XYZ-789", "Jane Smith")
            jetson_device.add_known_car("DEF-456", "Bob Johnson")
        
            print(f'Known entities setup completed for {jetson_device.device_name}')
        else:
            print('Device is not a Jetson Nano!')

def run_security_scan(self, group_name=None):
    """Run security detection on all Jetson Nano devices"""
    if group_name:
        if group_name in self.groups:
            devices = self.groups[group_name]
            jetson_devices = [d for d in devices if isinstance(d, JetsonNano)]
            
            if jetson_devices:
                print(f'Running security scan in group "{group_name}":')
                for jetson in jetson_devices:
                    jetson.detect_and_capture()
            else:
                print(f'No Jetson Nano devices found in group "{group_name}"')
        else:
            print(f'Group "{group_name}" does not exist!')
    else:
        print('Running security scan on all Jetson Nano devices:')
        total_jetson = 0
        for group_name, devices in self.groups.items():
            jetson_devices = [d for d in devices if isinstance(d, JetsonNano)]
            if jetson_devices:
                print(f'  Scanning group "{group_name}":')
                for jetson in jetson_devices:
                    jetson.detect_and_capture()
                    total_jetson += 1
        
        if total_jetson == 0:
            print('No Jetson Nano devices found in any group!')
        else:
            print(f'Security scan completed on {total_jetson} Jetson Nano devices.')

def get_security_alerts(self, group_name=None):
    """Get security alerts from all Jetson Nano devices"""
    if group_name:
        if group_name in self.groups:
            devices = self.groups[group_name]
            jetson_devices = [d for d in devices if isinstance(d, JetsonNano)]
            
            if jetson_devices:
                print(f'Security alerts for group "{group_name}":')
                for jetson in jetson_devices:
                    print(f'\n--- {jetson.device_name} ---')
                    jetson.get_detection_log(5)
            else:
                print(f'No Jetson Nano devices found in group "{group_name}"')
        else:
            print(f'Group "{group_name}" does not exist!')
    else:
        print('All security alerts:')
        for group_name, devices in self.groups.items():
            jetson_devices = [d for d in devices if isinstance(d, JetsonNano)]
            if jetson_devices:
                print(f'\n=== Group: {group_name} ===')
                for jetson in jetson_devices:
                    print(f'\n--- {jetson.device_name} ---')
                    jetson.get_detection_log(3)

        
    def create_jetson_nano(self, group_name, device_name):
        """Create a Jetson Nano security device"""
        if group_name in self.groups:
            location = 'home'
            new_jetson = JetsonNano(location, group_name, device_name)
            self.groups[group_name].append(new_jetson)
            print(f'Jetson Nano "{device_name}" created and added to "{group_name}"!')
            return new_jetson
        else:
            print(f'Group "{group_name}" does not exist!')
            return None
  
    def create_group(self, group_name):
        if group_name not in self.groups:
            self.groups[group_name] = []
            print(f'Group "{group_name}" created successfully!')
        else:
            print(f'Group "{group_name}" already exists!')
    
    def add_device_to_group(self, group_name, device):
        if group_name in self.groups:
            if isinstance(device, Device):
                self.groups[group_name].append(device)
                device.group = group_name
                print(f'Device "{device.device_name}" added to group "{group_name}"')
            else:
                print('Invalid device object!')
        else:
            print(f'Group "{group_name}" does not exist!')
        
    def create_device(self, group_name, device_type, device_name):
        if group_name in self.groups:
            location = 'home'
            new_device = Device(location, group_name, device_type, device_name)
            self.groups[group_name].append(new_device)
            print(f'Device "{device_name}" created and added to "{group_name}"!')
            return new_device
        else:
            print(f'Group "{group_name}" does not exist!')
            return None
        
    def create_multiple_device(self, group_name, device_type, device_number):
        if group_name in self.groups:
            created_devices = []
            for i in range(1, device_number + 1):
                device_name = f'{device_type}_{i}'
                device = self.create_device(group_name, device_type, device_name)
                if device:
                    created_devices.append(device)
            
            print(f'{len(created_devices)} devices of type "{device_type}" created successfully!')
            return created_devices
        else:
            print(f'Group "{group_name}" does not exist!')
            return []

    def get_devices(self, group_name):
        if group_name in self.groups:
            return self.groups[group_name]
        else:
            print(f'Group "{group_name}" does not exist!')
            return []
    
    def turn_on_in_group(self, group_name):
        if group_name in self.groups:
            devices = self.get_devices(group_name)
            if devices:
                print(f'Turning ON all devices in group "{group_name}":')
                for device in devices:
                    device.turn_on()
            else:
                print(f'No devices found in group "{group_name}"')
        else:
            print(f'Group "{group_name}" does not exist!')
            
    def turn_off_in_group(self, group_name):
        if group_name in self.groups:
            devices = self.get_devices(group_name)
            if devices:
                print(f'Turning OFF all devices in group "{group_name}":')
                for device in devices:
                    device.turn_off()
            else:
                print(f'No devices found in group "{group_name}"')
        else:
            print(f'Group "{group_name}" does not exist!')

    def turn_on_all(self):
        print('Turning ON all devices in all groups:')
        total_devices = 0
        for group_name in self.groups:
            devices = self.groups[group_name]
            for device in devices:
                device.turn_on()
                total_devices += 1
        
        if total_devices == 0:
            print('No devices found to turn on!')
        else:
            print(f'Total {total_devices} devices turned ON!')

    def turn_off_all(self):
        print('Turning OFF all devices in all groups:')
        total_devices = 0
        for group_name in self.groups:
            devices = self.groups[group_name]
            for device in devices:
                device.turn_off()
                total_devices += 1
        
        if total_devices == 0:
            print('No devices found to turn off!')
        else:
            print(f'Total {total_devices} devices turned OFF!')

    def get_status_in_group(self, group_name):
        if group_name in self.groups:
            devices = self.get_devices(group_name)
            if devices:
                print(f'Status of devices in group "{group_name}":')
                for device in devices:
                    status_text = "ON" if device.get_status() else "OFF"
                    print(f'  Device "{device.device_name}" is {status_text}')
            else:
                print(f'No devices found in group "{group_name}"')
        else:
            print(f'Group "{group_name}" does not exist!')
    
    def get_status_in_device_type(self, device_type):
        print(f'Status of all "{device_type}" devices:')
        found_devices = []
        
        for group_name, devices in self.groups.items():
            for device in devices:
                if device.device_type.lower() == device_type.lower():
                    found_devices.append(device)
                    status_text = "ON" if device.get_status() else "OFF"
                    print(f'  {device.device_name} (in {group_name}) is {status_text}')
        
        if not found_devices:
            print(f'No devices of type "{device_type}" found!')
        else:
            print(f'Total {len(found_devices)} "{device_type}" devices found.')
    
    def create_sensor(self, group_name, sensor_type, sensor_name):
        if group_name not in self.sensors:
            self.sensors[group_name] = []
        
        location = 'home'
        new_sensor = Sensor(location, group_name, sensor_type, sensor_name)
        self.sensors[group_name].append(new_sensor)
        print(f'Sensor "{sensor_name}" created and added to "{group_name}"!')
        return new_sensor
    
    def create_multiple_sensor(self, group_name, sensor_type, sensor_number):
        if group_name not in self.sensors:
            self.sensors[group_name] = []
        
        created_sensors = []
        for i in range(1, sensor_number + 1):
            sensor_name = f'{sensor_type}_{i}'
            sensor = self.create_sensor(group_name, sensor_type, sensor_name)
            if sensor:
                created_sensors.append(sensor)
        
        print(f'{len(created_sensors)} sensors of type "{sensor_type}" created successfully!')
        return created_sensors
    
    def get_sensors(self, group_name):
        if group_name in self.sensors:
            return self.sensors[group_name]
        else:
            print(f'No sensors found in group "{group_name}"')
            return []
    
    def read_all_sensors(self, group_name=None):
        if group_name:
            if group_name in self.sensors:
                sensors = self.sensors[group_name]
                print(f'Reading sensors in group "{group_name}":')
                for sensor in sensors:
                    data = sensor.read_data()
                    print(f'  {sensor.sensor_name}: {data}')
            else:
                print(f'No sensors found in group "{group_name}"')
        else:
            print('Reading all sensors:')
            for group_name, sensors in self.sensors.items():
                print(f'  Group "{group_name}":')
                for sensor in sensors:
                    data = sensor.read_data()
                    print(f'    {sensor.sensor_name}: {data}')
    
    def display_all_groups(self):
        print('=== All Groups ===')
        for group_name in self.groups:
            print(f'\nGroup: {group_name}')
            
            # Display devices
            devices = self.groups[group_name]
            if devices:
                print('  Devices:')
                for device in devices:
                    status_text = "ON" if device.get_status() else "OFF"
                    print(f'    - {device.device_name} ({device.device_type}) - {status_text}')
            else:
                print('  No devices in this group')
            
            # Display sensors
            sensors = self.sensors.get(group_name, [])
            if sensors:
                print('  Sensors:')
                for sensor in sensors:
                    print(f'    - {sensor.sensor_name} ({sensor.sensor_type})')
            else:
                print('  No sensors in this group')
import random
import datetime
import os

# ============= NEW JETSON NANO DEVICE CLASS =============
class JetsonNano(Device):
    def __init__(self, location, group, device_name):
        super().__init__(location, group, 'jetson_nano', device_name)
        self.detection_enabled = False
        self.known_people = []  # List of known person IDs
        self.known_cars = []    # List of known car license plates
        self.captured_images = []
        self.detection_log = []
        
    def turn_on(self):
        super().turn_on()
        self.detection_enabled = True
        print(f'{self.device_name} AI detection system is now ACTIVE!')
        
    def turn_off(self):
        super().turn_off()
        self.detection_enabled = False
        print(f'{self.device_name} AI detection system is now INACTIVE!')
    
    def add_known_person(self, person_id, name):
        """Add a known person to the database"""
        person_data = {'id': person_id, 'name': name}
        if person_data not in self.known_people:
            self.known_people.append(person_data)
            print(f'Added known person: {name} (ID: {person_id})')
        else:
            print(f'Person {name} is already in the database')
    
    def add_known_car(self, license_plate, owner):
        """Add a known car to the database"""
        car_data = {'plate': license_plate, 'owner': owner}
        if car_data not in self.known_cars:
            self.known_cars.append(car_data)
            print(f'Added known car: {license_plate} (Owner: {owner})')
        else:
            print(f'Car {license_plate} is already in the database')
    
    def detect_and_capture(self):
        """Simulate AI detection and capture unknown people/cars"""
        if not self.detection_enabled:
            print(f'{self.device_name} detection is disabled!')
            return
            
        # Simulate detection results
        detection_types = ['person', 'car', 'both', 'none']
        detection_result = random.choice(detection_types)
        
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        if detection_result == 'none':
            print(f'[{timestamp}] {self.device_name}: No objects detected')
            return
            
        unknown_detected = False
        
        if detection_result in ['person', 'both']:
            # Simulate person detection
            detected_person_id = f"PERSON_{random.randint(1000, 9999)}"
            is_known = any(person['id'] == detected_person_id for person in self.known_people)
            
            if not is_known:
                unknown_detected = True
                image_filename = f"unknown_person_{detected_person_id}_{timestamp.replace(':', '-')}.jpg"
                self.capture_image(image_filename, 'unknown_person')
                
                log_entry = {
                    'timestamp': timestamp,
                    'type': 'unknown_person',
                    'id': detected_person_id,
                    'image': image_filename,
                    'location': self.location
                }
                self.detection_log.append(log_entry)
                
                print(f' [ALERT] {self.device_name}: Unknown person detected!')
                print(f'   Person ID: {detected_person_id}')
                print(f'   Image captured: {image_filename}')
            else:
                known_person = next(person for person in self.known_people if person['id'] == detected_person_id)
                print(f' [OK] {self.device_name}: Known person detected - {known_person["name"]}')
    
        if detection_result in ['car', 'both']:
        # Simulate car detection
            detected_license = f"ABC-{random.randint(100, 999)}"
            is_known_car = any(car['plate'] == detected_license for car in self.known_cars)
        
            if not is_known_car:
                unknown_detected = True
                image_filename = f"unknown_car_{detected_license}_{timestamp.replace(':', '-')}.jpg"
                self.capture_image(image_filename, 'unknown_car')
            
                log_entry = {
                    'timestamp': timestamp,
                    'type': 'unknown_car',
                    'license': detected_license,
                    'image': image_filename,
                    'location': self.location
            }
                self.detection_log.append(log_entry)
            
                print(f' [ALERT] {self.device_name}: Unknown car detected!')
                print(f'   License plate: {detected_license}')
                print(f'   Image captured: {image_filename}')
            else:
                known_car = next(car for car in self.known_cars if car['plate'] == detected_license)
                print(f'[OK] {self.device_name}: Known car detected - {known_car["owner"]}\'s {detected_license}')
    
        if unknown_detected:
            print(f'  Security alert logged at {timestamp}')

def capture_image(self, filename, detection_type):
    """Simulate capturing an image"""
    image_data = {
        'filename': filename,
        'type': detection_type,
        'timestamp': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'location': self.location
    }
    self.captured_images.append(image_data)
    
    # Simulate saving to filesystem (in real implementation, this would save actual image)
    print(f' Image saved: {filename}')

def get_detection_log(self, limit=10):
    """Get recent detection logs"""
    if not self.detection_log:
        print('No detection logs available')
        return
    
    print(f'=== Recent Detection Log for {self.device_name} ===')
    recent_logs = self.detection_log[-limit:]
    
    for log in recent_logs:
        if log['type'] == 'unknown_person':
            print(f"[{log['timestamp']}] Unknown Person - ID: {log['id']}")
            print(f"   Image: {log['image']}")
        elif log['type'] == 'unknown_car':
            print(f"[{log['timestamp']}] Unknown Car - License: {log['license']}")
            print(f"   Image: {log['image']}")
        print(f"   Location: {log['location']}")
        print("---")

def get_captured_images(self):
    """Get list of all captured images"""
    if not self.captured_images:
        print('No images captured yet')
        return
    
    print(f'=== Captured Images by {self.device_name} ===')
    for image in self.captured_images:
        print(f" {image['filename']}")
        print(f"   Type: {image['type']}")
        print(f"   Time: {image['timestamp']}")
        print(f"   Location: {image['location']}")
        print("---")
        
def clear_old_data(self, days_old=30):
        """Clear detection logs and images older than specified days"""
        cutoff_date = datetime.datetime.now() - datetime.timedelta(days=days_old)
        
        # Filter logs
        old_log_count = len(self.detection_log)
        self.detection_log = [
            log for log in self.detection_log 
            if datetime.datetime.strptime(log['timestamp'], "%Y-%m-%d %H:%M:%S") >= cutoff_date
        ]
        
        # Filter images
        old_image_count = len(self.captured_images)
        self.captured_images = [
            image for image in self.captured_images 
            if datetime.datetime.strptime(image['timestamp'], "%Y-%m-%d %H:%M:%S") >= cutoff_date
        ]
        
        removed_logs = old_log_count - len(self.detection_log)
        removed_images = old_image_count - len(self.captured_images)
        
        print(f'Cleanup completed: Removed {removed_logs} old logs and {removed_images} old images')
def get_statistics(self):
        """Get detection statistics"""
        total_detections = len(self.detection_log)
        person_detections = sum(1 for log in self.detection_log if log['type'] == 'unknown_person')
        car_detections = sum(1 for log in self.detection_log if log['type'] == 'unknown_car')
        
        print(f'=== {self.device_name} Statistics ===')
        print(f'Status: {"ACTIVE" if self.detection_enabled else "INACTIVE"}')
        print(f'Total unknown detections: {total_detections}')
        print(f'Unknown people detected: {person_detections}')
        print(f'Unknown cars detected: {car_detections}')
        print(f'Known people in database: {len(self.known_people)}')
        print(f'Known cars in database: {len(self.known_cars)}')
        print(f'Total images captured: {len(self.captured_images)}')

# ============= END OF JETSON NANO CLASS =============


# ============= UPDATED ControlPanel CLASS METHODS =============
# Add these methods to your existing ControlPanel class:

def create_jetson_nano(self, group_name, device_name):
        """Create a Jetson Nano security device"""
        if group_name in self.groups:
            location = 'home'
            new_jetson = JetsonNano(location, group_name, device_name)
            self.groups[group_name].append(new_jetson)
            print(f'Jetson Nano "{device_name}" created and added to "{group_name}"!')
            return new_jetson
        else:
            print(f'Group "{group_name}" does not exist!')
            return None
    
def run_security_scan(self, group_name=None):
        """Run security detection on all Jetson Nano devices"""
        if group_name:
            if group_name in self.groups:
                devices = self.groups[group_name]
                jetson_devices = [d for d in devices if isinstance(d, JetsonNano)]
                
                if jetson_devices:
                    print(f'Running security scan in group "{group_name}":')
                    for jetson in jetson_devices:
                        jetson.detect_and_capture()
                else:
                    print(f'No Jetson Nano devices found in group "{group_name}"')
            else:
                print(f'Group "{group_name}" does not exist!')
        else:
            print('Running security scan on all Jetson Nano devices:')
            total_jetson = 0
            for group_name, devices in self.groups.items():
                jetson_devices = [d for d in devices if isinstance(d, JetsonNano)]
                if jetson_devices:
                    print(f'  Scanning group "{group_name}":')
                    for jetson in jetson_devices:
                        jetson.detect_and_capture()
                        total_jetson += 1
            
            if total_jetson == 0:
                print('No Jetson Nano devices found in any group!')
            else:
                print(f'Security scan completed on {total_jetson} Jetson Nano devices.')
    
def get_security_alerts(self, group_name=None):
        """Get security alerts from all Jetson Nano devices"""
        if group_name:
            if group_name in self.groups:
                devices = self.groups[group_name]
                jetson_devices = [d for d in devices if isinstance(d, JetsonNano)]
                
                if jetson_devices:
                    print(f'Security alerts for group "{group_name}":')
                    for jetson in jetson_devices:
                        print(f'\n--- {jetson.device_name} ---')
                        jetson.get_detection_log(5)
                else:
                    print(f'No Jetson Nano devices found in group "{group_name}"')
            else:
                print(f'Group "{group_name}" does not exist!')
        else:
            print('All security alerts:')
            for group_name, devices in self.groups.items():
                jetson_devices = [d for d in devices if isinstance(d, JetsonNano)]
                if jetson_devices:
                    print(f'\n=== Group: {group_name} ===')
                    for jetson in jetson_devices:
                        print(f'\n--- {jetson.device_name} ---')
                        jetson.get_detection_log(3)
    
def setup_known_entities(self, jetson_device):
        """Helper method to setup known people and cars for a Jetson Nano device"""
        if isinstance(jetson_device, JetsonNano):
            # Add some example known people
            jetson_device.add_known_person("PERSON_1001", "John Doe")
            jetson_device.add_known_person("PERSON_1002", "Jane Smith")
            jetson_device.add_known_person("PERSON_1003", "Bob Johnson")
            
            # Add some example known cars
            jetson_device.add_known_car("ABC-123", "John Doe")
            jetson_device.add_known_car("XYZ-789", "Jane Smith")
            jetson_device.add_known_car("DEF-456", "Bob Johnson")
            
            print(f'Known entities setup completed for {jetson_device.device_name}')
        else:
            print('Device is not a Jetson Nano!')

# ============= END OF UPDATED ControlPanel METHODS =============


# ============= UPDATED EXAMPLE USAGE =============
if __name__ == "__main__":
    # Create control panel
    cp = ControlPanel()
    
    # Create groups
    cp.create_group('living_room')
    cp.create_group('bedroom')
    cp.create_group('kitchen')
    cp.create_group('security')
    
    # Create regular devices
    cp.create_device('living_room', 'lamp', 'main_lamp')
    cp.create_device('living_room', 'tv', 'smart_tv')
    cp.create_multiple_device('bedroom', 'lamp', 3)
    cp.create_multiple_device('kitchen', 'light', 2)
    
    # Create Jetson Nano security devices
    jetson1 = cp.create_jetson_nano('security', 'front_door_security')
    jetson2 = cp.create_jetson_nano('security', 'garage_security')
    jetson3 = cp.create_jetson_nano('living_room', 'indoor_security')
    
    # Setup known entities for Jetson Nano devices
    if jetson1:
        cp.setup_known_entities(jetson1)
    if jetson2:
        cp.setup_known_entities(jetson2)
    if jetson3:
        cp.setup_known_entities(jetson3)
    
    # Create sensors
    cp.create_sensor('living_room', 'temperature', 'temp_sensor_1')
    cp.create_sensor('bedroom', 'motion', 'motion_detector')
    cp.create_multiple_sensor('kitchen', 'humidity', 2)
    
    # Test regular device operations
    print('\n=== Testing Regular Device Operations ===')
    cp.turn_on_in_group('living_room')
    print()
    cp.get_status_in_group('living_room')
    print()
    cp.get_status_in_device_type('lamp')
    
    # Test Jetson Nano security operations
    print('\n=== Testing Jetson Nano Security System ===')
    
    # Turn on security devices
    cp.turn_on_in_group('security')
    if jetson3:
        jetson3.turn_on()
    
    print('\n--- Running Security Scans ---')
    # Run multiple security scans to generate some data
    for i in range(5):
        print(f'\nSecurity Scan #{i+1}:')
        cp.run_security_scan('security')
        if jetson3:
            jetson3.detect_and_capture()
    
    print('\n--- Security Statistics ---')
    # Display statistics for each Jetson Nano
    if jetson1:
        jetson1.get_statistics()
        print()
    if jetson2:
        jetson2.get_statistics()
        print()
    if jetson3:
        jetson3.get_statistics()
        print()
    
    print('\n--- Security Alerts ---')
    # Get security alerts
    cp.get_security_alerts('security')
    
    print('\n--- Captured Images ---')
    # Show captured images
    if jetson1:
        jetson1.get_captured_images()
    
    print('\n=== Testing Sensor Operations ===')
    cp.read_all_sensors('living_room')
    cp.read_all_sensors()
    
    print('\n=== Display All Groups ===')
    cp.display_all_groups()
    
    print('\n=== Testing Turn Off All ===')
    cp.turn_off_all()
    
    print('\n=== Final Status ===')
    cp.display_all_groups()
    
    print('\n=== Security System Cleanup ===')
    # Clean up old data (simulate cleanup after 0 days to show functionality)
    if jetson1:
        jetson1.clear_old_data(0)  # This will clear all data for demo purposes

# ============= END OF EXAMPLE USAGE =============


# ============= ADDITIONAL UTILITY FUNCTIONS =============
def simulate_continuous_monitoring(control_panel, duration_minutes=1):
    """
    Simulate continuous security monitoring
    This function would run the security scan every few seconds in a real implementation
    """
    import time
    
    print(f'\n=== Starting Continuous Security Monitoring for {duration_minutes} minute(s) ===')
    print('Press Ctrl+C to stop monitoring early\n')
    
    end_time = time.time() + (duration_minutes * 60)
    scan_count = 0
    
    try:
        while time.time() < end_time:
            scan_count += 1
            print(f'--- Monitoring Scan #{scan_count} ---')
            control_panel.run_security_scan()
            
            # Wait 10 seconds between scans
            print('Waiting 10 seconds before next scan...\n')
            time.sleep(10)
            
    except KeyboardInterrupt:
        print('\n⚠️ Monitoring stopped by user')
    
    print(f'\n=== Monitoring Complete ===')
    print(f'Total scans performed: {scan_count}')
    print('Getting final security alerts...\n')
    control_panel.get_security_alerts()

def create_security_report(control_panel, filename="security_report.txt"):
    """
    Generate a comprehensive security report
    """
    import datetime
    
    print(f'Generating security report: {filename}')
    
    report_content = []
    report_content.append("=" * 50)
    report_content.append("SMART HOME SECURITY REPORT")
    report_content.append("=" * 50)
    report_content.append(f"Generated: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    report_content.append("")
    
    # Find all Jetson Nano devices
    jetson_devices = []
    for group_name, devices in control_panel.groups.items():
        for device in devices:
            if isinstance(device, JetsonNano):
                jetson_devices.append((group_name, device))
    
    if not jetson_devices:
        report_content.append("No Jetson Nano security devices found.")
        return
    
    # Generate report for each device
    for group_name, jetson in jetson_devices:
        report_content.append(f"DEVICE: {jetson.device_name}")
        report_content.append(f"Group: {group_name}")
        report_content.append(f"Location: {jetson.location}")
        report_content.append(f"Status: {'ACTIVE' if jetson.detection_enabled else 'INACTIVE'}")
        report_content.append("")
        
        # Statistics
        total_detections = len(jetson.detection_log)
        person_detections = sum(1 for log in jetson.detection_log if log['type'] == 'unknown_person')
        car_detections = sum(1 for log in jetson.detection_log if log['type'] == 'unknown_car')
        
        report_content.append("STATISTICS:")
        report_content.append(f"  Total unknown detections: {total_detections}")
        report_content.append(f"  Unknown people: {person_detections}")
        report_content.append(f"  Unknown cars: {car_detections}")
        report_content.append(f"  Known people in database: {len(jetson.known_people)}")
        report_content.append(f"  Known cars in database: {len(jetson.known_cars)}")
        report_content.append(f"  Images captured: {len(jetson.captured_images)}")
        report_content.append("")
        
        # Recent alerts
        if jetson.detection_log:
            report_content.append("RECENT ALERTS (Last 5):")
            recent_logs = jetson.detection_log[-5:]
            for log in recent_logs:
                if log['type'] == 'unknown_person':
                    report_content.append(f"  [{log['timestamp']}] Unknown Person - ID: {log['id']}")
                elif log['type'] == 'unknown_car':
                    report_content.append(f"  [{log['timestamp']}] Unknown Car - License: {log['license']}")
                report_content.append(f"    Image: {log.get('image', 'N/A')}")
        else:
            report_content.append("No alerts recorded.")
        
        report_content.append("")
        report_content.append("-" * 30)
        report_content.append("")
    
    # Write report to file
    try:
        with open(filename, 'w') as f:
            f.write('\n'.join(report_content))
        print(f'Security report saved to: {filename}')
    except Exception as e:
        print(f'Error saving report: {e}')
        # Print report to console instead
        print('\n'.join(report_content))

def emergency_lockdown(control_panel):
    """
    Emergency function to activate all security devices and turn off all other devices
    """
    print('\n🚨 EMERGENCY LOCKDOWN ACTIVATED 🚨')
    print('Turning off all non-security devices...')
    
    # Turn off all regular devices
    for group_name, devices in control_panel.groups.items():
        for device in devices:
            if not isinstance(device, JetsonNano) and device.status == 'on':
                device.turn_off()
    
    print('Activating all security devices...')
    
    # Turn on all Jetson Nano devices
    jetson_count = 0
    for group_name, devices in control_panel.groups.items():
        for device in devices:
            if isinstance(device, JetsonNano):
                if device.status == 'off':
                    device.turn_on()
                jetson_count += 1
    
    print(f'Emergency lockdown complete: {jetson_count} security devices activated')
    
    # Run immediate security scan
    print('Running immediate security scan...')
    control_panel.run_security_scan()

def setup_demo_scenario(control_panel):
    """
    Setup a complete demo scenario with multiple security events
    """
    print('\n=== Setting up Demo Security Scenario ===')
    
    # Find Jetson Nano devices
    jetson_devices = []
    for group_name, devices in control_panel.groups.items():
        for device in devices:
            if isinstance(device, JetsonNano):
                jetson_devices.append(device)
    
    if not jetson_devices:
        print('No Jetson Nano devices found for demo!')
        return
    
    # Ensure devices are active
    for jetson in jetson_devices:
        if jetson.status == 'off':
            jetson.turn_on()
    
    # Simulate multiple security events
    print('Simulating security events...')
    for i in range(10):
        for jetson in jetson_devices:
            jetson.detect_and_capture()
    
    print('Demo scenario setup complete!')
    return jetson_devices

# ============= END OF UTILITY FUNCTIONS =============


# ============= ADVANCED EXAMPLE WITH ALL FEATURES =============
def run_advanced_demo():
    """
    Run an advanced demo showcasing all features
    """
    print("🏠 SMART HOME SECURITY SYSTEM - ADVANCED DEMO 🏠")
    print("=" * 60)
    
    # Initialize system
    cp = ControlPanel()
    
    # Setup home layout
    print("\n1. Setting up smart home layout...")
    groups = ['entrance', 'living_room', 'kitchen', 'bedroom', 'garage', 'backyard']
    for group in groups:
        cp.create_group(group)
    
    # Add regular devices
    print("\n2. Installing regular smart devices...")
    cp.create_multiple_device('living_room', 'lamp', 3)
    cp.create_multiple_device('kitchen', 'light', 2)
    cp.create_device('bedroom', 'fan', 'ceiling_fan')
    cp.create_device('garage', 'door', 'garage_door')
    # Install security system
    print("\n3. Installing Jetson Nano security system...")
    jetson_entrance = cp.create_jetson_nano('entrance', 'main_entrance_cam')
    jetson_garage = cp.create_jetson_nano('garage', 'garage_security_cam')
    jetson_backyard = cp.create_jetson_nano('backyard', 'backyard_monitor')
    
    # Setup known entities for all security devices
    print("\n4. Configuring security database...")
    security_devices = [jetson_entrance, jetson_garage, jetson_backyard]
    for jetson in security_devices:
        if jetson:
            cp.setup_known_entities(jetson)
    
    # Add sensors
    print("\n5. Installing environmental sensors...")
    cp.create_sensor('living_room', 'temperature', 'main_temp_sensor')
    cp.create_sensor('entrance', 'motion', 'door_motion_sensor')
    cp.create_multiple_sensor('kitchen', 'humidity', 2)
    cp.create_sensor('garage', 'temperature', 'garage_temp')
    
    # System status check
    print("\n6. System Status Check...")
    cp.display_all_groups()
    
    # Activate security system
    print("\n7. Activating security system...")
    cp.turn_on_in_group('entrance')
    cp.turn_on_in_group('garage')
    cp.turn_on_in_group('backyard')
    
    # Simulate normal day activity
    print("\n8. Simulating normal day activity...")
    cp.turn_on_in_group('living_room')
    cp.turn_on_in_group('kitchen')
    
    # Read environmental data
    print("\n9. Reading environmental sensors...")
    cp.read_all_sensors()
    
    # Security monitoring phase
    print("\n10. Running security monitoring (5 scans)...")
    for scan in range(5):
        print(f"\n--- Security Scan #{scan + 1} ---")
        cp.run_security_scan()
    
    # Generate alerts and statistics
    print("\n11. Security Analysis...")
    cp.get_security_alerts()
    
    print("\n12. Security Statistics...")
    for jetson in security_devices:
        if jetson:
            jetson.get_statistics()
            print()
    
    # Emergency scenario
    print("\n13. Simulating emergency scenario...")
    emergency_lockdown(cp)
    
    # Generate security report
    print("\n14. Generating security report...")
    create_security_report(cp, "advanced_demo_security_report.txt")
    
    # System cleanup
    print("\n15. System maintenance...")
    for jetson in security_devices:
        if jetson:
            print(f"Cleaning old data for {jetson.device_name}...")
            jetson.clear_old_data(0)  # Clear all for demo
    
    # Final status
    print("\n16. Final System Status...")
    cp.display_all_groups()
    
    print("\n" + "=" * 60)
    print("🎉 ADVANCED DEMO COMPLETED SUCCESSFULLY! 🎉")
    print("=" * 60)

# ============= MAIN EXECUTION =============
if __name__ == "__main__":
    # You can choose which demo to run:
    
    # Option 1: Run the original simple demo
    # (Uncomment the following lines for simple demo)
    """
    cp = ControlPanel()
    cp.create_group('living_room')
    cp.create_group('security')
    
    jetson1 = cp.create_jetson_nano('security', 'front_door_security')
    if jetson1:
        cp.setup_known_entities(jetson1)
        jetson1.turn_on()
        for i in range(3):
            jetson1.detect_and_capture()
        jetson1.get_statistics()
        jetson1.get_detection_log()
    """
    
    # Option 2: Run the advanced comprehensive demo
    run_advanced_demo()
    
    # Option 3: Run continuous monitoring demo (uncomment to use)
    """
    print("\n" + "=" * 60)
    print("Starting continuous monitoring demo...")
    cp = ControlPanel()
    cp.create_group('security')
    jetson = cp.create_jetson_nano('security', 'continuous_monitor')
    if jetson:
        cp.setup_known_entities(jetson)
        simulate_continuous_monitoring(cp, duration_minutes=0.5)  # 30 seconds demo
    """
    
    # Option 4: Interactive demo mode (uncomment to use)
    """
    print("\n" + "=" * 60)
    print("🔧 INTERACTIVE SECURITY SYSTEM DEMO 🔧")
    print("Available commands:")
    print("1. Setup system")
    print("2. Run security scan")
    print("3. Get alerts")
    print("4. Emergency lockdown")
    print("5. Generate report")
    print("6. Exit")
    
    cp = ControlPanel()
    
    while True:
        choice = input("\nEnter command (1-6): ").strip()
        
        if choice == '1':
            print("Setting up demo system...")
            setup_demo_scenario(cp)
        elif choice == '2':
            print("Running security scan...")
            cp.run_security_scan()
        elif choice == '3':
            print("Getting security alerts...")
            cp.get_security_alerts()
        elif choice == '4':
            print("Initiating emergency lockdown...")
            emergency_lockdown(cp)
        elif choice == '5':
            print("Generating security report...")
            create_security_report(cp, "interactive_demo_report.txt")
        elif choice == '6':
            print("Exiting interactive demo. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1-6.")
    """

# ============= END OF COMPLETE SMART HOME SECURITY SYSTEM =============

"""
SYSTEM FEATURES SUMMARY:
========================

1. DEVICE MANAGEMENT:
   - Regular smart devices (lamps, TVs, fans, etc.)
   - Jetson Nano AI security cameras
   - Environmental sensors
   - Group-based organization

2. SECURITY FEATURES:
   - Real-time person and vehicle detection
   - Known entity database (people and cars)
   - Automatic image capture of unknown entities
   - Security alert logging
   - Detection statistics and reporting

3. CONTROL CAPABILITIES:
   - Individual device control
   - Group-based control
   - Emergency lockdown mode
   - Continuous monitoring
   - Automated security scans

4. DATA MANAGEMENT:
   - Detection logs with timestamps
   - Image capture and storage simulation
   - Security report generation
   - Data cleanup and maintenance
   - Statistical analysis

5. MONITORING & ALERTS:
   - Real-time security alerts
   - Historical log review
   - System status monitoring
   - Environmental sensor readings
   - Comprehensive reporting

Usage Examples:
- Home security monitoring
- Access control systems
- Perimeter surveillance
- Smart home automation
- Emergency response systems
"""


# ============= END OF ControlPanel CLASS =============


# ============= EXAMPLE USAGE AND TESTING =============
#''' if __name__ == "__main__":
    # Create control panel
    #cp = ControlPanel()
    
    # Create groups
    #cp.create_group('living_room')
   # cp.create_group('bedroom')
   # cp.create_group('kitchen')
    
    # Create individual devices
   # cp.create_device('living_room', 'lamp', 'main_lamp')
    #cp.create_device('living_room', 'tv', 'smart_tv')
    
    # Create multiple devices
    #cp.create_multiple_device('bedroom', 'lamp', 3)
    #cp.create_multiple_device('kitchen', 'light', 2)
    
    # Create sensors
    #cp.create_sensor('living_room', 'temperature', 'temp_sensor_1')
    #cp.create_sensor('bedroom', 'motion', 'motion_detector')
    #cp.create_multiple_sensor('kitchen', 'humidity', 2)
    
    # Test device operations
    #print('\n=== Testing Device Operations ===')
    #cp.turn_on_in_group('living_room')
   # print()
   # cp.get_status_in_group('living_room')
    #print()
    #cp.get_status_in_device_type('lamp')
    
   # print('\n=== Testing Sensor Operations ===')
    #cp.read_all_sensors('living_room')
    #cp.read_all_sensors()
    
   # print('\n=== Display All Groups ===')
   # cp.display_all_groups()
    
   # print('\n=== Testing Turn Off All ===')
   # cp.turn_off_all()
    
    #print('\n=== Final Status ===')
    #cp.display_all_groups()'''


