import serial
import time

class CNCController:
    def __init__(self, port='COM1', baud_rate=115200, timeout=1):
        self.ser = serial.Serial(port, baud_rate, timeout=timeout)

    def connect(self):
        time.sleep(2)  # Wait for the connection to establish
        print("Connected to CNC machine.")

    def home(self):
        self.ser.write(b"$H\n")
        time.sleep(5)  # Wait for homing to complete
        print("CNC machine homed.")

    def setup(self):
        self.ser.write(b"G21\n")  # Set units to millimeters
        self.ser.write(b"G91\n")  # Set to relative positioning
        self.ser.write(b"F500\n")  # Set feed rate to 100 mm/min
        self.ser.write(b"G0 X0 Y0\n")  # Move to the starting position
        print("CNC machine set up.")

    def move(self, direction, distance):
        command = f"G0 {direction}{distance}\n"
        try:
            self.ser.write(command.encode())
            print(f"Moved {direction} by {distance} mm.")
        except serial.SerialException as e:
            print(f"Serial communication error: {e}")

    def automate_camera_movement(self, step_size):
        try:
            # Move up in steps
            self.move_in_steps('Y', 28, step_size=0.5)
            time.sleep(5)  # Pause for 5 seconds

            # Move left in steps
            self.move_in_steps('X', 3, step_size=1)
            time.sleep(5)  # Pause for 5 seconds

            # Move right in steps
            self.move_in_steps('X', 3, step_size=1)
            time.sleep(5)  # Pause for 5 seconds


            # Move down in steps
            self.move_in_steps('Y', -10, step_size=0.5)
            time.sleep(5)  # Pause for 5 seconds

            # Move down in steps
            self.move_in_steps('X', -3, step_size=1)
            time.sleep(5)  # Pause for 5 seconds

            # Move down in steps
            self.move_in_steps('X', -3, step_size=1)
            time.sleep(5)  # Pause for 5 seconds


        except KeyboardInterrupt:
            print("Movement interrupted by the user.")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.disconnect()

    def move_in_steps(self, axis, distance, step_size):
        steps = int(abs(distance) / step_size)
        direction = -1 if distance < 0 else 1
        for _ in range(steps):
            self.move(axis, direction * step_size)
            time.sleep(0.2)  # Pause for 0.2 seconds

    def disconnect(self):
        self.ser.write(b"$X\n")  # Kill alarm lock if any
        self.ser.write(b"G0 X0\n")  # Move back to the origin
        print("Disconnected from CNC machine.")
        self.ser.close()

