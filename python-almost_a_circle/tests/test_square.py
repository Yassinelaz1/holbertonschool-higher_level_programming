import unittest
from models.square import Square

class TestSquare(unittest.TestCase):
    def test_constructor(self):
        """Test constructor with default id"""
        s1 = Square(5, 1, 2)
        self.assertEqual(s1.size, 5)
        self.assertEqual(s1.x, 1)
        self.assertEqual(s1.y, 2)
        self.assertEqual(s1.id, 4)

        """Test constructor with custom id"""
        s2 = Square(3, 2, 3, 100)
        self.assertEqual(s2.size, 3)
        self.assertEqual(s2.x, 2)
        self.assertEqual(s2.y, 3)
        self.assertEqual(s2.id, 100)

    def test_invalid_size(self):
        """Test for invalid size value"""
        with self.assertRaises(ValueError):
            Square(0)

        with self.assertRaises(TypeError):
            Square("invalid")

    def test_size_property(self):
        """ Test size property and setter"""
        s = Square(5)
        self.assertEqual(s.size, 5)

        s.size = 10
        self.assertEqual(s.size, 10)

        with self.assertRaises(ValueError):
            s.size = -1

        with self.assertRaises(TypeError):
            s.size = "invalid"

    def test_str(self):
        """Test string representation"""
        s = Square(5, 1, 2, 100)
        self.assertEqual(str(s), "[Square] (100) 1/2 - 5")

    def test_update(self):
        """Test update method"""
        s = Square(5, 1, 2, 100)
        s.update(200, 10, 3, 4)
        self.assertEqual(s.id, 200)
        self.assertEqual(s.size, 10)
        self.assertEqual(s.x, 3)
        self.assertEqual(s.y, 4)

    def test_to_dictionary(self):
        """Test conversion to dictionary"""
        s = Square(5, 1, 2, 100)
        expected_dict = {
            "id": 100,
            "size": 5,
            "x": 1,
            "y": 2
        }
        self.assertEqual(s.to_dictionary(), expected_dict)
    
    def test_size_change(self):
        """Test changing size and checking if width and height are updated accordingly"""
        s = Square(5)
        s.size = 10
        self.assertEqual(s.width, 10)
        self.assertEqual(s.height, 10)

    def test_area(self):
        """ Test area calculation"""
        s = Square(5)
        self.assertEqual(s.area(), 25)

    def test_invalid_x(self):
        """ Test for invalid x value"""
        with self.assertRaises(ValueError):
            Square(5, -1)

        with self.assertRaises(TypeError):
            Square(5, "invalid")

    def test_invalid_y(self):
        """Test for invalid y value"""
        with self.assertRaises(ValueError):
            Square(5, 1, -1)

        with self.assertRaises(TypeError):
            Square(5, 1, "invalid")

    def test_size_property(self):
        """Test size property and setter"""
        s = Square(5)
        self.assertEqual(s.size, 5)

        s.size = 10
        self.assertEqual(s.size, 10)

        with self.assertRaises(ValueError):
            s.size = -1

        with self.assertRaises(TypeError):
            s.size = "invalid"

    def test_str(self):
        """Test string representation"""
        s = Square(5, 1, 2, 100)
        self.assertEqual(str(s), "[Square] (100) 1/2 - 5")

    def test_update(self):
        """ Test update method"""
        s = Square(5, 1, 2, 100)
        s.update(200, 10, 3, 4)
        self.assertEqual(s.id, 200)
        self.assertEqual(s.size, 10)
        self.assertEqual(s.x, 3)
        self.assertEqual(s.y, 4)

    def test_to_dictionary(self):
        """ Test conversion to dictionary"""
        s = Square(5, 1, 2, 100)
        expected_dict = {
            "id": 100,
            "size": 5,
            "x": 1,
            "y": 2
        }
        self.assertEqual(s.to_dictionary(), expected_dict)

if __name__ == '__main__':
    unittest.main()
