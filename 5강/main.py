def 피규어():
    give=input('밀러 대위,잭슨 일병,레이번 일병,호바스 상사,멜리쉬 일병,업헴 통신병,카르파조 일병 중 무엇을 고르시겠습니까?')
    get=input('did와 face pool중 어느 회사를 고르시겠습니까(did/face pool)?')
    회사1 = 'did'
    회사2 = 'face pool'
    if 회사1==get:
        if '밀러대위'== give:
            print('did 밀러 대위를 주세요.')
        elif '잭슨일병'==give:
            print('did 잭슨 일병을 주세요')
        elif '레이번 일병'==give:
            print('did 레이번 일병을 주세요')
        elif '호바스 상사'==give:
            print('did 호바스 상사를 주세요')
        elif '업헴 통신병'==give:
            print('did 업헴 통신병을 주세요')
        elif '카르파조 일병'==give:
            print('did 카르파조 일병을 주세요')
    if 회사2 == get:
        if '밀러대위'== give:
            print('face pool 밀러 대위를 주세요.')
        elif '잭슨일병'==give:
            print('face pool 잭슨 일병을 주세요')
        elif '레이번 일병'==give:
            print('face pool 레이번 일병을 주세요')
        elif '호바스 상사'==give:
            print('face pool 호바스 상사를 주세요')
        elif '업헴 통신병'==give:
            print('face pool 업헴 통신병을 주세요')
        elif '카르파조 일병'==give:
            print('face pool 카르파조 일병을 주세요')

movie1 = input('CGV 라이언 일병 구하기가 상영 중인가요(예/아니요)?')
movie2 = input('아이맥스 라이언 일병 구하기가 상영 중인가요(예/아니요)?')
if movie1 == '예':
    print('CGV로 가자')
    피규어()
elif movie2 == '예':
    print('아이맥스로 가자')
else:
    print('집에 가서 밴드 오브 브라더스 재방송 보자')
popcorn = input('카라멜 팝콘이 남아있나요(예/아니요)?')
if popcorn == '예':
    print('카라멜 팝콘 주세요')
else:
    print('치즈 팝콘을 주세요') 
juice = input('바나나 우유가 있나요(예/아니요)?')
if juice == '예':
    print('바나나 우유 주세요')
else:
    print('딸기 우유를 주세요')
