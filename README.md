# Quantus_coding_test
Quantus_coding_test

## 1. get_1_or_0 함수 test

assertIn 함수를 사용해서 결과값이 [0, 1] 리스트 안에 포함되는지를 확인해 보았습니다.

```python
def test_get_1_or_0(self):
        self.assertIn(random_n.get_1_or_0(),[0,1])
```
## 2. get_random 함수 test


### 1) test_variable_below_zero함수

0미만의 숫자를 변수로 두었을 경우:

value error를 반환하기 때문에 assertRaises를 이용해서 value error를 확인해 보았습니다.

```python
def test_variable_below_zero(self):
        '''
        get_random 함수에 0미만의 숫자를 변수로 두었을 경우, value error
        '''
        self.assertRaises(ValueError, random_n.get_random, -10)
        print(10,'value error')
```
### 2) test_variable_above_zero함수

0이상의 숫자를 변수로 두었을 경우:

- 0이상의 숫자를 변수로 두었을 경우에는 랜덤한 숫자가 결과값으로 나와야 했습니다.
- 그래서 예상 가능한 변수를 TEST_LIST라는 리스트에 넣고 각각 for 문을 돌려서 get_random 함수를 통과하도록 했습니다.
- 다양한 케이스를 커버할 수 있도록 TEST_LIST에는  0, 1, 1억이 넘는 숫자, 소수를 포함하였습니다.
- get_random함수로 추출한 값은 1)0보다 같거나 큰지, 2)변수값보다 같거나 작은지 3)그리고 integer=정수인지를 확인하도록 했습니다.

```python
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
```
### 3) test_check_time함수

- 함수 실행 시간을 체크해보았습니다.
- time 모듈을 이용해서 함수 전후 시간을 잰 뒤 차이를 구했습니다.
- 처음에 1000000을 변수로 넣었더니 함수 실행 시간이 짧아 정확한 값이 나오지 않았습니다.
- 다시 TESTING_NUM을’100000000000000000000000000000000000000000000000000000000000000000000000000’으로 바꾸니 함수 실행 시간이 0.0010004043579101562로 나타났습니다.

```python
def test_check_time(self):
      '''
      걸리는 시간 체크
      '''
      TESTING_NUM=100000000000000000000000000000000000000000000000000000000000000000000000000
      start= time.time()
      random_n.get_random(TESTING_NUM)
      finish= time.time()
      print(finish-start)

>>> 0.0010020732879638672
```
조금 더 시간을 줄여볼 수 없을까 싶어서 재귀적으로 함수를 불러오는 방식이 아닌 while문을 사용해 봤습니다. 
```python
기존 코드:
def get_random(n):
    '''0~n사이의 정수를 랜덤으로 반환하는 함수'''
    if n<0:
        raise ValueError('Cannot get random number below zero')

    binary = format(floor(n), 'b')
    ls=[get_1_or_0() for i in binary]
    result= int(''.join(map(str,ls)),2)
    if result>n:
        return get_random(n)
    return result

이후코드:
def get_random(n):
    '''0~n사이의 정수를 랜덤으로 반환하는 함수'''
    if n<0:
        raise ValueError('Cannot get random number below zero')

    binary = format(floor(n), 'b')
    while True:
        ls=[get_1_or_0() for i in binary]
        result= int(''.join(map(str,ls)),2)
        if result<=n:
            return result
```
```python
def test_check_time(self):
      '''
      걸리는 시간 체크
      '''
      TESTING_NUM=100000000000000000000000000000000000000000000000000000000000000000000000000
      start= time.time()
      random_n.get_random(TESTING_NUM)
      finish= time.time()
      print(finish-start)

>>> 0.00028824806213378906
```
### 4) test_check_random함수

0미만의 숫자를 변수로 두었을 경우:

- 마지막으로 함수가 랜덤한 값을 나타내는게 맞는지 확인하는 테스트 코드를 짜보고 싶었으나 stackoverflow 등 확인 결과 일반적인 방법으로는 어려운 듯 했습니다.
- 대신 함수가 균등하게 결과를 나타내는게 맞는지를 확인해 보기로 했습니다.
- get_random 함수에 2를 넣는것을 100000번 반복한 뒤 결과값 0,1,2를 각각 카운트 했습니다.
- 마지막으로 assertTrue 함수를 사용해서 카운트한 각 숫자가 98%이상 일치하는지를 확인했습니다.

```python
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

      print(f'count0={count0},count1={count1}, count2={count2}')
			self.assertTrue(
          min(count0,count1)/max(count0,count1)>0.98
          and min(count1,count2)/max(count1,count2)>0.98
          and min(count0,count2)/max(count0,count2)>0.98
      )


>>>count0=33448, count1=33241, count2=33473
```
