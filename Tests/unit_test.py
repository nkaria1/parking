import unittest
import cv2

class CarParkingTestCase(unittest.TestCase):
    def test_shape(self):
        input = cv2.imread("../Data/detect_blob.png")
        expected_output = (760,541,3)
        result = input.shape
        self.assertEqual(expected_output, result)
