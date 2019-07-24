"""
1번 문제
1.2개의숫자를인자로받아더하기,빼기,곱하기,나누기
연산의결과를반환하는4개의함수를calc.py에작성하시오.
단,나누기연산에서는try except구문을사용하여‘0’으로
나누려고하는경우에는문자열’0으로는나눌수없습니다.’을반환하시오.

"""


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def mul(x, y):
    return x * y


def div(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return '0으로는 나눌 수 없습니다.'

# print(div(1, 2))
# print(div(1, 0))
# 만약 정확하게 이 파일을 실행 했을 때만, print 기능이
# 실행되면 좋겠다.($ python calc.py)
# 아래처럼 코드를 작성함

# print(__name__)  # 스트링처럼 실행됨 2가지
# 파일 name 또는 main으로

if __name__ == '__main__':
    print(div(1, 2))
    print(div(1, 0))

"""

2번 문제
2.1번에서작성한calc.py모듈을import하여,각연산을수행하는
함수들을실행하는코드를작성하시오.

"""
