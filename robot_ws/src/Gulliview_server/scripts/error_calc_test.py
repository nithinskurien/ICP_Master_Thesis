import unittest
from error_calc import *

class TestOneLapCounterClockWise(unittest.TestCase):


    def test_up_strait_point_to_right(self):
        mod = errorCalc('testpath.txt')
        p0 = Point(105,50)
        self.assertEqual(mod.calculateError(p0), 5)
    def test_up_strait_point_to_left(self):
        mod = errorCalc('testpath.txt')
        p0 = Point(95,60)
        self.assertEqual(mod.calculateError(p0), -5)

    def test_left_up_point_to_right(self):
        mod = errorCalc('testpath.txt')
        p0 = Point(100,90)
        self.assertTrue(mod.calculateError(p0)< 2.8 and mod.calculateError(p0)> 2.7)
    def test_left_up_point_to_left(self):
        mod = errorCalc('testpath.txt')
        p0 = Point(90,90)
        self.assertTrue(mod.calculateError(p0)< -5.5 and mod.calculateError(p0)> -5.6)


    def test_left_strait_point_to_right(self):
        mod = errorCalc('testpath.txt')
        p0 = Point(95,100)
        mod.calculateError(p0)
        p0 = Point(50,105)
        self.assertEqual(mod.calculateError(p0), 5)
    def test_left_strait_point_to_left(self):
        mod = errorCalc('testpath.txt')
        p0 = Point(95,100)
        mod.calculateError(p0)
        p0 = Point(50,95)
        self.assertEqual(mod.calculateError(p0), -5)

    def test_left_down_point_to_right(self):
        mod = errorCalc('testpath.txt')
        p0 = Point(95,100)
        mod.calculateError(p0)
        p0 = Point(50,95)
        mod.calculateError(p0)
        p0 = Point(30,100)
        self.assertEqual(mod.calculateError(p0), 6)
    def test_left_down_point_to_left(self):
        mod = errorCalc('testpath.txt')
        p0 = Point(95,100)
        mod.calculateError(p0)
        p0 = Point(50,95)
        mod.calculateError(p0)
        p0 = Point(30,85)
        self.assertEqual(mod.calculateError(p0), -6)


    def test_down_strait_point_to_right(self):
        mod = errorCalc('testpath.txt')
        p0 = Point(95,100)
        mod.calculateError(p0)
        p0 = Point(50,95)
        mod.calculateError(p0)
        p0 = Point(30,100)
        mod.calculateError(p0)
        p0 = Point(15,50)
        self.assertEqual(mod.calculateError(p0), 5)
    def test_down_strait_point_to_left(self):
        mod = errorCalc('testpath.txt')
        p0 = Point(95,100)
        mod.calculateError(p0)
        p0 = Point(50,95)
        mod.calculateError(p0)
        p0 = Point(30,100)
        mod.calculateError(p0)
        p0 = Point(25,50)
        self.assertEqual(mod.calculateError(p0), -5)

    def test_down_right_point_to_right(self):
        mod = errorCalc('testpath.txt')
        p0 = Point(95,100)
        mod.calculateError(p0)
        p0 = Point(50,95)
        mod.calculateError(p0)
        p0 = Point(30,100)
        mod.calculateError(p0)
        p0 = Point(25,50)
        mod.calculateError(p0)
        p0 = Point(20,30)
        self.assertEqual(mod.calculateError(p0), 4)
    def test_down_right_point_to_left(self):
        mod = errorCalc('testpath.txt')
        p0 = Point(95,100)
        mod.calculateError(p0)
        p0 = Point(50,95)
        mod.calculateError(p0)
        p0 = Point(30,100)
        mod.calculateError(p0)
        p0 = Point(25,50)
        mod.calculateError(p0)
        p0 = Point(40,30)
        self.assertEqual(mod.calculateError(p0), -8)

    def test_right_strait_point_to_right(self):
        mod = errorCalc('testpath.txt')
        p0 = Point(95,100)
        mod.calculateError(p0)
        p0 = Point(50,95)
        mod.calculateError(p0)
        p0 = Point(30,100)
        mod.calculateError(p0)
        p0 = Point(25,50)
        mod.calculateError(p0)
        p0 = Point(20,30)
        mod.calculateError(p0)
        p0 = Point(60,15)
        self.assertEqual(mod.calculateError(p0), 5)
    def test_right_strait_point_to_left(self):
        mod = errorCalc('testpath.txt')
        p0 = Point(95,100)
        mod.calculateError(p0)
        p0 = Point(50,95)
        mod.calculateError(p0)
        p0 = Point(30,100)
        mod.calculateError(p0)
        p0 = Point(25,50)
        mod.calculateError(p0)
        p0 = Point(60,25)
        self.assertEqual(mod.calculateError(p0), -5)

    def test_right_up_point_to_right(self):
        mod = errorCalc('testpath.txt')
        p0 = Point(95,100)
        mod.calculateError(p0)
        p0 = Point(50,95)
        mod.calculateError(p0)
        p0 = Point(30,100)
        mod.calculateError(p0)
        p0 = Point(25,50)
        mod.calculateError(p0)
        p0 = Point(20,30)
        mod.calculateError(p0)
        p0 = Point(60,15)
        mod.calculateError(p0)
        p0 = Point(100,25)
        self.assertTrue(mod.calculateError(p0)< 5.6 and mod.calculateError(p0)> 5.5)
    def test_right_up_point_to_left(self):
        mod = errorCalc('testpath.txt')
        p0 = Point(95,100)
        mod.calculateError(p0)
        p0 = Point(50,95)
        mod.calculateError(p0)
        p0 = Point(30,100)
        mod.calculateError(p0)
        p0 = Point(25,50)
        mod.calculateError(p0)
        p0 = Point(20,30)
        mod.calculateError(p0)
        p0 = Point(60,15)
        mod.calculateError(p0)
        p0 = Point(95,30)
        self.assertTrue(mod.calculateError(p0)> -1.4 and mod.calculateError(p0)< -1.3)

    def test_up_strait_one_lap(self):
        mod = errorCalc('testpath.txt')
        p0 = Point(95,100)
        mod.calculateError(p0)
        p0 = Point(50,95)
        mod.calculateError(p0)
        p0 = Point(30,100)
        mod.calculateError(p0)
        p0 = Point(25,50)
        mod.calculateError(p0)
        p0 = Point(20,30)
        mod.calculateError(p0)
        p0 = Point(60,15)
        mod.calculateError(p0)
        p0 = Point(100,25)
        mod.calculateError(p0)
        p0 = Point(105,50)
        self.assertEqual(mod.calculateError(p0), 5)
    def test_up_strait_one_lap(self):
        mod = errorCalc('testpath.txt')
        p0 = Point(95,100)
        mod.calculateError(p0)
        p0 = Point(50,95)
        mod.calculateError(p0)
        p0 = Point(30,100)
        mod.calculateError(p0)
        p0 = Point(25,50)
        mod.calculateError(p0)
        p0 = Point(20,30)
        mod.calculateError(p0)
        p0 = Point(60,15)
        mod.calculateError(p0)
        p0 = Point(100,25)
        mod.calculateError(p0)
        p0 = Point(95,50)
        self.assertEqual(mod.calculateError(p0), -5)

class PathRecet (unittest.TestCase):
    def test_up_strait_point_to_right(self):
        mod = errorCalc('testpath.txt')
        p0 = Point(105,50)
        self.assertEqual(mod.calculateError(p0), 5)
        p0 = Point(90, 100)
        self.assertEqual(mod.calculateError(p0), 0)
        p0 = Point(2000, 2000)
        self.assertTrue(mod.calculateError(p0)> 1000)
        p0 = Point(105,50)
        self.assertEqual(mod.calculateError(p0), 5)

if __name__ == '__main__':
    unittest.main()
