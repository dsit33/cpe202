import unittest

def swap(word):
    if len(word) <= 1:
        return word
    else:
        return word[1] + word[0]+ swap(word[2:])

class TestsLab3(unittest.TestCase):
   
    def test_swap1(self):
        self.assertEqual(swap("derek"), "ederk")
    def test_swap2(self):
        self.assertEqual(swap("spot"), "psto")
    def test_swap3(self):
        self.assertEqual(swap("abcdef"), "badcfe")
      

# Run the unit tests.
if __name__ == '__main__':
    unittest.main()