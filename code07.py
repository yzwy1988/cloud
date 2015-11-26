import unittest

class Test(unittest.TestCase):
    def test_case(self):
        try:
            num=input("Enter a number:")
            msg="the number is not 10!"
            self.assertEqual(num,10,msg),
        except:
            AssertionError,"msg",
            print (msg)
            

if __name__=="__main__":
    unittest.main()