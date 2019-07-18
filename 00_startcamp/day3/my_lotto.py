# my = [1, 2, 3, 4, 5, 6]

# real = [1, 2, 3, 4, 5, 6]
# bonus = 7

# my와 real이 6개가 같으면  1등
# my와 real이 5개가 같고 나머지 하나가 bonus면 2등
# my와 real이 5개가 같으면 3등
# '' 4개가 같으면 4등
# ''3개가 같으면 5등
# 나머지는 꽝

# my = [1, 2, 3, 4, 5, 7]
# real = [1, 2, 3, 4, 5, 6]
# bonus = [7]

import random
n1, n2, n3, n4, n5, n6 = map(int, input(
    '띄어쓰기로 구분하여 1 ~ 45 사이 숫자 6개를 입력하세요:').split(" "))
my = [n1, n2, n3, n4, n5, n6]
numbers = range(1, 46)
real = random.sample(numbers, 6)
bonus = random.sample(numbers, 1)  # print(type(bonus))
mismatch = 0
print('내가 뽑은번호: {0}\n당첨번호: {1}'.format(my, real))
while bonus in real:
    bonus = random.sample(numbers, 1)
print('보너스 번호: {0}'.format(bonus))
for i in real:
    if i not in my:
        mismatch += 1  # print(mismatch)
if mismatch == 0:
    print('1등! 축하합니다!')
if mismatch == 1:
    if bonus[0] in my:
        print('2등! 축하합니다!')
    else:
        print('3등! 축하합니다!')
if mismatch == 2:
    print('4등! 축하합니다!')
if mismatch == 3:
    print('5등! 축하합니다!')
else:
    print('꽝입니다!')
