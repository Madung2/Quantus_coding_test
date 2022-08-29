from random import randrange
from math import floor




def get_1_or_0():
    return randrange(2)

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

