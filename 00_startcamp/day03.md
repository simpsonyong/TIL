# StartCamp Day03





```
# 리스트 내포 기능을 이용해 다음 문장으로부터 모음('aeiou')을 제거하십시오.

\# 'Python is powerful... and fast; plays well with others; runs everywhere; is friendly & easy to learn; is Open.'

\# 입력

\# 입력없음

\# ex_012_input.txt

\# 출력

\# Pythn s pwrfl... nd fst; plys wll wth thrs; rns vrywhr; s frndly & sy t lrn; s Opn.
```



```
#   a = [1, 2, 3, 4]

\#   result = []

\#   for num in a:

\#       result.append(num * 3)

\#   print(result)

\#   

\#   result = [num * 3 for num in a]

\#   print(result)

\#   

\#   result = [num * 3 for num in a if num % 2 == 0]

\#   print(result)

\#   

\#   # 연습문제 풀이

\#   print("[문제5] 리스트 내포1")

\#   """

\#   리스트 중에서 홀수에만 2를 곱하여 저장하는 다음과 같은 코드가 있다.

\#   numbers = [1, 2, 3, 4, 5]

\#   result = []

\#   for n in numbers:

\#       if n % 2 == 1:

\#           result.append(n*2)

\#   위 코드를 리스트 내포로 표현하시오.

\#   """

\#   numbers = [1, 2, 3, 4, 5]

\#   result = [num * 2 for num in numbers if num % 2 == 1]

\#   print(result)

\#   

\#   print("[문제6] 리스트 내포2")

\#   """

\#   리스트 내포를 이용하여 다음 문장에서 모음('aeiou')을 제거하시오.

\#   Life is too short, you need python

\#   """

\#   moeum = "aeiou"

\#   sentence = "Life is too short, you need python"

\#   result = [char for char in sentence if char not in moeum]

\#   print(''.join(result))


```



## Input()에 대하여

우리가 어떠한 입력도 취하지 않으면 프로그램은 끝나지 않음.

input은 무조건 문자열로 받음

$(달러사인/프롬프트)의 의미 : 컴퓨터가 입력받을 준비가 되어있다.

###### ![1562717647130](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1562717647130.png)

###### ![1562717769490](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1562717769490.png)

```
Ctrl + C : 동작이나 입력 취소하고 다시 시작

Ctrl + D : 터미널 종료

* 무언가 종료를 하고 싶을 때는 위의 단축키 중 하나를 입력하면 된다
```

name = input('What is your name?: ') # ----> input 내부에 질문을 통하여 UX 개선

```
# code는 = 을 기준으로 오른쪽부터 읽는다

name = input('What\'s your name?: ') # input을 계산하고 변수 name에 그 값을 입력
print('hi, ' + name)


```

```
리스트

numbers[-1] # 파이썬에서만 동작함 뒤에서 첫번째 값을 불러들이는 것

```

```
input() 을 문자열로 받아도 리스트로 인식가능

words = input('입력 고고: ')

print('{0}, {1}'.format(words[0], words[-1]))

박스 안에 들어있는 값보다  type이나 class가 중요하다

type 물타입(이상해꽃 이상해풀 )
```



#### <u>파이썬은 input에 사용자의 입력을 받으면 언제나 string(문자열)으로 나온다!</u

```
words = input('입력 고고: ')

print(type(words))

print(words[0], words[-1])

*output*
입력 고고: 12345
<class 'str'>
1 5
(venv)
```

|      |      |      |      |      |      |
| ---- | ---- | ---- | ---- | ---- | ---- |
| 1    |      |      |      |      |      |
| TRUE |      |      |      |      |      |
| [1   | 2    | 3    | 4    | 5]   |      |
| [p   | n    | e    | n    | o]   |      |
|      |      |      |      |      |      |
|      |      |      |      |      |      |

컴퓨터가 메모리에 저장하는 방식(문자열이 리스트로 인식되는 이유)

문자열을 list로 바꿀 필요가 없다!

```
# words 의 첫 글자와 마지막 글자를 출력하라.

방법 1: 비효율
words = input('입력 고고: ')
lst_words = list(words) # 이렇게 굳이 리스트로 바꿀 필요가 없다
print('{0}, {1}'.format(words[0], words[-1]))

방법 2: 효율
words = input('입력 고고: ')
print(type(words))
print(words[0], words[-1]) # 이렇게만 해주셔도 됩니다.

방법 3: 비효율(길이값으로)
import random
length = random.choice(range(1, 100)) # 0
unknown = list(range(length)) # [0, 1, 2, ..., 49]
print(unknown)
print('{0}, {1}'.format(unknown[0], unknown[-1]))


기초 문제
numbers = [1, 2, 3, 4, 5]
# numbers 의 첫 요소와 마지막 요소를 출력하라
print('{0}, {1}'.format(numbers[0], numbers[-1]))
```



```
자연수
n = input('자연수를 입력하세요: ')
# '10' => 10
# str => list(str) / str => int(str)

try:
    n_value = int(n)
    for i in range(1, n_value+1):# 0 ~ 9
        print(i)

except:
    print('자연수를 입력하세요!!!!!!!!!!!!!')
    
    n_value = int(n)
    for i in range(1, n_value+1):# 0 ~ 9
        print(i + 1, ㄷ)
    
```

소프트웨어 접점 ㅋㅋ 디폴트값(기본적으로)

#### print(i + 1, end='/') ->  range에서 설정하지말고 밑에 프린트에서 설정하고 end 값을 통해서 프린트 구분 가능

​        자연수를 입력하세요: 10
1/2/3/4/5/6/7/8/9/10/(venv)

```
# 자연수 n 을 입력받고, 1 부터 n 까지 출력하라

# '10' => 10

# str => list(str) / str => int(str)

try:
    n = int(input('자연수를 입력하세요: '))
    for i in range(n_value):# 0 ~ 9
        print(i + 1, end='/')

except:
    print('자연수를 입력하세요!!!!!!!!!!!!!')
```

## 나머지 Remainder

```
# 짝수/홀수를 구분하자. 2 => 짝! 3 => 홀!

try:

​    number = int(input('숫자를 입력하세요: '))

​    if number % 2 == 0:

​        print('짝!')

​    else:

​        print('홀!')

except:

​    print('자연수가 아닙니다')
```

```
# fizz buzz 3 6 9 게임 => 

\# 3의 배수에서 fizz 5의 배수에서 buzz 15배수에서 fizz buzz출력



number = int(input('숫자를 입력하세요: '))

for i in range(1, number+1):

​    if i % 15 == 0:

​        print('fizzbuzz', end=' ')

​    elif i % 3 == 0:

​        print('fizz', end=' ')

​    elif i % 5 == 0:

​        print('buzz', end=' ')

​    else:

​        print(i, end=' ')
```

소프트웨어 개발자가 되는 것

http://techm.kr/bbs/board.php?bo_table=article&wr_id=2137

# Dictionary의 이해



객체 : (실제하는)데이터

```
로또 스크래핑

사이트 셀렉팅 데이터값 => 스크래핑

데이터를 현실에서 가져오는 방법 

로또번호를 동행복권 API를 통해서 가져온다

https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=866

셀렉문

{"totSellamnt":81961886000,"returnValue":"success","drwNoDate":"2019-07-06","firstWinamnt":2240409000,"drwtNo6":39,"drwtNo4":34,"firstPrzwnerCo":9,"drwtNo5":37,"bnusNo":12,"firstAccumamnt":20163681000,"drwNo":866,"drwtNo2":15,"drwtNo3":29,"drwtNo1":9}
```

API를 받아올 때(더 깔끔하고 이해하기 쉬움)

dict(response)

import json #(제이슨)

```
1번째 방법

string = '나는{} 을 먹는다.'. format()
```

```
2번째 방법

string = f'나는{meal}을 먹는다.'
```

3번째 방법





키벨류 동시에

for key, value in data.items(): #items 무조거들어가야함



# 로또 번호 추출(get_lotto)

```
import requests

import json

url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=866' #로또 api



response = requests.get(url).text



data = json.loads(response) # print(type(data), data)

print(data['bnusNo'])

real_numbers = []
```



```
---------------------------------
딕셔너리 키 벨류 뽑는 법
for key, value in data.items():

​    if 'drwtNo' in key:

​        real_numbers.append(value)
for key in d: #기본적으로 키 값만 튀어나오게 되어있다.
	print(a)

```

```
print(real_numbers)



'''

{

"totSellamnt":81961886000,      # 총 판매금액

"returnValue":"success",        # 응답가능여부

"drwNoDate":"2019-07-06",       # 추첨일

"firstWinamnt":2240409000,      # 1등 금액

"drwtNo6":39,                   # no4

"drwtNo4":34,                   # no6

"firstPrzwnerCo":9,             # 1등 당첨자수

"drwtNo5":37,                   # no5

"bnusNo":12,                    # 보너스

"firstAccumamnt":20163681000,   # 이번회차 누적금

"drwNo":866,                    # 회차

"drwtNo2":15,                   # no2

"drwtNo3":29,                   # no3

"drwtNo1":9                     # no1

}

'''
```

# dictionary 가 있을 때

```
some_dict = {'june': 12, 'hello': 22, 'world': 33}
```

## 아래와 같이 key : value 로 출력하는 방법

```
june : 12
hello : 22
world : 33
```

## keys 이용하기

```
for key in some_dict.keys():
    print(key, ":", some_dict[key])
```

평범한 방식이다. perl 에서도 요런식으로 많이 사용하고 있음.

## items 이용하기

```
for key, value in some_dict.items():
    print(key, ":", value)
```

(key, value) 로 구성된 리스트를 리턴해서 key, value 를 바로 뽑아 사용 하는 방식



어플리케이션 => 사용자와 그렇게 가깝지 않다.

웹사이트

client <-> server



# 모듈 차이

```
import flask                    # 필통을 꺼낸다(연필 칼 다 가능)

random.choice([1, 2, 3, 4, 5])  # 꺼낸 필통에서 연필 사용한다



from random import choice       #필통에서 연필만 꺼낸다(칼 지우개 불가)

choice([1, 2, 3, 4, 5], 2)      #연필을 사용한다
```



# 앱라우트함수를 이용한 웹서버

```
@app.route('/') # 라우트 이게 붙으면

def index():

​    return 'Hello World!' # 이 일을 해라



@app.route('/hi') # 라우트 이게 붙으면

def hi():           # index든 hi이든 상관없음, 하지만 /백슬래시 다음 이름으로 통상적으로 붙임

​    return 'Hi!'


import random
@app.route('/pick_lotto') # 로또도 적용 가능

def pick_lotto():

​    numbers = range(1, 46)
​    lucky = random.sample(numbers, 6) 
​    return str(lucky)



if __name__ == '__main__':

​    app.run(debug=True)
```

# 전체코드

```
# import flask                    # 필통을 꺼낸다(연필 칼 다 가능)

\# random.choice([1, 2, 3, 4, 5])  # 꺼낸 필통에서 연필 사용한다



\# from random import choice       #필통에서 연필만 꺼낸다(칼 지우개 불가)

\# choice([1, 2, 3, 4, 5], 2)      #연필을 사용한다

import random

from flask import Flask



app = Flask(__name__)



@app.route('/') # 라우트 이게 붙으면

def index():

​    return 'Hello World!' # 이 일을 해라



@app.route('/hi') # 라우트 이게 붙으면

def hi():           # index든 hi이든 상관없음, 하지만 /백슬래시 다음 이름으로 통상적으로 붙임

​    return 'Hi!'



@app.route('/pick_lotto') # 라우트 이게 붙으면

def pick_lotto():

​    numbers = range(1, 46)

​    lucky = random.sample(numbers, 6) # index든 hi이든 상관없음, 하지만 /백슬래시 다음 이름으로 통상적으로 붙임

​    return str(lucky)



if __name__ == '__main__':

​    app.run(debug=True)
```

# name과 main의

```
if __name__ -- '__main__':
```

밑의 코드에서 `if __name__ == ""__main__""`은 왜 쓰는건가요?

### 소스코드

```
if __name__ == ""__main__""
    print ""hello""
```

스크립트가 파이썬 인터프리터 명령어로 패싱되어 실행되면(python myscript.py같이) 다른 언어들과는 다르게, 파이썬은 자동으로 실행되는 메인함수가 없습니다. 파이썬은 메인 함수가 없는 대신 들여쓰기 하지 않은 모든 코드(level 0코드)를 실행합니다 다만, 함수나 클래스는 정의되었지만, 실행되지는 않습니다

질문하신 경우, 최 상위 코드는 if 블록이고, `__name__`은 현재 모듈의 이름을 담고있는 내장 변수입니다. python myscript.py 같이 이 모듈이 직접 실행되는 경우에만,`__name__ 은 "__main__"`으로 설정됩니다.

따라서 질문자의 코드가 다른 모듈에 의해 import된 경우 함수와 객체의 정의는 import되지만 `__name__`이 `"__main__"`이 아니기 때문에 if문은 실행되지 않습니다.

이처럼,

```
if __name__ == "__main__":
```

을 써서, 스크립트가 직접 실행되는지 혹은 import되어 실행되는지 테스트 할 수 있습니다.

예를들어 다음 코드의 경우

#### file A.py

```
def func():
    print("function A.py")

print("top-level A.py")

if __name__ == "__main__":
    print("A.py 직접 실행")
else:
    print("A.py가 임포트되어 사용됨")
```

#### file B.py

```
import A as one

print(""top-level in B.py"")
one.func()

if __name__ == "__main__":
    print("B.py가 직접 실행")
else:
    print("B.py가 임포트되어 사용됨")
>> python A.py
top-level in A.py
A.py가 직접 실행


>>python B.py
top-level in A.py
A.py가 임포트되어 사용됨
top-level in B.py
function A.py
B.py가 직접 실행
```

장고와 플라스크 요청 응답 비슷하다 플라스크는 안쓴다

장고는 훨씬 큰 규모의 사이트 만드는데 중요

플라스크는 마이크로 프레임워크

장고는 많은 파일의 구조화를 통해

```
@app.route('/get_lotto/1')

그냥 1이라고 쓰고 싶지 않다.

어떤것을 넣을까?

<int: num>

@app.route('/get_lotto/<int:num>') 
이게 바로 변수 라우팅 variable routing임.(변수가 있는 길)

route 길 route1 1번국도 미국
라우터:
route 기능이 주소창 길을 뚫어주는것이다.
not found 

변수가 없이 노가다로
하드코딩 해놨다 = 다때려놓았다. (안좋은 코딩)
```

```
@app.route('/get_lotto/<int:num>')  # 라우트 이게 붙으면

def get_lotto_1():

​    \# 1회차 로또정보



@app.route('/hello/<name>')  # 라우트 이게 붙으면
def hello(name): # 위에 변수명하고 함수 내부 변수명하고 일치해야함
    return 'hi, {name}'
```

return 은 무조건 str만 받는다. int넣으면 안됩니다

django 장고 => 인스타그램만듬

프레임워크(도구라고 생각하삼) react 페이스북 



웹서버  앞(프론트엔드 html) 뒤(백엔드/파이썬쪽/장고 등등)

vue.js 마지막주차때 사용할 예정



서빙할 음식 컨텐츠(html) 일하게 만드게 만드는 사람에 가까운(server)



```
from flask import Flask, render_template
```

## 2차원 이상 list 의 합 구하기 

- 리스트의 합을 구하다가 int 값이 아닌 list 값을 만나면 그 안의 합을 구해주는 방식으로 재귀함수를 구성해야 2차원 이상의 list 합을 구할 수 있습니다.

> lst = [ [ 1, [1,1,1,1], 1 ] , [ 1,1,1 ] ]
>
> 
>
> def sum_list(lst, res = 0):    
>
> for i in lst:
>
> ​          if type(i) == list:
>
> ​                res += sum_list(i)
>
> ​          else:
>
> ​                res += i
>
> return res
>
> 
>
> print(sum_list(lst))

https://www.codecademy.com/



세상의 데이터를 가져오는 방법 3가지

1. 스크래핑(일반적인 사이트) -> 사람보라고 만든걸 어거지로 파헤쳐서 긁는다(딕셔너리 형태의)

2. api 프로그래밍하라고 준 의미가 있는 접점(일반인한테는 의미가없음)
3. 서비스제공자가 제공하는 패키지(가장 쉬움 주식 등..)

https://iextrading.com/apps/stocks/

모든 api 전부 무료 + 쉽게 접근가능한건 아니다

api는 유료일 수도 있다.

회원가입해야하는 것도 있고

국가꺼는 실명 인증까지해야한다



api가 가장 쉽고 정보를 받아 사용하기 쉽지만

소수의 기업만 pip install 쉽게 주진 않는다. 네이버도 없음 



```
from iexfinance.stocks import Stock

import random


companies = ['AAPL','GOOGL','TSLA','FB','AMZN']

company = Stock(random.choice(companies), token='pk_34947d6f20564c52a9dcd62bf4d4ab5f')


print(company.get_quote())

output

{'symbol': 'AAPL', 'companyName': 'Apple, Inc.', 'calculationPrice': 'close', 'open': 199.05, 'openTime': 1562679000265, 'close': 201.24, 'closeTime': 1562702400457, 'high': 201.51, 'low': 198.81, 'latestPrice': 201.24, 'latestSource': 'Close', 'latestTime': 'July 9, 2019', 'latestUpdate': 1562702400457, 'latestVolume': 20365465, 'iexRealtimePrice': 201.28, 'iexRealtimeSize': 100, 'iexLastUpdated': 1562702398891, 'delayedPrice': 201.24, 'delayedPriceTime': 1562702400457, 'extendedPrice': 200.9, 'extendedChange': -0.34, 'extendedChangePercent': -0.00169, 'extendedPriceTime': 1562715897466, 'previousClose': 200.02, 'change': 1.22, 'changePercent': 0.0061, 'iexMarketPercent': 0.019760265724352476, 'iexVolume': 402427, 'avgTotalVolume': 24728097, 'iexBidPrice': 0, 'iexBidSize': 0, 'iexAskPrice': 0, 'iexAskSize': 0, 'marketCap': 925921339200, 'peRatio': 16.78, 'week52High': 233.47, 'week52Low': 142, 'ytdChange': 0.272691, 'lastTradeTime': 1562702400457}

토큰을 기업에서 주면 정보를 찾기 쉽다
```

