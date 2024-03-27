import cv2
import numpy as np
import time
import serial

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
        time.sleep(5)
        self.capture_and_save_images()

        # Move left in steps
        self.move_in_steps('X', 3, step_size=1)
        time.sleep(5)
        self.capture_and_save_images()

        # Move right in steps
        self.move_in_steps('X', 3, step_size=1)
        time.sleep(5)
        self.capture_and_save_images()

        # Move down in steps
        self.move_in_steps('Y', -10, step_size=0.5)
        time.sleep(5)
        self.capture_and_save_images()

        # Move down in steps
        self.move_in_steps('X', -3, step_size=1)
        time.sleep(5)
        self.capture_and_save_images()

        # Move down in steps
        self.move_in_steps('X', -3, step_size=1)
        time.sleep(5)
        self.capture_and_save_images()

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

    def capture_and_save_images(self):
        # Capture frames from both cameras
        ret1, frame1 = cam1.read()
        ret2, frame2 = cam2.read()

        # Check frames
        if not ret1 or not ret2:
            print("Failed to grab frames")
            return

        # Detect and capture red objects from frames if present
        if detect_red(frame1):
            img_name = f"red_detected_cam1_{img_counter_cam1}.png"
            cv2.imwrite(f'{path}/{img_name}', frame1)
            print(f"{img_name} written!")
            img_counter_cam1 += 1

        if detect_red(frame2):
            img_name = f"red_detected_cam2_{img_counter_cam2}.png"
            cv2.imwrite(f'{path}/{img_name}', frame2)
            print(f"{img_name} written!")
            img_counter_cam2 += 1

    def disconnect(self):
        self.ser.write(b"$X\n")  # Kill alarm lock if any
        self.ser.write(b"G0 X0\n")  # Move back to the origin
        print("Disconnected from CNC machine.")
        self.ser.close()

# Initialize cams
cam1 = cv2.VideoCapture(0)
cam2 = cv2.VideoCapture(1)

# Create windows
cv2.namedWindow("Camera 1")
cv2.namedWindow("Camera 2")

# Path directory
path = 'Captured Images'

# Track images
img_counter_cam1 = 0
img_counter_cam2 = 0

# Detect color
def detect_red(frame):
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Range of red colors
    lower_red = np.array([0, 100, 100])
    upper_red = np.array([10, 255, 255])
    mask = cv2.inRange(hsv_frame, lower_red, upper_red)

    # Find contours
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Check red
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 100:  # Minimum area to consider
            return True
    return False

while True:
    # Capture frames
    ret1, frame1 = cam1.read()
    ret2, frame2 = cam2.read()

    # Check frames
    if not ret1 or not ret2:
        print("Failed to grab frames")
        break

    # Display
    cv2.imshow("Camera 1", frame1)
    cv2.imshow("Camera 2", frame2)

    time.sleep(4)

    # Press q to break
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Close all
cam1.release()
cam2.release()
cv2.destroyAllWindows()
