import math
import unittest
import shape_area_calculator


class TestShapeArea(unittest.TestCase):
    def test_compute_circle_area(self):
        radius = 5
        expected_area = math.pi * radius ** 2
        self.assertAlmostEqual(shape_area_calculator.compute_circle_area(radius), expected_area)

    def test_compute_triangle_area(self):
        side1, side2, side3 = 3, 4, 5
        expected_area = 6
        expected_is_right_triangle = True
        self.assertAlmostEqual(shape_area_calculator.compute_triangle_area(side1, side2, side3)[0], expected_area)
        self.assertEqual(shape_area_calculator.compute_triangle_area(side1, side2, side3)[1], expected_is_right_triangle)


if __name__ == '__main__':
    unittest.main()