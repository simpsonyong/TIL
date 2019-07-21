# 1일차
# 문제 1
# n = 5
# m = 9
# star = '*'
# space = ' '
# print(star*n)
# print(f'{star}{space*(n-2)}{star}\n'*(m-3)+f'{star}{space*(n-2)}{star}')
# print(star*n)

# 교수님 해설
# n, m = 5, 9 # 사실 교수님도 이거 한줄씩 변수 나누어 쓰심
# print('start')
# print((('*'*n) + '\n') * m)
# garo = '*' * n
# print((garo+'\n')*(m - 1)) + garo) # 출력시 밑에 백스페이스 처리를 고민해볼 것
# print('end')

# 문제 2
# print('"파일은 C:\\Windows\\Users\\내문서\\Python에 저장이 되어있습니다."\n나는 생각했다.
#  \'cd를 써서 git bash로 들어가봐야지\'')

# 문제 2 교수님 해설 # '' 안에 ""는 이스케이프 문자로 자동으로 되지만 엄격하게 구분하려면 \"를 사용
# answer = '\"파일은 C:\\Windows\\Users\\내문서\\Python에 저장이 되어있습니다.
# \"\n나는 생각했다. \'cd를 써서 git bash로 들어가봐야지\''
# print(answer)

# 문제 3
# a = 1
# b = 4
# c = -21
# root = (b**2 - 4*a*c)**0.5
# x1 = (-b + root) / (2*a)
# x2 = (-b - root) / (2*a)
# print('x = {}, {}'.format(x1, x2))

# 문제 3 교수님 해설 # 비슷한 방식으로 푸심 근의 공식 문제였다.
# a, b, c = 1, 4, -21
# x1 = (-b + ((b**2 - 4*a*c)**(1/2))) / (2*a)
# x2 = (-b - ((b**2 - 4*a*c))**(1/2)) / (2*a)
# print(x1, x2)

# 2일차
# 문제 1
# n = 5
# m = 9
# star = '*'
# space = ' '
# for i in range(m):
#     if i == 0 or i == m - 1:
#         print(star*n)
#     else:
#         print(star+space*(n-2)+star)

# 문제 2
# student = {'python': 80, 'algorithm': 99, 'django': 89, 'flask': 83}
# average = 0
# for i in student.values():
#     average += i
# print(average/len(student))
# print(sum(student.values()) / len(student)) => 한줄로 작성

# 문제 3
# blood_types = ['A', 'B', 'A', 'O', 'AB', 'AB', 'O', 'A', 'B', 'O', 'B', 'AB']
# dict_blood = {}
# for i in blood_types:
#     if i not in dict_blood:
#         dict_blood[i] = blood_types.count(i)
# print(dict_blood)

# 교수님 해설

# dict_blood[b] => 키 값이 오류가 있는 경우 에러 발생
# dict_blood.get(b) => 키 값이 오류가 있는 경우 None값 출력

# if dict_blood.get(b):
#         dict_blood[b] += 1
# else:
#     dict_blood[] = blood_types.count(i)

# request.args.get('stock_code') => request.args도 딕셔너리로 이루어저여ㅣㅆ다
