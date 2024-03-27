import sys
import sqlite3
import threading
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel
from matplotlib.backend_bases import FigureCanvasBase
from volumetricRepresentation import VolumetricRepresentation
from camMovement import CNCController
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Volumetric Representation")
        MainWindow.resize(1200, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(50, 630, 461, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(730, 450, 431, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(660, 520, 501, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(660, 610, 501, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(50, 580, 461, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(660, 490, 501, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(660, 580, 501, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(50, 530, 461, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(50, 480, 461, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(660, 550, 501, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(50, 430, 461, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(0, 10, 1201, 71))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarWidget.setGeometry(QtCore.QRect(50, 90, 461, 281))
        self.calendarWidget.setObjectName("calendarWidget")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(50, 690, 1111, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Volumetric Representation"))
        self.pushButton_3.setText(_translate("MainWindow", "EC Level"))
        self.label_6.setText(_translate("MainWindow", "DATA for MM/DD/YY"))
        self.label_2.setText(_translate("MainWindow", "Water Temperature:"))
        self.label_5.setText(_translate("MainWindow", "EC Level:"))
        self.pushButton_5.setText(_translate("MainWindow", "pH Level"))
        self.label.setText(_translate("MainWindow", "Nutrient Content: "))
        self.label_4.setText(_translate("MainWindow", "pH Level:"))
        self.pushButton_4.setText(_translate("MainWindow", "Ambient Temperature"))
        self.pushButton_2.setText(_translate("MainWindow", "Water Temperature"))
        self.label_3.setText(_translate("MainWindow", "Ambient Temperature:"))
        self.pushButton.setText(_translate("MainWindow", "Nutrient Content"))
        self.label_7.setText(_translate("MainWindow", "Volumetric Representation"))
        self.pushButton_6.setText(_translate("MainWindow", "Run Servo Motors"))
        self.pushButton_6.clicked.connect(self.run_servo_motors)
        self.statusLabel = QtWidgets.QLabel(self.centralwidget)
        self.statusLabel.setGeometry(QtCore.QRect(50, 740, 1111, 30))  # Adjust the geometry as needed
        font = QtGui.QFont()
        font.setPointSize(14)
        self.statusLabel.setFont(font)
        self.statusLabel.setObjectName("statusLabel")
        self.statusLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.statusLabel.setText("Status: Idle")
        # Initialize volumetric representation with a placeholder image path or the actual image path
        lettuce_image_path = r"C:\Users\Jay Degamo\Desktop\VFARM-GUI\imagesAttendance\volumetric_representation.png"
        self.volumetric_representation = VolumetricRepresentation(lettuce_image_path)

        # Use FigureCanvas to embed the matplotlib figure in the PyQt5 application
        self.figure_canvas = FigureCanvas(self.volumetric_representation.fig)
        self.figure_canvas.setParent(self.centralwidget)  # Set the parent widget
        self.figure_canvas.setGeometry(660, 90, 461, 281)
        self.init_db()  # Initialize the database

    def init_db(self):
        self.conn = sqlite3.connect('sensor_data.db')
        c = self.conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS sensor_data (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        sensor_name TEXT NOT NULL,
                        data_value TEXT NOT NULL,
                        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                     )''')
        self.conn.commit()

    def display_sensor_data(self, sensor):
        c = self.conn.cursor()
        c.execute("SELECT data_value FROM sensor_data WHERE sensor_name=? ORDER BY timestamp DESC LIMIT 1", (sensor,))
        result = c.fetchone()
        sensor_data = f"Data for {sensor}: {result[0] if result else 'No data available'}"
        # Assuming self.label_6 is the QLabel for displaying sensor data:
        self.label_6.setText(sensor_data)

    def run_servo_motors(self):
        self.statusLabel.setText("Status: Initializing...")  # Update label text
        threading.Thread(target=self.run_cnc_operations).start()

    def run_cnc_operations(self):
        try:
            self.cnc_controller = CNCController(port='COM1')
            self.cnc_controller.connect()
            self.cnc_controller.home()
            self.cnc_controller.setup()

            # Assuming you want to update the UI from this thread, use signals or a thread-safe method
            # This is a placeholder for setting text safely from another thread
            self.update_status("Status: Running...")

            self.cnc_controller.automate_camera_movement(step_size=0.2)

            # Update status upon completion
            self.update_status("Status: Movement completed.")
        except Exception as e:
            self.update_status(f"Error: {str(e)}")

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
