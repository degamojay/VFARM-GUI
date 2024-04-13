from PyQt5.QtCore import QObject

class ApplicationLogic(QObject):
    def __init__(self):
        super().__init__()
        self.status = "Ready"
        self.selected_plant = 1
        self.sensor_data = {
            "Nutrient Content": "No data available",
            "Water Temperature": "No data available",
            "EC Level": "No data available",
            "Ambient Temperature": "No data available",
            "pH Level": "No data available"
        }

    def update_status(self, status):
        self.status = status

    def update_sensor_data(self, sensor, data):
        if sensor in self.sensor_data:
            self.sensor_data[sensor] = data

    def get_sensor_data(self):
        return self.sensor_data

    def get_status(self):
        return self.status

    def get_selected_plant(self):
        return self.selected_plant

    def set_selected_plant(self, plant):
        self.selected_plant = plant
