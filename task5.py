import math
import unittest

def contocycfeat(hour):
    angle = (hour % 24) * 2 * math.pi / 24
    return math.sin(angle), math.cos(angle)

def calcycdiff(hour1, hour2):
    sin1, cos1 = contocycfeat(hour1)
    sin2, cos2 = contocycfeat(hour2)
    diff = math.acos(sin1 * sin2 + cos1 * cos2)
    return diff * 24 / (2 * math.pi)

class testtime(unittest.TestCase):
    
    def test_contocycfeat(self):
        sin_0, cos_0 = contocycfeat(0)
        self.assertAlmostEqual(sin_0, 0, delta=0.01)
        self.assertAlmostEqual(cos_0, 1, delta=0.01)
        
        sin_6, cos_6 = contocycfeat(6)
        self.assertAlmostEqual(sin_6, 1, delta=0.01)
        self.assertAlmostEqual(cos_6, 0, delta=0.01)
        
        sin_12, cos_12 = contocycfeat(12)
        self.assertAlmostEqual(sin_12, 0, delta=0.01)
        self.assertAlmostEqual(cos_12, -1, delta=0.01)
        
        sin_18, cos_18 = contocycfeat(18)
        self.assertAlmostEqual(sin_18, -1, delta=0.01)
        self.assertAlmostEqual(cos_18, 0, delta=0.01)

    def test_calcycdiff_same_time(self):
        self.assertAlmostEqual(calcycdiff(10, 10), 0)

    def test_calcycdiff_normal(self):
        self.assertAlmostEqual(calcycdiff(5, 7), 2, delta=0.01)
        self.assertAlmostEqual(calcycdiff(12, 15), 3, delta=0.01)

    def test_calcycdiff_across_midnight(self):
        self.assertAlmostEqual(calcycdiff(23, 1), 2, delta=0.01)
        self.assertAlmostEqual(calcycdiff(22, 2), 4, delta=0.01)

    def test_calcycdiff_halfway(self):
        self.assertAlmostEqual(calcycdiff(0, 12), 12, delta=0.01)
        self.assertAlmostEqual(calcycdiff(6, 18), 12, delta=0.01)

if __name__ == "__main__":
    unittest.main()
