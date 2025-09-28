# Handle imports with proper error handling
try:
    import paho.mqtt.client as mqtt
    print("Status: paho.mqtt module found and imported successfully")
except ImportError:
    print("Status: paho.mqtt not found, using simulation mode")
    class mqtt:
        @staticmethod
        def connect(broker, port): print(f"MQTT: Connected to {broker}:{port}")
        @staticmethod
        def publish(client, device, message): print(f"MQTT: Published to {device}: {message}")

try:
    import RPi.GPIO as GPIO
    print("Status: RPi.GPIO module found and imported successfully")
except ImportError:
    print("Status: RPi.GPIO not found, using simulation mode")
    class GPIO:
        OUT = "OUT"
        @staticmethod
        def setup(pin, mode): print(f"GPIO: Setup pin {pin}")
        @staticmethod
        def output(pin, state): print(f"GPIO: Pin {pin} set to {state}")

try:
    import Adafruit_DHT
    print("Status: Adafruit_DHT module found and imported successfully")
except ImportError:
    print("Status: Adafruit_DHT not found, using simulation mode")
    class Adafruit_DHT:
        DHT22 = "DHT22"
        @staticmethod
        def read_retry(sensor, pin):
            return 65.0, 23.5  # humidity, temperature

class Device:
    
    def __init__(self,location,group,device_type,device_name,pin):
        self.location=location
        self.group=group
        self.device_type=device_type
        self.device_name=device_name 
        self.status='off'
        
        # Camera code 38 support
        if self.device_type=='camera':
            self.camera_code=38
            print(f'Camera {self.device_name} setup with code {self.camera_code}')
        
        #sherkat dade beman
        self.mqtt_broker='jasdhash'
        self.port=37362  
        
        #on dastgahe pini --> 
        self.mqtt_client=pin
        
        self.connect_mqtt()
        self.setup_gpio()

    def connect_mqtt(self):
        mqtt.connect(self.mqtt_broker,self.port)
        
    def setup_gpio(self):
        if self.device_type=='lights':
            GPIO.setup(17,GPIO.OUT)
            
        elif self.device_type=='doors':
            GPIO.setup(27,GPIO.OUT)
            
        elif self.device_type=='camera':
            print(f'Camera {self.device_name} ready with code {self.camera_code}')

    def turn_on(self):
        print('Done!!!')
        self.status='on'
        
        if self.device_type=='camera':
            print(f'Camera {self.device_name} started with code {self.camera_code}')
        
        mqtt.publish(self.mqtt_client,self.device_name,'TURN ON')

    def turn_off(self):
        print('off')
        self.status='off'
        
        if self.device_type=='camera':
            print(f'Camera {self.device_name} stopped')
            
        mqtt.publish(self.mqtt_client,self.device_name,'TURN OFF')
        
    def get_status(self):
        if self.status=='on':
            return True
        else:
            return False
        
# Test devices
a1=Device('home','room','lights','lamps1001','w328376231863816326216')
a1.turn_on()
a1.turn_off()

# Camera with code 38
cam1=Device('home','room','camera','camera001','cam123')
cam1.turn_on()
cam1.turn_off()

class Sensor:
    
    def __init__(self,location,group,sensor_name,sensor_type,pin):
        self.location=location
        self.group=group
        self.sensor_name=sensor_name
        self.sensor_type=sensor_type
        self.pin=pin
        
a1=Sensor('hom','room1','temp','thermoset10','2823shasjash')

print(a1.location)
print(a1.pin)

class Sensor:
    
    def __init__(self,location,group,sensor_name,sensor_type,pin):
        self.location=location
        self.group=group
        self.sensor_name=sensor_name
        self.sensor_type=sensor_type
        self.pin=pin
        
    def read_data(self):
        humidity,temperature=Adafruit_DHT.read_retry(Adafruit_DHT.DHT22,self.pin)
        return temperature
        
a1=Sensor('hom','room1','temp','thermoset10','2823shasjash')
a1.read_data()
