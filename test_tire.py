import unittest
from datetime import datetime

from tire.carrigan_tire import CarriganTire
from tire.octoprime_tire import OctoPrimeTire

class TestCarrigan(unittest.TestCase):
    def test_needs_service_true(self):
        sensor_array = [1,0.1,0.2,0.9]
        tire = CarriganTire(sensor_array)
        self.assertTrue(tire.needs_service())
        
    def test_needs_service_false(self):
        sensor_array = [0.3,0.1,0.2,0.34]
        tire = CarriganTire(sensor_array)
        self.assertFalse(tire.needs_service())
        

class TestOctoPrime(unittest.TestCase):
    def test_needs_service_true(self):
        sensor_array = [1,1,1,0.1]
        tire = OctoPrimeTire(sensor_array)
        self.assertTrue(tire.needs_service())
        
    def test_needs_service_false(self):
        sensor_array = [0.4,0.3,0.25,0.7]
        tire = OctoPrimeTire(sensor_array)
        self.assertFalse(tire.needs_service())
        
if __name__ == '__main__':
    unittest.main()