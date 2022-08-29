import unittest
import random_n

class TestQuantusQuiz(unittest.TestCase):
    def test_get_1_or_0(self):
        self.assertIn(random_n.get_1_or_0(),[0,1])


    def test_get_random(self):
        test_list=[0,1,3,10, 2.1, 10000000000000000, ]

        for i in test_list:
            if i <0:
                self.assertRaises(ValueError)
            num=random_n.get_random(i)

            self.assertTrue(
                num>=0 
                and num<=i 
                and isinstance(num, int)
                )
            print(i,num, True)
        


if __name__ == '__main__':
    unittest.main()