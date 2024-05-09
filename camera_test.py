import cv2
import os
import re
from datetime import datetime

def next_available_index(output_folder, camera_id):
    index = 1
    current_date = datetime.now().strftime("%Y%m%d")
    base_filename = f"{current_date}_image{camera_id}_{index}.jpg"
    while os.path.exists(os.path.join(output_folder, base_filename)):
        base_filename = f"{current_date}_image{camera_id}_{index}.jpg"
        index += 1
    return base_filename

def capture_images(num_images, output_folder):
    # Access the cameras
    cap1 = cv2.VideoCapture(0)
    cap2 = cv2.VideoCapture(1)

    # Check if the cameras are opened successfully
    if not cap1.isOpened():
        print("Error: Unable to access Camera 0.")
        return

    if not cap2.isOpened():
        print("Error: Unable to access Camera 1.")
        return

    # Capture images
    count = 1
    while count <= num_images:
        ret1, frame1 = cap1.read()
        ret2, frame2 = cap2.read()

        if ret1 and ret2:
            # Save the frames as images
            image_path1 = os.path.join(output_folder, next_available_index(output_folder, 1))
            cv2.imwrite(image_path1, frame1)
            print(f"Image captured and saved: {image_path1}")

            image_path2 = os.path.join(output_folder, next_available_index(output_folder, 2))
            cv2.imwrite(image_path2, frame2)
            print(f"Image captured and saved: {image_path2}")

            count += 1

    # Release the cameras and close OpenCV windows
    cap1.release()
    cap2.release()
    cv2.destroyAllWindows()

# Number of images to capture
num_images = 1
# Output folder to save images
output_folder = "captured_images"
# Call the function to capture images
capture_images(num_images, output_folder)