list=[1,2,3,4,5]
print(list) # [1,2,3,4,5]
list =[1,5,3,6]
print(list[1:3])
list = [1,3,5,6]
length = len(list)
print(length)
무지개 = ['빨강','주황','노랑','초록','파랑','남색','보라']
첫번째색 = 무지개[0]
print('무지개의 첫번째 색은 {}이다'.format(첫번째색))
마지막색 = 무지개[6]
print('무지개의 마지막 색은 {}이다'.format(마지막색))

동물=['강아지','고양이','새','코끼리','곰']
식물=['소나무','단풍나무','장미꽃','벚꽃']
생물=동물+식물
print(생물)#'강아지','고양이','새','코끼리','곰','소나무','단풍나무','장미꽃','벚꽃'
print(생물*3)
list=[1,2,3]
list[1]=10
print(list)
동물 = ['강아지','고양이','새','코끼리','곰']
동물.append('사람')
print(동물)
동물 = ['강아지','고양이','새','코끼리','곰']
del 동물[1]


동물 = ['강아지','고양이','새','코끼리','곰']
동물.remove('고양이')
print(동물)

list=[]
list=['아바타','어벤저스','타이타닉']
list.append('겨울왕국2')
print(list)
list = ['아바타', '어벤저스', '타이타닉','명량', '겨울왕국2']
list.insert(4,'겨울왕국')
print(list)
list=['아바타', '어벤저스', '타이타닉', '명량', '겨울왕국', '겨울왕국2']
del list[4]
print(list)
list=['아바타', '어벤저스', '타이타닉', '명량', '겨울왕국', '겨울왕국2']
list.remove('겨울왕국')
print(list)
tuple=()
print (tuple)
음식=('떡볶이','햄버거')
print(음식)
무지개 = ['빨강','주황','노랑','초록','파랑','남색','보라']
마지막색=무지개[6]
print('무지개의 마지막 색은 {}이다'.format(마지막색))
t=(1,2,3,4,5,6,7,8,9,10)
print(t*10)
t2 = t*10
print(t2)
print(len(t2))
t=[1,2,3]
t[0]='a'
print(t)
while True:
    data=int(input("1,2,3을 입력해주세요."))
    t=('주먹','가위','보')
    print( t[data-1] )
    if data==-1:
        break

# if data==1:
#     print(t[0])

# if data == 2:
#     print(t[1])
# if data==3:
#     print(t[2])
음식=[]
while True:
    food = input("좋아하는 음식은 무엇입니까?")
    음식.append(food)
    print(음식)
