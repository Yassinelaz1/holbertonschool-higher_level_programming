import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def test_constructor(self):
        """Test constructor with default id"""
        r1 = Rectangle(5, 10, 1, 2)
        self.assertEqual(r1.width, 5)
        self.assertEqual(r1.height, 10)
        self.assertEqual(r1.x, 1)
        self.assertEqual(r1.y, 2)
        self.assertEqual(r1.id, 2)

        """Test constructor with custom id"""
        r2 = Rectangle(3, 6, 2, 3, 100)
        self.assertEqual(r2.width, 3)
        self.assertEqual(r2.height, 6)
        self.assertEqual(r2.x, 2)
        self.assertEqual(r2.y, 3)
        self.assertEqual(r2.id, 100)

    def test_invalid_width(self):
        """ Test for invalid width value"""
        with self.assertRaises(ValueError):
            Rectangle(0, 5)

        with self.assertRaises(TypeError):
            Rectangle("invalid", 5)

    def test_invalid_height(self):
        """ Test for invalid height value"""
        with self.assertRaises(ValueError):
            Rectangle(5, -1)

        with self.assertRaises(TypeError):
            Rectangle(5, "invalid")

    def test_invalid_x(self):
        """Test for invalid x value"""
        with self.assertRaises(ValueError):
            Rectangle(5, 10, -1)

        with self.assertRaises(TypeError):
            Rectangle(5, 10, "invalid")

    def test_invalid_y(self):
        """ Test for invalid y value"""
        with self.assertRaises(ValueError):
            Rectangle(5, 10, 1, -1)

        with self.assertRaises(TypeError):
            Rectangle(5, 10, 1, "invalid")

    def test_area(self):
        """ Test area calculation"""
        r = Rectangle(5, 10)
        self.assertEqual(r.area(), 50)

    def test_str(self):
        """ Test string representation"""
        r = Rectangle(5, 10, 1, 2, 100)
        self.assertEqual(str(r), "[Rectangle] (100) 1/2 - 5/10")

    def test_update(self):
        """Test update method"""
        r = Rectangle(5, 10, 1, 2, 100)
        r.update(200, 6, 12, 3, 4)
        self.assertEqual(r.id, 200)
        self.assertEqual(r.width, 6)
        self.assertEqual(r.height, 12)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)

    def test_to_dictionary(self):
        """ Test conversion to dictionary"""
        r = Rectangle(5, 10, 1, 2, 100)
        expected_dict = {
            "id": 100,
            "width": 5,
            "height": 10,
            "x": 1,
            "y": 2
        }
        self.assertEqual(r.to_dictionary(), expected_dict)

if __name__ == '__main__':
    unittest.main()
