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

# ============= END OF ControlPanel CLASS =============


# ============= EXAMPLE USAGE AND TESTING =============
if __name__ == "__main__":
    # Create control panel
    cp = ControlPanel()
    
    # Create groups
    cp.create_group('living_room')
    cp.create_group('bedroom')
    cp.create_group('kitchen')
    
    # Create individual devices
    cp.create_device('living_room', 'lamp', 'main_lamp')
    cp.create_device('living_room', 'tv', 'smart_tv')
    
    # Create multiple devices
    cp.create_multiple_device('bedroom', 'lamp', 3)
    cp.create_multiple_device('kitchen', 'light', 2)
    
    # Create sensors
    cp.create_sensor('living_room', 'temperature', 'temp_sensor_1')
    cp.create_sensor('bedroom', 'motion', 'motion_detector')
    cp.create_multiple_sensor('kitchen', 'humidity', 2)
    
    # Test device operations
    print('\n=== Testing Device Operations ===')
    cp.turn_on_in_group('living_room')
    print()
    cp.get_status_in_group('living_room')
    print()
    cp.get_status_in_device_type('lamp')
    
    print('\n=== Testing Sensor Operations ===')
    cp.read_all_sensors('living_room')
    cp.read_all_sensors()
    
    print('\n=== Display All Groups ===')
    cp.display_all_groups()
    
    print('\n=== Testing Turn Off All ===')
    cp.turn_off_all()
    
    print('\n=== Final Status ===')
    cp.display_all_groups()
    
    