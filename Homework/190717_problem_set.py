# 1번
# for first in range(2, 10):
#     print(f'----- {first} 단 -----')
#     for second in range(1, 10):
#         print(f'{first} * {second} = {first*second}')

# 2번
# count = 0
# number = int(input())
# for i in range(2, number+1):
#     for j in range(1, i+1):
#         if i % j == 0:
#             count += 1
#     if count == 2:
#         print(i)
#     count = 0
#     if count > 2:
#         break
# 1번째
# N = 10
# for i in range(2, N+1):  # 2 ~ 10
#     is_prime = True

#     for j in range(2, i):
#         if i % j == 0:
#             is_prime = False
#             break

#     if is_prime == True:
#         print(i)
# 2번째
# import time
# start = time.time()

# N = 100000
# for i in range(2, N+1):  # 2 ~ 10
#     for j in range(2, int(i**0.5)+1):
#         if i % j == 0:
#             break
#     else:
#         print(i)

# end = time.time()

# print(end - start)

# 3번
# 1번째
# fact = 1
# number = int(input())
# for i in range(1, number+1):
#     fact *= i
# print(fact)
# 2번째
# import math
# result = math.factorial(5)
# print(result)

# 4번
# users = [
#     {'id': 'john', 'password': 'qwer1234'},
#     {'id': 'neo', 'password': '12341234'},
#     {'id': 'jason', 'password': 'kingjason'},
# ]
# check = True
# user = input('id 를 입력하세요:')
# for i in range(len(users)):
#     if user in users[i]['id']:
#         k = i
#         password = input('password 를 입력하세요:')
#         if password in users[k]['password']:
#             print('환영합니다!')
#             break
#         else:
#             print('패스워드가 올바르지 않습니다.')
#             break
#     if user not in users[i]['id']:
#         print('존재하지 않는 사용자 입니다.')
#         break

# 엑스트라 4번

# 과일은 몇개?
# 아래 코드에서 과일과 아닌 것을 구분하기

# basket = {'apple': 4, 'orange': 3, 'computer': 28, 'tv': 2, 'banana': 5, 'tomato': 9}
# fruits = ['apple', 'orange', 'banana', 'pear', 'tomato']

# # 과일은 21개, 아닌 것은 30개
# total = [0, 0]
# for k, v in basket.items():
#     if k in fruits:
#         total[0] += v
#     else:
#         total[1] += v
# print('과일은 {}개, 아닌 것은 {}개'.format(total[0], total[1]))
