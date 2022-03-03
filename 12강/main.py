class Dog:
    def __init__(self, name, age):
       self.name = name
       self.age = age

    def bark(self):
        print ('멍멍')

    def move(self):
        print ('움직인다')

    def __str__(self):
        sentence = '이름:{} ,나이:{}'.format(self.name, self.age)
        return sentence

dog1 = Dog('코코',2)
dog2 = Dog('두리',2)
dog3 = Dog('핏불',5)
print(dog1)
print(dog2)
print(dog3)

class Animal:
    def eat(self):
        print('먹는다')
    def move(self):
        print('움직인다')

class Dog(Animal):
    def bark(self):
        print('멍멍')
    def shake(self):
        print('꼬리를 흔들다')

dog=Dog()
dog.eat()
dog.move()
dog.bark()
dog.shake()

class Animal:
    def __init__(self, name, age):
       self.name = name
       self.age = age

    def eat(self):
        print ('먹는다')

    def move(self):
        print ('움직인다')

class Dog:
    def __init__(self, name, age):
       self.name = name
       self.age = age

    def bark(self):
        print ('멍멍')

    def shake(self):
        print ('흔들다')

    def __str__(self):
        sentence = '이름:{} ,나이:{}'.format(self.name, self.age)
        return sentence

    def __str__(self):
        sentence = '이름:{} ,나이:{}'.format(self.name, self.age)
        return sentence

dog1=Dog('코코',2)

dog = Dog('두리',3)
dog.bark()
dog.shake()

class calculator:
    def __init__(self):
        self.result = 0

    def 더하기(self, num):
        self.result += num
        return self.result

call = calculator()

print(call.더하기(3))
print(call.더하기(4))

class Animal:
    def __init__(self, name, age):
       self.name = name
       self.age = age

    def eat(self):
        print ('먹는다')

    def move(self):
        print ('움직인다')

class Crong:
    def __init__(self, name, age):
       self.name = name
       self.age = age

    def bark(self):
        print ('크로오옹!')
    def say(self):
        print ('크로오옹!')

    def __str__(self):
        sentence = '이름:{} ,나이:{}'.format(self.name, self.age)
        return sentence

    def __str__(self):
        sentence = '이름:{} ,나이:{}'.format(self.name, self.age)
        return sentence

crong = Crong('크롱',19)
crong.bark()
crong.say()

class Animal:
    def __init__(self, name, age):
       self.name = name
       self.age = age

    def eat(self):
        print ('먹는다')

    def move(self):
        print ('움직인다')

class Human:
    def __init__(self, name, age,birthday):
       self.name = name
       self.age = age
       self.birthday = birthday

    def 말하기(self):
        print ('')


class Student(Human):
    def __init__(self, name, age):
       self.name = name
       self.age = age

    def 중2병(self):
        print ('내 왼손에 흑염룡이...')
    
human = Human('김말자',99)
human.말하기()
student= Student('김법규',15)
student.중2병()
