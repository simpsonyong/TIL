파일 3개: README.md(결과보고서) / boxoffice.csv / movie.csv / director.csv

필수 라이브러리 활용 + requests 가상환경 구축 후 설치

영화관입장권통합전산망 오픈API:  http://www.kobis.or.kr/kobisopenapi/homepg/main/main.do

오픈 API 서비스 키 환경변수 지정 / 노출 금지 88046c163877d0c66e3c8b436a091eaa

pip install python-decouple

from decouple import config

환경 변수 지정 X => 나중에 볼 예정 별거 아님

환경변수 말고 decouple이 더 깔끔해서 이 방법으로

import requests

from decouple import config

'

```
"""

http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json -> 이렇게 만 입력하면 사이트에서 내가 무엇을 요구하는지 모른다

?

key=430156241533f1d058c603178cc3ca0e

&

targetDt=20120101

"""
```

크롬 확장프로그램 JSON Viewer깔아야 API 깔끔하게 보임

.get(name) vs [name] 오류남 vs 안남



대표코드 "movieCd": "20112207",

영화명 "movieNm": "미션임파서블:고스트프로토콜",

누적관걕수  "audiAcc": "5328435",





requests.get() -> 사이트에서 url 적고 엔터치는 거랑 비슷함



csv형태의 파일 -> 딕셔너리로 저장하는 것이 제일 깔끔함





파이썬으로 프로그래밍을 하다보면 날짜와 시간 처리를 해야 하는 경우가 자주 생깁니다. 여기서는 날짜와 시간을 표현하는 time과 datetime 모듈을 소개하겠습니다.

### 47.4.1  time 모듈로 현재 시간 구하기

먼저 시간을 표현하는 time 모듈입니다. 다음과 같이 time 모듈의 time 함수를 호출하면 1970년 1월 1일 0시 0분 0초 이후 경과한 시간을 초단위로 반환합니다. 시간대는 UTC(Universal Time Coordinated, 협정 세계시)를 사용합니다.

```
>>> import time
>>> time.time()
1526694734.1275969
```

### 47.4.2  날짜와 시간 형태로 변환하기

time 모듈의 localtime 함수를 사용하면 time에서 반환한 값을 날짜와 시간 형태로 변환해줍니다. 특히 localtime이라는 이름 그대로 현재 지역의 시간대를 사용합니다. 우리나라에서 실행했다면 UTC에 9시간을 더한 KST(Korea Standard Time, 한국 표준시)를 사용합니다(UTC+09:00).

- **time.localtime(****초)**

```
>>> time.localtime(time.time())
time.struct_time(tm_year=2018, tm_mon=5, tm_mday=19, tm_hour=10, tm_min=54, tm_sec=25, tm_wday=5, tm_yday=139, tm_isdst=0)
```

여기서 tm_wday는 요일(월요일~일요일, 0~6), tm_yday는 1월 1일부터 경과한 일수,tm_isdst는 서머타임 여부입니다.

### 47.4.3  날짜/시간 포맷에 맞춰서 출력하기

time.localtime으로 만든 객체는 time.strftime 함수를 사용하여 원하는 날짜/시간 포맷으로 출력할 수 있습니다.

- **time.strftime('****포맷', 시간객체)**

```
>>> time.strftime('%Y-%m-%d', time.localtime(time.time()))
'2018-05-19'
>>> time.strftime('%c', time.localtime(time.time()))
'Sat May 19 11:14:27 2018'
```

%Y는 연, %m은 월, %d는 일인데, '%Y-%m-%d'는 '연-월-일' 포맷이라는 뜻입니다. 그리고 %c는 날짜와 시간을 함께 출력합니다.

다음은 날짜/시간 포맷 코드입니다.

▼ **표 47-4** 날짜

| 코드 | 설명                                      | 예                                |
| ---- | ----------------------------------------- | --------------------------------- |
| %a   | 요일 줄임말                               | Sun, Mon, ... Sat                 |
| %A   | 요일                                      | Sunday, Monday, ..., Saturday     |
| %w   | 요일을 숫자로 표시, 월요일~일요일, 0~6    | 0, 1, ..., 6                      |
| %d   | 일                                        | 01, 02, ..., 31                   |
| %b   | 월 줄임말                                 | Jan, Feb, ..., Dec                |
| %B   | 월                                        | January, February, …, December    |
| %m   | 숫자 월                                   | 01, 02, ..., 12                   |
| %y   | 두 자릿수 연도                            | 01, 02, ..., 99                   |
| %Y   | 네 자릿수 연도                            | 0001, 0002, ..., 2017, 2018, 9999 |
| %H   | 시간(24시간)                              | 00, 01, ..., 23                   |
| %I   | 시간(12시간)                              | 01, 02, ..., 12                   |
| %p   | AM, PM                                    | AM, PM                            |
| %M   | 분                                        | 00, 01, ..., 59                   |
| %S   | 초                                        | 00, 01, ..., 59                   |
| %Z   | 시간대                                    | 대한민국 표준시                   |
| %j   | 1월 1일부터 경과한 일수                   | 001, 002, ..., 366                |
| %U   | 1년중 주차, 월요일이 한 주의 시작으로     | 00, 01, ..., 53                   |
| %W   | 1년중 주차, 월요일이 한 주의 시작으로     | 00, 01, ..., 53                   |
| %c   | 날짜, 요일, 시간을 출력, 현재 시간대 기준 | Sat May 19 11:14:27 2018          |
| %x   | 날짜를 출력, 현재 시간대 기준             | 05/19/18                          |
| %X   | 시간을 출력, 현재 시간대 기준             | '11:44:22'                        |

### 47.4.4        datetime 모듈로 현재 날짜와 시간 구하기

이번에는 datetime 모듈의 datetime 클래스를 사용해보겠습니다. datetime.datetime으로 현재 날짜와 시간을 구할 때는 today 메서드를 사용합니다(현재 시간대 기준, KST).

- **datetime.datetime.today()**

```
>>> import datetime
>>> datetime.datetime.today()
datetime.datetime(2018, 5, 19, 13, 15, 15, 881617)
```

만약 datetime 모듈로 현재 시간을 구할 때 UTC를 기준으로 구하고 싶다면 now 메서드에 pytz 모듈로 시간대를 지정해주어야 합니다.

- **datetime.datetime.now(****시간대객체)**

먼저 pip로 pytz 모듈을 설치합니다.

```
pip install pytz
```

그리고 pytz.timezone에 'UTC'를 지정하면 UTC를 기준으로 시간을 구할 수 있습니다(KST보다 9시간 이전의 시간이 나옴).

```
>>> datetime.datetime.now(pytz.timezone('UTC'))
datetime.datetime(2018, 5, 19, 4, 40, 12, 536110, tzinfo=<UTC>)
```

### 47.4.5  특정 날짜와 시간으로 객체 만들기

또는, datetime.datetime에 연, 월, 일, 시, 분, 초, 마이크로초를 넣어서 객체를 만들 수도 있습니다.

- **datetime.datetime(year, month, day, hour=0, minute=0, second=0, microsecond=0)**

```
>>> d = datetime.datetime(2018, 5, 19)
>>> d
datetime.datetime(2018, 5, 19, 0, 0)
```

### 47.4.6  문자열로 날짜/시간 객체 만들기

strptime 메서드를 사용하면 문자열 형태의 날짜를 datetime.datetime 객체로 만들 수 있습니다. 이때는 날짜/시간 포맷을 지정해줘야 합니다.

- **datetime.datetime.strptime('****날짜문자열', '포맷')**

```
>>> d = datetime.datetime.strptime('2018-05-19', '%Y-%m-%d')
>>> d
datetime.datetime(2018, 5, 19, 0, 0)
```

### 47.4.7  날짜/시간 객체를 문자열로 만들기

반대로 datetime 객체를 문자열로 만들 수도 있습니다. 이때는 strftime 메서드를 사용합니다.

- **datetime****객체.strftime('포맷')**

```
>>> d.strftime('%Y-%m-%d')
'2018-05-19'
>>> d.strftime('%c')
'Sat May 19 00:00:00 2018'
```

### 47.4.8  날짜와 시간 속성에 접근하기

datetime.datetime 객체는 연( year), 월(month), 일(day), 시(hour), 분(minute), 초(second), 마이크로초(microsecond) 속성을 따로 가져올 수 있습니다.

```
>>> today = datetime.today()
>>> today.year, today.month, today.day, today.hour, today.minute, today.second, today.microsecond
(2018, 5, 19, 9, 54, 15, 868556)
```

### 47.4.9  날짜와 시간 차이 계산하기

datetime 모듈에서 유용한 기능이 바로 datetime.timedelta입니다. datetime.timedelta는 두 날짜와 시간 사이의 차이를 계산할 때 사용합니다.

- **datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0,                    minutes=0, hours=0, weeks=0)**

다음은 2018년 5월 13일에서 20일전 날짜를 구합니다.

```
>>> d = datetime(2018, 5, 13)
>>> from datetime import timedelta
>>> d - timedelta(days=20)
datetime.datetime(2018, 4, 23, 0, 0)
```

즉, datetime.datetime 객체에서 datetime.timedelta를 빼면 이전 날짜와 시간을 구하고, 더하면 이후 날짜와 시간을 구합니다.

특히 datetime.datetime 객체에서 datetime.datetime 객체를 빼면 datetime.timedelta객체가 나옵니다.

```
>>> datetime(2018, 5, 13) - datetime(2018, 4, 1)
datetime.timedelta(42)
```



# 시간출력

```
import time
from datetime import date, timedelta

std_date = date(2019, 7, 21)
for i in range(50):
    print(std_date.strftime('%y%m%d'))
    std_date = std_date - timedelta(weeks=1)
    
-----output----
190721
190714
190707
190630
190623
190616
190609
```

# 교수님 time설명

```
from datetime import date, timedelta

d = datime(2019, 7, 12) - timedelta(weeks=2)
d.strftime('%Y%m%d')
```

날짜

[]



날짜 영화 코드 관객수

1		ㅇㅇ ㅇㅇ ㅇㅇ



![1563522250042](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1563522250042.png)

![1563522220286](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1563522220286.png)

if 설정을 하지 않으면 밑에처럼 INDEX OUT OF RANGE 가 나온다 FALSE값ㅇ르 반환하므로