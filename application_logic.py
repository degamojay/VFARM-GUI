from PyQt5.QtCore import QObject
from sensorData import SensorDataThread

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
        self.sensor_thread = SensorDataThread()
        self.sensor_thread.data_updated.connect(self.update_sensor_data)

    def start_collecting_data(self):
        self.sensor_thread.start()

    def stop_collecting_data(self):
        self.sensor_thread.quit()

    def update_status(self, status):
        self.status = status

    def update_sensor_data(self, data):
        # Parse data and update application logic
        values = data.split(",")
        try:
            amb_temp, water_temp, ph_value, ec_value, lux_top, lux_bot = map(float, values)
            self.sensor_data["Ambient Temperature"] = amb_temp
            self.sensor_data["Water Temperature"] = water_temp
            self.sensor_data["pH Level"] = ph_value
            self.sensor_data["EC Level"] = ec_value
        except ValueError:
            print("Invalid data format received:", data)


    def get_sensor_data(self):
        return self.sensor_data

    def get_status(self):
        return self.status

    def get_selected_plant(self):
        return self.selected_plant

    def set_selected_plant(self, plant):
        self.selected_plant = plant
