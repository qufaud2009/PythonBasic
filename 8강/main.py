import random
com=random.randint(0,100)
print(com)
print('0~100까지의 숫자를 입력하세요.')
print("맞추면 100억, 틀리시면 전재산이 사라지고 죽습니다.")
n = 0
while True:
    n=n+1
    print('{}번째 도전'.format(n))
    if int(n)>10:
        print("실패 하셨습니다.")
        break

    user=input('당신의 선택은?')
    print(user)
    if int(user)>com:
        print("값이 큽니다.")
    elif int(user) <=-1:
        print(com)
        break
    elif int(user)<com:
        print("값이 작습니다.")
    else:
        print("정답 입니다.")
        break

    import random
숫자1=random.randint(0,100)
숫자2=random.randint(0,100)
정답 = 숫자1+숫자2
print(정답)
print('임의의 숫자 두개가 주어집니다.0~100까지의 두 숫자의 합을 입력하세요.')
print("맞추면 100억, 틀리시면 전재산이 사라지고 죽습니다.")
n = 0
while True:
    n=n+1
    print('{}번째 도전'.format(n))
    if n>10:
        print("실패 하셨습니다.")
        break
    print("{},{}".format(숫자1,숫자2))
    user=input('당신의 선택은?')
    print(user)
    if int(user)>정답:
        print("값이 큽니다.")
    elif int(user) <=-1:
        print(정답)
        break
    elif int(user)<(정답):
        print("값이 작습니다.")
    else:
        print("정답 입니다.")
        break

print("===빼기문제 시작======")
숫자1=random.randint(0,100)
숫자2=random.randint(0,100)
answer = 숫자1-숫자2
print(answer)
print('임의의 숫자 두개가 주어집니다.0~100까지의 두 숫자의 차를 입력하세요.')
print("맞추면 100억, 틀리시면 전재산이 사라지고 죽습니다.")
n = 0
while True:
    n=n+1
    print('{}번째 도전'.format(n))
    if int(n)>10:
        print("실패 하셨습니다.")
        break
    print("{},{}".format(숫자1,숫자2))
    user=int(input('당신의 선택은?'))
    print(user)
    if user>answer:
        print("값이 큽니다.")
    elif user<answer:
        print("값이 작습니다.")
    else:
        print("정답 입니다.")
        break


