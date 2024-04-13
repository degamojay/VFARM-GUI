import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QGridLayout
from PyQt5.QtWidgets import QCalendarWidget, QHBoxLayout, QGroupBox, QPushButton, QSpacerItem, QSizePolicy
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from application_logic import ApplicationLogic
from volumetricRepresentation import VolumetricRepresentation


class App(QMainWindow):
    def __init__(self, application_logic):
        super().__init__()
        self.application_logic = application_logic
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

        self.fig = VolumetricRepresentation(image_path=r"C:\Users\Group N - II\Desktop\VFARM-GUI\imagesAttendance\volumetric_representation.png").fig
        if self.fig is None:  # Check if fig is None
                no_data_label = QLabel("No Data Yet")
                no_data_label.setAlignment(Qt.AlignCenter)
                content_layout.addWidget(no_data_label)
        else:
                self.canvas = FigureCanvas(self.fig)
                content_layout.addWidget(self.canvas, 1)

        control_panel = self.create_control_panel()
        content_layout.addLayout(control_panel)

        self.plant_label = QLabel(self.get_plant_label_text())
        self.plant_label.setAlignment(Qt.AlignCenter)
        self.plant_label.setFont(QFont("Arial", 16))  # Set the font size to 16
        main_layout.addWidget(self.plant_label)

        main_layout.addLayout(content_layout)

        plant_buttons_layout = self.create_plant_buttons()  # Create plant label buttons
        main_layout.addLayout(plant_buttons_layout)

    def get_plant_label_text(self):
        return f"Plant {self.application_logic.get_selected_plant()}"

    def create_plant_buttons(self):
        plant_buttons_layout = QHBoxLayout()
        plant_buttons_layout.setAlignment(Qt.AlignLeft)
        plant_buttons_layout.setSpacing(20)

        self.plant_buttons = []

        for i in range(1, 7):
            plant_button = QPushButton(f"Plant {i}")
            plant_button.setMinimumSize(125, 20)  # Adjust the height as needed
            plant_button.clicked.connect(lambda checked, plant=i: self.on_plant_button_clicked(plant))
            plant_buttons_layout.addWidget(plant_button)
            self.plant_buttons.append(plant_button)

        return plant_buttons_layout

    def on_plant_button_clicked(self, plant):
        self.application_logic.set_selected_plant(plant)
        self.plant_label.setText(self.get_plant_label_text())

    def create_control_panel(self):
        control_panel_layout = QVBoxLayout()
        control_panel_layout.setAlignment(Qt.AlignTop)
        control_panel_layout.setSpacing(5)

        status_group = QGroupBox("System Status")
        status_layout = QVBoxLayout(status_group)
        self.status_label = QLabel(self.application_logic.get_status())
        self.status_label.setAlignment(Qt.AlignCenter)
        font = self.status_label.font()
        font.setPointSize(10)  # Set font size to 12
        self.status_label.setFont(font)
        status_layout.addWidget(self.status_label)
        control_panel_layout.addWidget(status_group)

        self.calendar = QCalendarWidget()
        control_panel_layout.addWidget(self.calendar)

        sensor_data_group = QGroupBox("Sensor Data")
        sensor_data_layout = QVBoxLayout(sensor_data_group)
        self.sensor_data_labels = {}

        for sensor, data in self.application_logic.get_sensor_data().items():
            sensor_label = QLabel(f"{sensor}: {data}")
            sensor_label.setStyleSheet("QLabel { margin-bottom: 30px; }")  # Add bottom margin
            font = sensor_label.font()
            font.setPointSize(10)  # Set font size to 12
            sensor_label.setFont(font)
            sensor_data_layout.addWidget(sensor_label)
            self.sensor_data_labels[sensor] = sensor_label

        # Add spacer to fill remaining space
        spacer_item = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        sensor_data_layout.addItem(spacer_item)

        control_panel_layout.addWidget(sensor_data_group)

        return control_panel_layout


if __name__ == "__main__":
    app_logic = ApplicationLogic()
    app = QApplication(sys.argv)
    window = App(app_logic)
    window.show()
    sys.exit(app.exec_())
