import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QGridLayout
from PyQt5.QtWidgets import QCalendarWidget, QHBoxLayout, QGroupBox, QPushButton, QSpacerItem, QSizePolicy
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from volumetricRepresentation import VolumetricRepresentation
from camMovement import CNCController
import threading


class App(QMainWindow):
    def __init__(self, volumetric_representation):
        super().__init__()
        self.setWindowTitle("Volumetric Visualization")
        self.setGeometry(100, 100, 1200, 800)

        main_widget = QWidget(self)
        self.setCentralWidget(main_widget)
        main_layout = QVBoxLayout(main_widget)
        main_layout.setSpacing(10)

        header_label = QLabel("Volumetric Visualization", self)
        header_label.setAlignment(Qt.AlignCenter)
        header_label.setFont(QFont("Arial", 20, QFont.Bold))
        main_layout.addWidget(header_label)

        content_layout = QHBoxLayout()
        content_layout.setSpacing(10)

        self.fig = volumetric_representation.fig
        self.canvas = FigureCanvas(self.fig)
        content_layout.addWidget(self.canvas, 1)

        control_panel = self.create_control_panel()
        content_layout.addLayout(control_panel, 0)

        main_layout.addLayout(content_layout)

        plant_buttons_layout = self.create_plant_buttons()  # Create plant label buttons
        main_layout.addLayout(plant_buttons_layout)

    def create_plant_buttons(self):
        plant_buttons_layout = QHBoxLayout()
        plant_buttons_layout.setAlignment(Qt.AlignLeft)
        plant_buttons_layout.setSpacing(20)

        for i in range(1, 7):
            plant_button = QPushButton(f"Plant {i}")
            plant_button.setMinimumSize(125, 20)  # Adjust the height as needed
            plant_buttons_layout.addWidget(plant_button)

        return plant_buttons_layout


    def create_control_panel(self):
        control_panel_layout = QVBoxLayout()
        control_panel_layout.setAlignment(Qt.AlignTop)
        control_panel_layout.setSpacing(5)

        status_group = QGroupBox("System Status")
        status_layout = QVBoxLayout(status_group)
        self.status_label = QLabel("Status: Ready")
        self.status_label.setAlignment(Qt.AlignCenter)
        status_layout.addWidget(self.status_label)
        control_panel_layout.addWidget(status_group)

        self.calendar = QCalendarWidget()
        control_panel_layout.addWidget(self.calendar)

        sensor_data_group = QGroupBox("Sensor Data")
        sensor_data_layout = QVBoxLayout(sensor_data_group)
        self.sensor_data_date_label = QLabel("Select a date to view sensor data")
        self.sensor_data_date_label.setAlignment(Qt.AlignCenter)
        self.sensor_data_date_label.setStyleSheet("QLabel { margin-bottom: 20px; }")
        sensor_data_layout.addWidget(self.sensor_data_date_label)

        # Display all sensor data without buttons
        self.sensors = ["Nutrient Content", "Water Temperature", "EC Level", "Ambient Temperature", "pH Level"]
        self.sensor_labels = {}
        for sensor in self.sensors:
            sensor_label = QLabel(f"{sensor}: No data available")
            sensor_label.setStyleSheet("QLabel { margin-bottom: 30px; }")  # Add bottom margin
            sensor_data_layout.addWidget(sensor_label)
            self.sensor_labels[sensor] = sensor_label

        # Add spacer to fill remaining space
        spacer_item = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        sensor_data_layout.addItem(spacer_item)

        control_panel_layout.addWidget(sensor_data_group)

        return control_panel_layout

    # def run_servo_motors(self):
    #     threading.Thread(target=self.run_cnc_operations).start()

    # def run_cnc_operations(self):
    #     try:
    #         self.cnc_controller = CNCController(port='COM1')
    #         self.cnc_controller.connect()
    #         self.cnc_controller.home()
    #         self.cnc_controller.setup()

    #         self.update_status("Status: Running...")

    #         self.cnc_controller.automate_camera_movement(step_size=0.2)

    #         self.update_status("Status: Movement completed.")
    #     except Exception as e:
    #         self.update_status(f"Status: Error - {e}")

    # def update_status(self, status):
    #     self.status_label.setText(status)
    #     if "Error" in status:
    #         self.status_label.setStyleSheet("QLabel { color : red; }")
    #     else:
    #         self.status_label.setStyleSheet("QLabel { color : black; }")

    # # Add a method to update sensor data
    # def update_sensor_data(self, sensor_data):
    #     for sensor, value in sensor_data.items():
    #         self.sensor_labels[sensor].setText(f"{sensor}: {value}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    volumetric_representation = VolumetricRepresentation(r"C:\Users\Group N - II\Desktop\VFARM-GUI\imagesAttendance\volumetric_representation.png")  # Placeholder for actual usage
    window = App(volumetric_representation)
    window.show()
    sys.exit(app.exec_())
