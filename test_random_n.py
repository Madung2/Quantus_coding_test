import unittest
import random_n
import time



class TestGet1Or0(unittest.TestCase):
    def test_get_1_or_0(self):
        self.assertIn(random_n.get_1_or_0(),[0,1])


class TestGetRandom(unittest.TestCase):

    def test_variable_below_zero(self):
        '''
        get_random 함수에 0미만의 숫자를 변수로 두었을 경우, value error
        '''
        self.assertRaises(ValueError, random_n.get_random, -10)


    def test_variable_above_zero(self):
        '''
        get_random 함수에 0이상 숫자를 변수로 두었을 경우
        '''
        TEST_LIST=[0,1,3,10,2.1,10000000000000000]
        for i in TEST_LIST:
            num=random_n.get_random(i)

            self.assertTrue(
                num>=0 
                and num<=i 
                and isinstance(num, int)
                )

    def test_check_time(self):
        '''
        걸리는 시간 체크
        '''
        TESTING_NUM=100000000000000000000000000000000000000000000000000000000000000000000000000
        start= time.time()
        random_n.get_random(TESTING_NUM)
        finish= time.time()
        print('************')
        print(finish-start)

    def test_check_random(self):
        '''
        함수가 균등하게 결과를 나타내는지 체크
        '''
        TRYS=100000
        count0=0
        count1=0
        count2=0
        for i in range(TRYS):
            if random_n.get_random(2)==0:
                count0+=1
            if random_n.get_random(2)==1:
                count1+=1
            if random_n.get_random(2)==2:
                count2+=1

        # print(f'count0={count0},count1={count1}, count2={count2}')

        self.assertTrue(
            min(count0,count1)/max(count0,count1)>0.98
            and min(count1,count2)/max(count1,count2)>0.98
            and min(count0,count2)/max(count0,count2)>0.98
        )


if __name__ == '__main__':
    unittest.main()