import unittest
import numpy as np

from basicfunc import *

class TestBose(unittest.TestCase):
    
    def test_low_energy(self):
        '''
        能量为 0 时, Bose 函数应该是无穷大.
        '''
        b = bose(0, 1)
        self.assertEqual(b, np.inf)
        
    def test_increasing(self):
        b11 = bose(1, 1)
        b12 = bose(1, 2)
        b21 = bose(2, 1)
        self.assertTrue(b11>b12)    # 能量相同, 温度高, Bose 函数小
        self.assertTrue(b21<b11)    # 温度相同, 能量高, Bose 函数小

if __name__=='__main__':
    unittest.main()
