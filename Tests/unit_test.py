import unittest
import cv2
import os

class CarParkingTestCase(unittest.TestCase):
    def test_shape(self):
        # Get the current working directory
        cwd = os.getcwd()

        # Print the current working directory
        print("Current working directory: {0}".format(cwd))
        input = cv2.imread("Data/detect_blob.png")
        expected_output = (760,541,3)
        result = input.shape
        self.assertEqual(expected_output, result)
