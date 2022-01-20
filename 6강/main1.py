print("무슨 총으로 결말을 보시겠습니까(mg42/bar/m1919 browning/m2 browning)")
input("mg42/bar/m1919 browning/m2 browning")
hit = 0
while hit < 1111:
    hit = hit+1
    print("나무를 {}번 찍었습니다.".format(hit))
    if hit == 1110:
        print("!system! 산신령을 죽였으므로 잔혹한 운명으로 대체됩니다.")
        print("타타타타타타타타타타타타타타타타타타타타타타타타타탙나타타타타타타타타타타타타타타ㅏ타타타ㅏ타타타타ㅏ타ㅏ탕........감히 산신령의 나무를 베어?!")
        print("GAME OVER")
    elif hit == 1111:
        print("!system! 산신령을 죽였으므로 잔혹한 운명으로 대체됩니다.")
        print("날 10번 죽일 셈이냐?! 타타타타타타타타타타타타타타타타타타타타타타타타타탙나타타타타타타타타타타타타타타ㅏ타타타ㅏ타타타타ㅏ타ㅏ탕")
    else:
        print("!system! 끈기가 없으므로 잔혹한 운명으로 대체됩니다.")
        print("지사내가 도끼를 들었으면,나무가라도 베어야지!! 타타타타타타타타타타타타타타타타타타타타타타타타타탙나타타타타타타타타타타타타타타ㅏ타타타ㅏ타타타타ㅏ타ㅏ탕")
        print("GAME OVER")

number = 1
while number < 99:
    number=number+1
    print(number)

for number in range(1, 99, 1):
    print(number)

for number in range(1,1000):
    string = '{}*{}={}' .format(999, number, 999*number)
    print(string)



for 단 in range(2,10):
    for number in range(1,10):
        string = '{}x{}={}'. format(단, number, 단*number)
        print(string)
