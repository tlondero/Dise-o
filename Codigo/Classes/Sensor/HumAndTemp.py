import board
import adafruit_dht
dhtDevice = adafruit_dht.DHT22(board.D4, use_pulseio=False)
#The D4 is the pin

# Initial the dht device, with data pin connected to:
# dhtDevice = adafruit_dht.DHT22(board.D18)
# you can pass DHT22 use_pulseio=False if you wouldn't like to use pulseio.
# This may be necessary on a Linux single board computer like the Raspberry Pi,
# but it will not work in CircuitPython.
class HumAndTemp:
    def __init__(self):
        print("Humidity and Temperature class initialized!")
        self.Humidity = 71
        self.Temperature = 20

    def get_measurements(self):
        try:
            self.Humidity = dhtDevice.humidity
            self.Temperature = dhtDevice.temperature
            print(
                "Temp: {:.1f} C    Humidity: {}% ".format(
                    self.Temperature, self.Humidity
                )
            )
        except RuntimeError as error:
           print(error.args[0])
        return [self.Humidity, self.Temperature]#First humidity the second Temperature

    def destroy(self):
        print("Humidity and Temperature destroyed!")
        dhtDevice.exit()

