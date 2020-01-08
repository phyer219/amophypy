import unittest
import basicfunc

class TestBose(unittest.TestCase):
    def test_zero_temperature(self):
        b = bose(1, 1e10)
        self.assertTrue(b>1e10)

if __name__=='__main__':
    unittest.main()
