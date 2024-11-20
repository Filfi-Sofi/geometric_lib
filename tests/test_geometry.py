import unittest
from geometry import calculate_area, calculate_perimeter

class TestGeometry(unittest.TestCase):
    def test_calculate_area_circle(self):
        self.assertAlmostEqual(calculate_area("circle", radius=5), 78.54, places=2)

    def test_calculate_area_rectangle(self):
        self.assertEqual(calculate_area("rectangle", width=4, height=5), 20)

    def test_calculate_perimeter_circle(self):
        self.assertAlmostEqual(calculate_perimeter("circle", radius=5), 31.42, places=2)

    def test_calculate_perimeter_rectangle(self):
        self.assertEqual(calculate_perimeter("rectangle", width=4, height=5), 18)
