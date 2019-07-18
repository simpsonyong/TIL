my = [1, 2, 3, 4, 5, 8]
real = [1, 2, 3, 4, 5, 9]
bonus = 8

match_count = 0
is_bonus = False  # is_bonus 변수를 선언해야한다.

# set 집합개념을 적용한 방법
# set의 특징: 리스트와 달리 주머니 순서에 대한 개념이 존재하지 않음
# set{1, 2, 3} list[1, 2, 3] tuple(1, 2, 3) Dictionary{1:1, 2:2, 3:3}
# set과 dictionary 차이: dictionary는 키와 밸류값이 따로 존재 
# 리스트와 다른 클래스 my_set = set(my)
# 교집합 비교 set(my)
'''
match = set(my).intersection(set(real))
print(match)
match_count = len(match)
set으로 할 경우 상단 match_count = 0 선언도 필요 없다
'''

for i in my:
        # 밑에 bonus 매치는 비효율적인 방법임.
        # if 자체적으로 해결하는 다른 방법이 선호됨
    if i == bonus:
        is_bonus = True
        # False로 기준 삼아도 되지만 컴퓨터가 일을 많이한다.

    for j in real:
        if i == j:
            # match_count = match_count + 1
            match_count += 1

if bonus in real:
    is_bonus = True

# print(match_count, is_bonus)

if match_count == 6:
    result = '1등'

elif match_count == 5:
    if is_bonus:
        # is_bonus 변수 없이 if bonus in my로 바꿔버리면 해결
        result = '2등'
    else:
        result = '3등'

elif match_count == 4:
    result = '4등'

elif match_count == 3:
    result = '5등'

else:
    result = '꽝ㅠ'

print(result)
