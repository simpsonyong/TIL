""" test_case = 0
numbers = 0
real_number = []

while test_case < 1 or test_case > 50:
    test_case = int(input('input test_case(1 ~ 50): '))

for test_number in range(test_case):
    numbers = int(input('input numbers(5 ~ 1000): '))
    while numbers < 5 or numbers > 1000:
        numbers = int(input('input numbers(5 ~ 1000): '))

    real_number = list(map(int, input(f'{numbers}개의 양수를 입력하세요: ').split(' ')))
    while (min(real_number) < 1 or min(real_number) > 1000000) or (len(real_number) != numbers):
        real_number = list(map(int, input(f'{numbers}개의 양수를 입력하세요: ').split(' ')))
    case_result = max(real_number) - min(real_number)
    print('#{} {}'.format(test_number+1, case_result))
 """

test_case = 0
numbers = 0
real_number = []

while test_case < 1 or test_case > 50:
    test_case = int(input())

for test_number in range(test_case):
    numbers = int(input())
    while numbers < 5 or numbers > 1000:
        numbers = int(input())

    real_number = list(map(int, input().split(' ')))
    while (min(real_number) < 1 or min(real_number) > 1000000) or (len(real_number) != numbers):
        real_number = list(map(int, input().split(' ')))
    case_result = max(real_number) - min(real_number)
    print('#{} {}'.format(test_number+1, case_result))
