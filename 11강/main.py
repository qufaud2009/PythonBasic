def 더하기(a, b):
    return a + b

def 빼기(a, b):
    return a - b


import main1

print (main1.더하기(3,4)) #7
print (main1.빼기(4,2)) #2

from main1 import 더하기
print (더하기(3,4)) #7

from main1 import 더하기,빼기
print (더하기(3,4)) #7
print (빼기(4,2)) #2

from main1 import *
print (더하기(3,4)) #7
print (빼기(4,2)) #2

import main1 
print (main1.더하기(3,4)) #7
print (main1.빼기(4,2)) #2


print('그냥 print')
if __name__ == '__main__':
    print(__name__)
    print("수학.py 파일")

import keyword
print(keyword.kwlist )
print(keyword.iskeyword("hi"))
print(keyword.iskeyword("if"))

import random

for i  in range(6):
    number = random.randint(1,45)
    print(number, end=' ')

import time

print('현재시각:', time.time())

def manyloop(max):
    t1 = time.time()
    for a in range(max):
        pass
    t2 = time.time()
    print(t2-t1, '초 경과')

number = int(input('숫자를 입력하세요.'))
manyloop(number)

class Dog:
    name="코코"
    age = 2

    def bark(self):
        print('멍멍')
    def move(self):
        print('움직인다')

dog1 = Dog()

dog1.bark()
print(type(dog1))

dog2 = Dog()
dog2.name = '두리'
dog2.age = 4
dog2.weight = 10

print(dog1.name, dog1.age)
print(dog2.name, dog2.age)

class Dog:
    name="코코"
    age = 2

    def bark(self):
        print('멍멍')
    def move(self):
        print('움직인다')

dog1 = Dog()

dog1.bark()
print(type(dog1))

dog2 = Dog()
dog2.name = '두리'
dog2.age = 4
dog2.weight = 10

print(dog1.name, dog1.age)
print(dog2.name, dog2.age)


class Dog:
    def __init__ (self,name,age):
        self.name = name
        self.age = age

    def bark(self):
        print('멍멍')
    def move(self):
        print('움직인다')

dog1 = Dog('코코',2)
dog2 = Dog('두리',4)
dog3 = Dog('설탕',1)

print(dog1.name, dog1.age)
print(dog2.name, dog2.age)
print(dog3.name, dog3.age)
