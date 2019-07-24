# 3일차

""" 1. Python에서 기본으로 사용할 수 있는 Built in function 5개를 찾아서 작성하세요.
dir(__builtins__)
abs() set() sum() int() max() """

""" 2. 다음과 같이 함수가 정의되어 있다. 보기 중, 오류가 발생하는 코드를 고르시오.
def ssafy(name, location='서울'):
    print(f'{name}의 지역은 {location}입니다.')
답: 3번 ssafy(name='허준', '구미')
SyntaxError: positional argument follows keyword argument """

""" 3.다음과 같이 코드가 작성되어 있을 때, 변수 result에 저장된 값을 작성하시오.
def my_func(a,b):
    c = a + b
    print(c)

result = my_func(4,7)

result에 저장되는 값: '' """
# => 프린트함수로 다 날라가버림
# 4일차
# 1. Python에서 변수를 찾을 때 접근하는 이름 공간을 순서대로 작성하시오.
""" 파이썬에서 사용되는 이름들은 이름공간(namespce)에 저장되어 있습니다. 그리고, LEGB Rule을 가지고 있습니다.

변수에서 값을 찾을 때 아래와 같은 순서대로 이름을 찾아나갑니다.

Local scope: 정의된 함수
Enclosed scope: 상위 함수
Global scope: 함수 밖의 변수 혹은 import된 모듈
Built-in scope: 파이썬안에 내장되어 있는 함수 또는 속성 """

""" 2. 다음 중 옳지 않은 것을 고르시오. 1번 2개의 객체를 튜플형 식으로 반환 가능하다
(1) 함수는 오직 하나의 객체만 반환할 수 있어서, ‘return a, b’처럼 쓸 수 없다.
(2) 함수에서 return을 작성하지 않으면 None 값을 반환한다.
(3) 함수의 인자(parameter)는 함수를 선언할 때 설정한 값이며,
인수(argument)는 함수를 호출할 때 넘겨주는 값이다.
(4) 가변 인자를 설정할 때는 인자 앞에 *을 붙이고, 이 때는 함수 내에서 tuple로 처리된다. """


# def function()#parameter
# function(a,b)#a,b는 argument

# 3. 재귀 함수를 쓰는 장점과 단점을 작성하시오.
""" 장점: 자기 자신을 호출하는 재귀함수는 알고리즘 구현시 많이 사용됨
코드가 더 직관적이고 이해하기 쉬운 경우가 있음
알고리즘 자체가 재귀적인 표현이 자연스러운 경우가 있음
재귀 호출은 '변수 사용'을 줄여줄 수 있음
단점: 만들기는 어려움, for문이 더 빠름 """
