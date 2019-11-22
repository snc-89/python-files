from stringFunctions import StringFunctions as sf
import unittest

class TestStringFunctions(unittest.TestCase):
    def testLowerCase(self):
        self.assertEqual(sf.lowerCase("STEVE"), "steve")
        self.assertEqual(sf.lowerCase("steve"), "steve")

    def testNoDot(self):
        self.assertEqual(sf.noDot("steve."), "steve")
        self.assertEqual(sf.noDot("steve"), "steve")
        self.assertEqual(sf.noDot("steve,"), "steve")

    def testAddQuotes(self):
        self.assertEqual(sf.addQuotes("steve"), '"steve"')
        self.assertEqual(sf.addQuotes('"steve"'), '"steve"')
        self.assertEqual(sf.addQuotes('"steve'), '"steve"')

    def testReverse(self):
        self.assertEqual(sf.reverse("steve"), "evets")
        self.assertEqual(sf.reverse("rake"), "ekar")

    def testCompareString(self):
        self.assertTrue(sf.compareStrings("steve","steve"))
        self.assertFalse(sf.compareStrings("steve","rake"))
        self.assertFalse(sf.compareStrings("steve", "steve."))

    def testMakeString(self):
        arr = [0,1,2,3,4,5]
        self.assertEqual(sf.makeString(arr), "abcdef")
        


if __name__ == '__main__':
    unittest.main()
