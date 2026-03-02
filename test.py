import unittest
import main

class TestMain(unittest.TestCase):
    def setUp(self):
        print('about to test function')
    def test_do_stuff(self):
        test_param = 10
        res = main.do_stuff(test_param)
        self.assertEqual(res, 15)

    def test_do_stuff2(self):
        test_param = 'alsdkjfalsdj'
        res = main.do_stuff(test_param)
        self.assertIsInstance(res, ValueError)

    def test_do_stuff3(self):
        test_param = None
        res = main.do_stuff(test_param)
        self.assertEqual(res, 'Please enter valid number')



if __name__ == '__main__':
    unittest.main()