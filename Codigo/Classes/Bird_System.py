
#from Memory import Memory
import Classes.Charger
import Classes.Sensor.Sensor
import Classes.Communication.Communication
import Classes.Memory

class Bird_system:
    def __init__(self):
        print("System class initialized!")
        self.My_Charger = Classes.Charger.Charger()
        self.My_sensors = Classes.Sensor.Sensor.Sensor()
        self.My_Communication = Classes.Communication.Communication.Communication_sys()
        self.My_Memory = Classes.Memory.Memory()






