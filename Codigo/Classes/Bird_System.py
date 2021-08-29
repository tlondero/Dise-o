
#from Memory import Memory
import Classes.Charger
import Classes.Sensor.Sensor
import Classes.Communication.Communication
import Classes.Memory
import Classes.Timer
from datetime import datetime

import matplotlib.pyplot as plt
import matplotlib.image as mpimg


class Bird_system:
    def __init__(self):
        print("System class initialized!")
        self.My_Charger = Classes.Charger.Charger()
        self.My_sensors = Classes.Sensor.Sensor.Sensor()
        self.My_Communication = Classes.Communication.Communication.Communication_sys()
        self.My_Memory = Classes.Memory.Memory()
        self.My_Timer = Classes.Timer.PerpetualTimer(60*20, self.sensors_callback)
        self.My_Timer.start()

    def sensors_callback(self):
        # datetime object containing current date and time
        now = datetime.now()
        # dd/mm/YY H:M:S
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

        [hum,temp] = self.My_sensors.Temperature_and_humidity_sensor.get_measurements()
        light = self.My_sensors.Light_sensor.get_measurements()


        img = mpimg.imread('d8535b9e-d382-4173-b241-f694e3f2d6f9.jpg')
        imgplot = plt.imshow(img)
        print(f"Humidity: {hum}")
        print(f"Temp: {temp}")
        print(f"Light level: {light}")
        print("Medition aquired at date and time =", dt_string)
        plt.show()


