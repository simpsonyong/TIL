# fizz buzz 3 6 9 게임 => 
# 3의 배수에서 fizz 5의 배수에서 buzz 15배수에서 fizz buzz출력

number = int(input('숫자를 입력하세요: '))
for i in range(1, number+1):
    if i % 15 == 0:
        print('fizzbuzz', end=' ')
    elif i % 3 == 0:
        print('fizz', end=' ')
    elif i % 5 == 0:
        print('buzz', end=' ')
    else:
        print(i, end=' ')
