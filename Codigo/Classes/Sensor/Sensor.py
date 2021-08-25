import Classes.Sensor.HumAndTemp
import Classes.Sensor.Camera
import Classes.Sensor.Light


class Sensor:
    def __init__(self):
        print("Sensor class initialized!")
        self.Temperature_and_humidity_sensor = Classes.Sensor.HumAndTemp.HumAndTemp()
        self.Light_sensor = Classes.Sensor.Light.Light()
        self.Camera_sensor = Classes.Sensor.Camera.Camera()

    def destroy(self):
        print("Sensor destroyed!")
