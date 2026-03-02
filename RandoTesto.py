import unittest
import RandoGamo

class TestGame(unittest.TestCase):
    def setUp(self):
        print('Beginning Tests')

    def test_win_condition(self):
        test_target = test_guess = 5
        res = RandoGamo.check_guess(test_target, test_guess)
        self.assertEqual(res, 'Congrats!\nYou Win!!!')



if __name__ == '__main__':
    unittest.main()