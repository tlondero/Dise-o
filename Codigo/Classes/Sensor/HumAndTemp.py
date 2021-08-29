class HumAndTemp:
    def __init__(self):
        print("Humidity and Temperature class initialized!")
        self.Humidity = 71
        self.Temperature = 20

    def get_measurements(self):
        self.Humidity += 1
        self.Temperature += 1
        return [self.Humidity, self.Temperature]#First humidity the second Temperature

    def destroy(self):
        print("Humidity and Temperature destroyed!")

