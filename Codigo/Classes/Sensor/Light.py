class Light:
    def __init__(self):
        print("Light class initialized!")
        self.light_measured= 15

    def get_measurements(self):
        self.light_measured+=1
        return self.light_measured

    def destroy(self):
        print("Light and Temperature destroyed!")
