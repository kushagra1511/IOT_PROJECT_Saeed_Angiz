import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO  

class Device:
    
    def __init__(self,location,group,device_type,device_name,pin):
        self.location=location
        self.group=group
        self.device_type=device_type
        self.device_name=device_name 
        self.status='off'
        
        #sherkat dade beman
        self.mqtt_broker='jasdhash'
        self.port=37362  
        
        #on dastgahe pini --> 
        self.mqtt_client=pin
        
        # Camera code 38 support
        if self.device_type=='camera':
            self.camera_code=38
            print(f'Status: Camera {self.device_name} initialized with code {self.camera_code}')
        
        print(f'Status: Device {self.device_name} created at {self.location} in {self.group}')
        
        self.connect_mqtt()
        self.setup_gpio()

    def connect_mqtt(self):
        mqtt.connect(self.mqtt_broker,self.port)
        print(f'Status: MQTT connected to {self.mqtt_broker}:{self.port}')
        
    def setup_gpio(self):
        if self.device_type=='lights':
            GPIO.setup(17,GPIO.OUT)
            print(f'Status: Light {self.device_name} setup on GPIO pin 17')
            
        elif self.device_type=='doors':
            GPIO.setup(27,GPIO.OUT)
            print(f'Status: Door {self.device_name} setup on GPIO pin 27')
            
        elif self.device_type=='camera':
            print(f'Status: Camera {self.device_name} setup completed with code {self.camera_code}')

    def turn_on(self):
        print('Done!!!')
        self.status='on'
        print(f'Status: {self.device_name} is now ON')
        #oon devicer --> SHERKAT vasl bshe --> dastoopr bde --> sherkate b oon lampe vasl bshe
        #va oon lamp baram 'ROSHAN' kone
        
        if self.device_type=='camera':
            print(f'Status: Camera {self.device_name} started recording with code {self.camera_code}')
        elif self.device_type=='lights':
            GPIO.output(17,True)
            print(f'Status: Light {self.device_name} GPIO 17 activated')
        elif self.device_type=='doors':
            GPIO.output(27,True)
            print(f'Status: Door {self.device_name} GPIO 27 activated - OPEN')
            
        mqtt.publish(self.mqtt_client,self.device_name,'TURN ON')
        print(f'Status: MQTT message sent - {self.device_name} TURN ON')

    def turn_off(self):
        print('off')
        self.status='off'
        print(f'Status: {self.device_name} is now OFF')
        #bayad inja bnvis-->sherkate begam agah in device 
        #shekrat elamp --> 'Khamoosh' kone
        
        if self.device_type=='camera':
            print(f'Status: Camera {self.device_name} stopped recording')
        elif self.device_type=='lights':
            GPIO.output(17,False)
            print(f'Status: Light {self.device_name} GPIO 17 deactivated')
        elif self.device_type=='doors':
            GPIO.output(27,False)
            print(f'Status: Door {self.device_name} GPIO 27 deactivated - CLOSED')
            
        mqtt.publish(self.mqtt_client,self.device_name,'TURN OFF')
        print(f'Status: MQTT message sent - {self.device_name} TURN OFF')
        
    def get_status(self):
        if self.status=='on':
            print(f'Status: {self.device_name} is currently ON')
            return True
        else:
            print(f'Status: {self.device_name} is currently OFF')
            return False
        
#a1=..... (class --> device az tarighe ketabkhone)

a1=Device('home','room','lights','lamps1001','w328376231863816326216')
a1.turn_on()
a1.turn_off()

# Camera test with code 38
camera1=Device('home','room','camera','camera001','cam123')
camera1.turn_on()
camera1.turn_off()
print(f'Camera status: {camera1.get_status()}')



class Sensor:
    
    def __init__(self,location,group,sensor_name,sensor_type,pin):
        self.location=location
        self.group=group
        self.sensor_name=sensor_name
        self.sensor_type=sensor_type
        self.pin=pin
        print(f'Status: Sensor {self.sensor_name} created at {self.location}')
        
        
a1=Sensor('hom','room1','temp','thermoset10','2823shasjash')

print(f'Sensor location: {a1.location}')
print(f'Sensor pin: {a1.pin}')


#a1.turn_on()

#**things -_> device / sensor
#devcie -->dastoor turn on , off


#sensor--> damaor , begiri data -->: read_data()


    
import Adafruit_DHT   
    
class Sensor:
    
    def __init__(self,location,group,sensor_name,sensor_type,pin):
        self.location=location
        self.group=group
        self.sensor_name=sensor_name
        self.sensor_type=sensor_type
        self.pin=pin
        print(f'Status: DHT Sensor {self.sensor_name} initialized')
        
        
    def read_data(self):
        humidity,temperature=Adafruit_DHT.read_retry(Adafruit_DHT.DHT22,self.pin)
        print(f'Status: Sensor {self.sensor_name} reading data')
        print(f'Temperature: {temperature}°C, Humidity: {humidity}%')
        return temperature
        
a1=Sensor('hom','room1','temp','thermoset10','2823shasjash')

temp_data = a1.read_data()      
print(f'Final temperature reading: {temp_data}°C')
