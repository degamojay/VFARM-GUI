import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel
from PyQt5.QtWidgets import QPushButton, QCalendarWidget, QHBoxLayout, QGroupBox
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
        self.setGeometry(100, 100, 1200, 800)

        main_widget = QWidget(self)
        self.setCentralWidget(main_widget)
        main_layout = QVBoxLayout(main_widget)
        main_layout.setSpacing(10)

        header_label = QLabel("Volumetric Visualization", self)
        header_label.setAlignment(Qt.AlignCenter)
        header_label.setFont(QFont("Arial", 20, QFont.Bold))
        main_layout.addWidget(header_label)

        # Horizontal layout for canvas and controls
        content_layout = QHBoxLayout()
        content_layout.setSpacing(10)

        # Enlarging and adding the figure to the left side
        self.fig = volumetric_representation.fig
        self.canvas = FigureCanvas(self.fig)
        content_layout.addWidget(self.canvas, 1)

        # Control panel on the right side
        control_panel = self.create_control_panel()
        content_layout.addLayout(control_panel, 0)

        main_layout.addLayout(content_layout)

        # Dictionary to store sensor data
        self.sensor_data = {
            "Nutrient Content": "2",
            "Water Temperature": "2",
            "EC Level": "2",
            "Ambient Temperature": "2",
            "pH Level": "2"
        }

        self.display_sensor_data()

    def create_control_panel(self):
        control_panel_layout = QVBoxLayout()
        control_panel_layout.setAlignment(Qt.AlignTop)
        control_panel_layout.setSpacing(5)

        # Status label within a group box for clarity
        status_group = QGroupBox("System Status")
        status_layout = QVBoxLayout(status_group)
        self.status_label = QLabel("Status: Ready")
        self.status_label.setAlignment(Qt.AlignCenter)
        status_layout.addWidget(self.status_label)
        control_panel_layout.addWidget(status_group)

        # Calendar widget
        self.calendar = QCalendarWidget()
        control_panel_layout.addWidget(self.calendar)

        # Sensor data display
        sensor_data_group = QGroupBox("Sensor Data")
        sensor_data_layout = QVBoxLayout(sensor_data_group)
        self.sensor_data_date_label = QLabel("Select a date to view sensor data")
        self.sensor_data_date_label.setAlignment(Qt.AlignCenter)
        sensor_data_layout.addWidget(self.sensor_data_date_label)

        self.sensor_data_label = QLabel("")
        self.sensor_data_label.setAlignment(Qt.AlignCenter)
        sensor_data_layout.addWidget(self.sensor_data_label)
        control_panel_layout.addWidget(sensor_data_group)

        # Buttons for sensor data
        self.create_sensor_buttons(control_panel_layout)

        # Run Servo Motors button
        run_servo_button = QPushButton("Run Servo Motors")
        run_servo_button.clicked.connect(self.run_servo_motors)
        control_panel_layout.addWidget(run_servo_button)

        return control_panel_layout

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
        # Optionally change the font color to red for errors
        if "Error" in status:
            self.status_label.setStyleSheet("QLabel { color : red; }")
        else:
            self.status_label.setStyleSheet("QLabel { color : black; }")


    def display_sensor_data(self, sensor_name=None):
        """
        Update the display with new data for a specific sensor, if provided,
        or for all sensors otherwise.
        """
        if sensor_name:
            # Imagine get_sensor_data is a function that fetches the latest data for a given sensor.
            # You would need to implement this function based on your actual data retrieval logic.
            self.sensor_data[sensor_name] = self.get_sensor_data(sensor_name)
        
        sensor_data_text = ""
        for sensor, data in self.sensor_data.items():
            sensor_data_text += f"{sensor}: {data}\n"
        self.sensor_data_label.setText(sensor_data_text)


    def display_date_sensor_data(self):
        selected_date = self.calendar.selectedDate()
        formatted_date = selected_date.toString("yyyy-MM-dd")
        self.sensor_data_date_label.setText(f"Sensor Data for {formatted_date}")

        # Fetch and display sensor data for `formatted_date`
        # This is a placeholder; you'll need to integrate with your actual data source
        sensor_data = "Example Data: 123"
        self.sensor_data_label.setText(f"Data for {formatted_date}: {sensor_data}")


if __name__ == "__main__":
    # Example usage
    app = QApplication(sys.argv)
    volumetric_representation = VolumetricRepresentation(r"C:\Users\Jay Degamo\Desktop\VFARM-GUI\imagesAttendance\volumetric_representation.png")  # Placeholder for actual usage
    window = App(volumetric_representation)
    window.show()
    sys.exit(app.exec_())
