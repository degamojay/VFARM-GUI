import unittest
from unittest.mock import MagicMock
from application_logic import ApplicationLogic

class TestApplicationLogic(unittest.TestCase):
    def test_update_sensor_data(self):
        # Create an instance of ApplicationLogic
        app_logic = ApplicationLogic()

        # Mock data
        data = "25.5, 28.3, 6.8, 1.2, 1500.0, 800.0"

        # Call the update_sensor_data method with mocked data
        app_logic.update_sensor_data(data)

        # Check if the sensor_data dictionary in ApplicationLogic is updated correctly
        expected_sensor_data = {
            "Nutrient Content": "No data available",
            "Water Temperature": 28.3,
            "EC Level": 1.2,
            "Ambient Temperature": 25.5,
            "pH Level": 6.8
        }
        self.assertEqual(app_logic.get_sensor_data(), expected_sensor_data)

if __name__ == "__main__":
    unittest.main()
