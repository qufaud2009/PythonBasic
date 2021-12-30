def 시리얼먹기(우유,시리얼,그릇,숟가락):
    #print ("준비물을 준비합니다.")
    print ("{}을 {}에 넣습니다.".format(시리얼,그릇))
    print ("{}를 {}이 담긴 {}에 따릅니다.".format(우유,시리얼,그릇))
    print ("{}으로 {}과 {}를 떠서 먹습니다.".format(숟가락,시리얼,우유))


def 시리얼먹기(우유,시리얼,그릇,숟가락):
    #print ("준비물을 준비합니다.")
    print ("{}을 {}에 넣습니다.".format(시리얼,그릇))
    print ("{}를 {}이 담긴 {}에 따릅니다.".format(우유,시리얼,그릇))
    print ("{}으로 {}과 {}를 떠서 먹습니다.".format(숟가락,시리얼,우유))
    return"{} 1리터, {} 500그램 남았습니다.". format(우유, 시리얼)

결과 = 시리얼먹기("서울우유","콘푸로스트","밥그릇","쇠숟가락")
print (결과)


def say1 (name):
    string = '안녕하세요?   ' + name + '님'
    return string
def say2 (name):
    string = '안녕하세요?   ' + name + '님'
    print (string)

name = "tlswndud"
string = say1(name)

print(string)


name = input('당신의 이름은? ')
print(name)

age = input('당신의 나이는?')
print(age)
