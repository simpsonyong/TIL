# 1일차 HW
# 1번
# import keyword
# print(keyword.kwlist)
# ['False', 'None', 'True', 'and', 'as', 'assert',
#  'async', 'await', 'break', 'class', 'continue',
#  'def', 'del', 'elif', 'else', 'except', 'finally',
#  'for', 'from', 'global', 'if', 'import', 'in',
#  'is', 'lambda', 'nonlocal', 'not', 'or', 'pass',
#  'raise', 'return', 'try', 'while', 'with', 'yield']
# 2번
# a = 0.1 * 3
# b = 0.3
# # math 모듈 처리(python 3.5부터 활용 가능)
# import math
# print(math.isclose(a, b))
# # True 값이면 값이 동일함
# 3번
# 1) \n
# 2) \t
# 3) \\
# 4번
# name = “철수”
# print(f'안녕,{name}야')
# 5번
# 답: 5번 (float형태의 str은 int형으로 바꿀 수 없다

# 2일차 HW
# 문제1
# - String => immutable
# - List => mutable
# - Tuple => immutable
# - Range => immutable
# - Set => mutable
# - Dictionary => mutable
# 문제2
# # range 방법
# ls = []
# for i in range(1, 51):
#     if i % 2 == 1:
#         ls.append(i)
# print(ls)

# # slicing 방법
# ls = list(range(1, 51))
# print(ls[0::2])

# 문제3
# name = [
#     '김은수',
#     '김은영',
#     '김지희',
#     '김현지',
#     '문다혜',
#     '박준영',
#     '손현희',
#     '신승용',
#     '안유림',
#     '윤숙경',
#     '이경환',
#     '이설유',
#     '이승진',
#     '이지선',
#     '정병학',
#     '조현동',
#     '최솔지',
#     '하다연',
#     '허재웅',
#     '홍수경',
#     '박민기',
#     '전수빈',
#     '최재평',
#     '노영지',
#     '정은정',
# ]

# age = [
#     26,
#     25,
#     29,
#     27,
#     26,
#     29,
#     28,
#     29,
#     25,
#     26,
#     27,
#     '',
#     '',
#     27,
#     27,
#     27,
#     27,
#     28,
#     27,
#     26,
#     29,
#     26,
#     28,
#     25,
#     27,
# ]

# SS3_2 = {}
# for i in range(25):
#     SS3_2[name[i]] = age[i]

# print(SS3_2)

# print(dir())
