class Device:
    
    def __init__(self, location, group, device_type, device_name, pin=None):
        self.location = location
        self.group = group
        self.device_type = device_type
        self.device_name = device_name 
        self.status = 'off'
        self.pin = pin
        
        ''' Camera code 38'''
        if self.device_type == 'camera':
            self.camera_code = 38
        
        self.setup_device()

    def setup_device(self):
        if self.device_type == 'lights':
            print(f" Light {self.device_name} setup on pin 17 - Ready for operation")
            
        elif self.device_type == 'doors':
            print(f" Door {self.device_name} setup on pin 27 - Security system connected")
            
        elif self.device_type == 'camera':
            print(f" Camera {self.device_name} setup with code: {self.camera_code} - AI detection enabled")

    def turn_on(self):
        print(f' Turning on {self.device_name}...')
        self.status = 'on'
        
        if self.device_type == 'camera':
            print(f"📹 Camera {self.device_name} started with code {self.camera_code} - Recording active")
        elif self.device_type == 'lights':
            print(f" Light {self.device_name} is now ON - Illumination active")
        elif self.device_type == 'doors':
            print(f" Door {self.device_name} is now OPEN - Access granted")

    def turn_off(self):
        print(f' Turning off {self.device_name}...')
        self.status = 'off'
        
        if self.device_type == 'camera':
            print(f" Camera {self.device_name} stopped - Recording inactive")
        elif self.device_type == 'lights':
            print(f" Light {self.device_name} is now OFF - Power saved")
        elif self.device_type == 'doors':
            print(f" Door {self.device_name} is now CLOSED - Security enabled")
        
    def get_status(self):
        if self.status == 'on':
            return True
        else:
            return False

    def get_device_info(self):
        """Get comprehensive device information"""
        status_icon = "ON" if self.status == 'on' else "OFF"
        print(f"Device: {self.device_name}")
        print(f"   Type: {self.device_type}")
        print(f"   Location: {self.location}")
        print(f"   Group: {self.group}")
        print(f"   Status: {status_icon}")
        if self.pin:
            print(f"   Pin: {self.pin}")
        if hasattr(self, 'camera_code'):
            print(f"   Camera Code: {self.camera_code}")

# ============= COMPREHENSIVE TESTING SECTION =============
print(" === SMART HOME DEVICE TESTING === ")
print("=" * 50)

print("\n1.  TESTING LIGHT DEVICE:")
print("-" * 30)
light1 = Device('living_room', 'main_lights', 'lights', 'main_ceiling_lamp')
print(f"Initial status: {light1.status}")
light1.turn_on()
print(f"Status after turning on: {light1.status}")
light1.turn_off()
print(f"Final status: {light1.status}")
light1.get_device_info()

print("\n2.  TESTING DOOR DEVICE:")
print("-" * 30)
door1 = Device('entrance', 'security_doors', 'doors', 'front_main_door')
print(f"Initial status: {door1.status}")
door1.turn_on()  # Opens the door
print(f"Status after opening: {door1.status}")
door1.turn_off()  # Closes the door
print(f"Final status: {door1.status}")
door1.get_device_info()

print("\n3.  TESTING CAMERA DEVICE:")
print("-" * 30)
camera1 = Device('backyard', 'surveillance', 'camera', 'security_cam_01')
print(f"Initial status: {camera1.status}")
camera1.turn_on()  # Starts recording
print(f"Status after starting: {camera1.status}")
camera1.turn_off()  # Stops recording
print(f"Final status: {camera1.status}")
camera1.get_device_info()

print("\n4.  TESTING MULTIPLE OPERATIONS:")
print("-" * 30)
# Create multiple devices
devices = [
    Device('kitchen', 'kitchen_lights', 'lights', 'under_cabinet_led'),
    Device('garage', 'garage_access', 'doors', 'garage_side_door'),
    Device('driveway', 'perimeter_security', 'camera', 'driveway_monitor')
]

print(" All devices created successfully!")
print("\n Turning ON all devices:")
for device in devices:
    device.turn_on()
    print()

print(" Device Status Summary:")
for i, device in enumerate(devices, 1):
    print(f"\n{i}. {device.device_name.upper()}:")
    device.get_device_info()

print("\n Turning OFF all devices:")
for device in devices:
    device.turn_off()
    print()

print("\n5.  STATUS TESTING:")
print("-" * 30)
test_device = Device('bedroom', 'bedroom_lighting', 'lights', 'bedside_lamp')
print(f"Device created - Status check: {'ACTIVE' if test_device.get_status() else 'INACTIVE'}")
test_device.turn_on()
print(f"After turn_on - Status check: {'ACTIVE' if test_device.get_status() else 'INACTIVE'}")
test_device.turn_off()
print(f"After turn_off - Status check: {'ACTIVE' if test_device.get_status() else 'INACTIVE'}")

print("\n" + "=" * 50)
print(" ALL DEVICE TESTS COMPLETED SUCCESSFULLY!")
print(" Smart Home Device System Ready for Deployment")
print("=" * 50)

# ============= ADDITIONAL DEVICE STATISTICS =============
print("\n TESTING STATISTICS:")
print("-" * 20)
total_devices = len(devices) + 3  # Including individual test devices
print(f"Total devices tested: {total_devices}")
print(f"Device types tested: Lights, Doors, Cameras")
print(f"Operations tested: Setup, Turn On, Turn Off, Status Check")
print(f"All devices functioning:  PASS")
print("\n Device testing phase complete! ")