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
            print(f"Light {self.device_name} setup on pin 17")
            
        elif self.device_type == 'doors':
            print(f"Door {self.device_name} setup on pin 27")
            
        elif self.device_type == 'camera':
            print(f"Camera {self.device_name} setup with code: {self.camera_code}")

    def turn_on(self):
        print(f'Turning on {self.device_name}')
        self.status = 'on'
        
        if self.device_type == 'camera':
            print(f"Camera {self.device_name} started with code {self.camera_code}")
        elif self.device_type == 'lights':
            print(f"Light {self.device_name} is now ON")
        elif self.device_type == 'doors':
            print(f"Door {self.device_name} is now OPEN")

    def turn_off(self):
        print(f'Turning off {self.device_name}')
        self.status = 'off'
        
        if self.device_type == 'camera':
            print(f"Camera {self.device_name} stopped")
        elif self.device_type == 'lights':
            print(f"Light {self.device_name} is now OFF")
        elif self.device_type == 'doors':
            print(f"Door {self.device_name} is now CLOSED")
        
    def get_status(self):
        if self.status == 'on':
            return True
        else:
            return False

''' Test the code'''
print("=== Testing Devices ===")

'''Light device'''
light1 = Device('home', 'room', 'lights', 'lamp1001')
light1.turn_on()
light1.turn_off()
print()

''' Camera device with code 38'''
camera1 = Device('home', 'room', 'camera', 'camera001')
camera1.turn_on()
camera1.turn_off()
print()

''' Door device'''
door1 = Device('home', 'room', 'doors', 'door001')
door1.turn_on()
door1.turn_off()
print()

print("=== Status Check ===")
print(f"Light status: {light1.get_status()}")
print(f"Camera status: {camera1.get_status()}")
print(f"Door status: {door1.get_status()}")
