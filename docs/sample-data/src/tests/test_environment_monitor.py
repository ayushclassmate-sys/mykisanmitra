import unittest

from src.environment_monitor import validate_reading


class TestEnvironmentMonitor(unittest.TestCase):

    def test_valid_reading(self):
        self.assertTrue(validate_reading(25, 60))

    def test_low_temperature(self):
        self.assertFalse(validate_reading(-51, 60))

    def test_high_temperature(self):
        self.assertFalse(validate_reading(71, 60))

    def test_negative_humidity(self):
        self.assertFalse(validate_reading(25, -1))

    def test_excessive_humidity(self):
        self.assertFalse(validate_reading(25, 101))

    def test_boundary_values(self):
        self.assertTrue(validate_reading(-50, 0))
        self.assertTrue(validate_reading(70, 100))


if __name__ == "__main__":
    unittest.main()
