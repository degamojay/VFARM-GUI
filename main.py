import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from volumetricRepresentation import VolumetricRepresentation
from camMovement import CNCController
import threading


class App(QMainWindow):
    def __init__(self, volumetric_representation):
        super().__init__()
        self.setWindowTitle("Volumetric Visualization")
        self.setGeometry(100, 100, 800, 600)

        main_widget = QWidget(self)
        self.setCentralWidget(main_widget)
        layout = QVBoxLayout(main_widget)

        header_label = QLabel("Volumetric Visualization", self)
        header_label.setAlignment(Qt.AlignCenter)
        header_label.setFont(QFont("Arial", 16, QFont.Bold))
        layout.addWidget(header_label)

        self.fig = volumetric_representation.fig
        self.canvas = FigureCanvas(self.fig)
        layout.addWidget(self.canvas)

        self.status_label = QLabel("Status: Ready", self)
        self.status_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.status_label)

        button_widget = QWidget(self)
        button_layout = QVBoxLayout(button_widget)
        layout.addWidget(button_widget)

        self.sensor_data_label = QLabel("", self)
        self.sensor_data_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.sensor_data_label)

        self.create_sensor_buttons(button_layout)

        run_servo_button = QPushButton("Run Servo Motors", self)
        run_servo_button.clicked.connect(self.run_servo_motors)
        layout.addWidget(run_servo_button)

    def create_sensor_buttons(self, layout):
        sensors = ["Nutrient Content", "Water Temperature", "EC Level", "Ambient Temperature", "pH Level"]

        for sensor_name in sensors:
            button = QPushButton(sensor_name, self)
            button.clicked.connect(lambda _, sensor=sensor_name: self.display_sensor_data(sensor))
            layout.addWidget(button)

    def run_servo_motors(self):
        threading.Thread(target=self.run_cnc_operations).start()

    def run_cnc_operations(self):
        try:
            self.cnc_controller = CNCController(port='COM1')
            self.cnc_controller.connect()
            self.cnc_controller.home()
            self.cnc_controller.setup()

            self.update_status("Status: Running...")

            self.cnc_controller.automate_camera_movement(step_size=0.2)

            self.update_status("Status: Movement completed.")
        except Exception as e:
            self.update_status(f"Status: Error - {e}")

    def update_status(self, status):
        self.status_label.setText(status)

    def display_sensor_data(self, sensor):
        # Add logic to fetch sensor data and display it
        sensor_data = f"Data for {sensor}: [Example Data]"
        self.sensor_data_label.setText(sensor_data)

if __name__ == "__main__":
    lettuce_image_path = r"D:\1-PythonResearch\imagesAttendance\volumetric_representation.png"
    volumetric_representation = VolumetricRepresentation(lettuce_image_path)

    app = QApplication(sys.argv)
    window = App(volumetric_representation)
    window.show()
    sys.exit(app.exec_())
