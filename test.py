import sprints
import unittest

class TestFunc(unittest.TestCase):
    def testListEvenIntFloat(self):
        avg,max=sprints.MyFunc(4,6,8,6.9,17.3,16.8,8)
        self.assertEqual(avg,6.5)
        self.assertEqual(max,17.3)

    def testListIntFloat(self):
        avg, max = sprints.MyFunc(4, 6, 7,5,20.8,8, 6.9, 17.3, 16.8, 8)
        self.assertEqual(avg, 6.5)
        self.assertEqual(max, 20.8)

    def testListString(self):
        result = sprints.MyFunc("str1","str2","str3")
        self.assertEqual(result, 0)

    def testListFloatNoEvenInt(self):
        avg,max = sprints.MyFunc(1,7,18.9,19.2,5,16.4)
        self.assertEqual(avg, "There was no even integers in the list")
        self.assertEqual(max, 19.2)

    def testListNoFloatNoEvenInt(self):
        avg, max = sprints.MyFunc(1, 7, 5)
        self.assertEqual(avg, "There was no even integers in the list")
        self.assertEqual(max, "There was no decimals in the list")

    def testListEvenIntNoFloat(self):
        avg, max = sprints.MyFunc(2, 4,7,3)
        self.assertEqual(avg,3)
        self.assertEqual(max, "There was no decimals in the list")

    def testListIntFloatString(self):
        avg, max = sprints.MyFunc(2, 4, 7, 3,"str",17.2,18.6,6)
        self.assertEqual(avg, 4)
        self.assertEqual(max, 18.6)



if __name__ == '__main__':
    unittest.main()