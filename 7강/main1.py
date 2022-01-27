prompt = """
100
100, '종료'
Enter number:
"""
print(prompt)

number = 0
while number  !=100:
    print(prompt)
    number = int(input())

data = input("입력값")
if int(data) +20 <255:
    print(int(data) + 20)
else:
    print(255)

data = input("입력값")
if int(data) -20 <255 and int(data) -20 >= 0: 
    print(int(data) - 20)
elif (int(data) - 20) <= 0:
    print(0)
else:
    print(255)

data = input("주민둥록 번호")
if data[7] == '1' or data[7] == '3' :
    print("성별은 남자입니다.")
elif data[7] == '2' or data[7] == '4':
    print("성별은 여자입니다.")

for number in range(3,7,1):
    print(number)

for number in range(3,7,1):
    print(number)
    print("______")

for number in range(1,1000,1):
    if int(number)%3 == 0:
        print(number)

단=3
for number in range(1,10,2):
    string='{}x{}={}' .format(단,number,단*number)
    print(string)

data =0
for number in range(1,126,1):
    data=data+number
    # string='{}+{}={}' .format(number,number+1,number*2+1)
    print(data)

data =1
for number in range(1,99,1):
    data=data*number
    print(data)

while True:
    score=input('점수는?')
    if int(score) >= 60:
        print('시험에 합격하셨습니다.')
    else:
        print('시험에 불합격 하셨습니다.')
        if int(score) == -1:
            break
