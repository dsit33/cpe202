import unittest

def intpow(x, n):
    if n == 0:
        return 1
    else:
        return x * intpow(x, n-1)
    
class TestsLab3(unittest.TestCase):
   
    def test_intpow1(self):
        self.assertEqual(intpow(2, 3), 8)
    def test_intpow2(self):
        self.assertEqual(intpow(2, 4), 16)
    def test_intpow3(self):
        self.assertEqual(intpow(2, 8), 256)
      

# Run the unit tests.
if __name__ == '__main__':
    unittest.main()