from view import View
from paho.mqtt import client as mqtt_client

class Controller:
    def __init__(self):
        self.view = View()

        self.view.b1_btn['command'] = self.trigger_button_1
        self.view.b2_btn['command'] = self.trigger_button_2
        self.view.b3_btn['command'] = self.trigger_button_3
        self.view.send_btn['command'] = self.trigger_send

        self.setup_mqtt()


    def setup_mqtt(self):
        pass
        

    def trigger_button_1(self):
        pass


    def trigger_button_2(self):
        pass


    def trigger_button_3(self):
        pass


    def trigger_send(self):
        pass


    def start_app(self):
        self.view.init_window()


def main():
    controller = Controller()
    controller.start_app()

if __name__ == "__main__":
    main()