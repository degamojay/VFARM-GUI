import mysql.connector
from PyQt5.QtCore import QObject, pyqtSignal
from sensorData import SensorDataThread
import random


class ApplicationLogic(QObject):
    data_updated = pyqtSignal(dict)

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
        self.update_sensor_data_from_db()

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
            self.data_updated.emit(self.sensor_data)
        except ValueError:
            print("Invalid data format received:", data)

    def update_sensor_data_from_db(self):
        # Mock sensor data instead of fetching from the database
        amb_temp = random.uniform(20, 30)  # Example: Ambient temperature between 20 and 30
        water_temp = random.uniform(15, 25)  # Example: Water temperature between 15 and 25
        ph_value = random.uniform(5.5, 6.5)  # Example: pH level between 5.5 and 6.5
        ec_value = random.uniform(0.8, 1.2)  # Example: EC level between 0.8 and 1.2
        
        # Update the sensor data in the application logic
        self.sensor_data["Ambient Temperature"] = amb_temp
        self.sensor_data["Water Temperature"] = water_temp
        self.sensor_data["pH Level"] = ph_value
        self.sensor_data["EC Level"] = ec_value
        self.data_updated.emit(self.sensor_data)

    # def update_sensor_data_from_db(self):
    #     try:
    #         # Connect to MySQL database
    #         mydb = mysql.connector.connect(
    #             host="192.168.56.1",
    #             user="root",
    #             password="Thnksfrthmmrs1234!#",
    #             database="data_collection"
    #         )
    #         mycursor = mydb.cursor()

    #         # Fetch the latest sensor data from the database
    #         mycursor.execute("SELECT amb_temp, water_temp, ph_value, ec_value FROM sensor_data ORDER BY timestamp DESC LIMIT 1")
    #         data = mycursor.fetchone()

    #         # Update the sensor data in the application logic
    #         if data:
    #             amb_temp, water_temp, ph_value, ec_value = data
    #             self.sensor_data["Ambient Temperature"] = amb_temp
    #             self.sensor_data["Water Temperature"] = water_temp
    #             self.sensor_data["pH Level"] = ph_value
    #             self.sensor_data["EC Level"] = ec_value
    #             self.data_updated.emit(self.sensor_data)
    #         else:
    #             print("No sensor data found in the database.")
    #     except mysql.connector.Error as e:
    #         print("MySQL error:", e)
    #     finally:
    #         # Close the database connection
    #         if mycursor:
    #             mycursor.close()
    #         if mydb:
    #             mydb.close()

    def get_sensor_data(self):
        return self.sensor_data

    def get_status(self):
        return self.status

    def get_selected_plant(self):
        return self.selected_plant

    def set_selected_plant(self, plant):
        self.selected_plant = plant
