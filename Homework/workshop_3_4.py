# 3일차
""" Palindrome은 앞에서부터 읽었을 때와 뒤에서부터 읽었을 때 같은 단어를 뜻한다.
따라서, ‘a’ ‘nan’ ’토마토’ 모두 palindrome에 해당합니다. 단어를 입력받아 Palindrome을
검증하고 True나 False를 리턴하는
함수 palindrome(word)를 만들어보세요. """

# result = False
# is_palindrome = input('단어(회문)을 입력하세요:')
# if is_palindrome == is_palindrome[::-1]:
#     result = True

# print(f'해당 단어 회문 검증: {result}')

# 4일차

""" v 양의 정수 x를 입력 받아 제곱근의 근사값을 반환하는 함수를 작성하세요.
sqrt() 사용 금지 """

""" def sq(number):
    import math
    i = 0
    while i**2 < number:
        i += 1
    left = i - 1
    right = i
    while not math.isclose(left, right):
        standard = (left + right) / 2
        if standard ** 2 >= number:
            right = standard
        else:
            left = standard
    return left
number = int(input('제곱근 근사값을 원하는 숫자를 입력하세요: '))
print(sq(number)) """

""" def bisection(n, minimum=0, maximum=1):
    import math
    while maximum**2 < n:
        minimum, maximum = minimum, maximum + 1
    standard = (minimum + maximum) / 2
    if math.isclose(minimum, maximum):
        return minimum
    else:
        if standard**2 > n:
            maximum = standard
        else:
            minimum = standard
        return bisection(n, minimum, maximum)
number = int(input('제곱근 근사값을 원하는 숫자를 입력하세요: '))
print(bisection(number)) """

# 교수님 해설 while

""" def bisection(n, minimum=0, maximum=1):
    import math
    if minimum ** 2 == n:
        return minimum
    elif maximum ** 2 == n:
        return maximum
    else:
        while not math.isclose(minimum, maximum):
            if minimum ** 2 < n < maximum ** 2:
                guess = (minimum + maximum) / 2
                if n > guess ** 2:
                    minimum = guess
                else:
                    maximum = guess
            else:
                minimum, maximum = maximum, maximum + 1
        return minimum
print(bisection(3), 3 ** 0.5) """
# minimum, maximum = maximum, maximum + 1 이 연산을 안쪽에 듬

# def bis(n, minimum=0, maximum=1):
#     import math
#     while maximum**2 < n:
#         minimum, maximum = minimum, maximum + 1
#     standard = (minimum + maximum) / 2
#     if math.isclose(minimum, maximum):
#         return minimum
#     else:
#         if standard**2 > n:
#             maximum = standard
#         else:
#             minimum = standard
#         return bisection(n, minimum, maximum)
# number = int(input('제곱근 근사값을 원하는 숫자를 입력하세요: '))
# print(bisection(number))

# 교수님 해설 재귀
def bis(n, minimum=0, maximum=1):
    import math
    if minimum ** 2 == n:
        return minimum
    elif maximum ** 2 == n:
        return maximum
    elif math.isclose(minimum, maximum):
        return minimum

    if minimum ** 2 < n < maximum ** 2:
        guess = (minimum + maximum) / 2
        if n < guess ** 2:
            return bis(n, minimum, guess)
        else:
            return bis(n, guess, maximum)
    else:
        minimum, maximum = minimum, maximum + 1
        return bis(n, minimum, maximum)

print(bis(34), 34 ** 0.5)
