import Classes.Communication.Wifi
import Classes.Communication.Bluetooth
import Classes.Communication.WebPage


class Communication_sys:
    def __init__(self):
        print("Sensor class initialized!")
        self.My_WebPage = Classes.Communication.WebPage.WebPage()
        self.My_Bluetooth = Classes.Communication.Bluetooth.Bluetooth()
        self.My_Wifi = Classes.Communication.Wifi.Wifi()

    def destroy(self):
        print("Sensor destroyed!")