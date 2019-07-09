# StartCamp Day_02

## what is git?

#### **git: scm(source code manager) / vcs(version control system)**

```
최종발표.pptx 
최종발표_수정.pptx
최종발표_최종수정.pptx
최종발표_최종수정_최종.pptx
...
```

**누구나 이러한 경험이 있다.**

```
최종발표v1.pptx

최종발표v2.pptx

최종발표v3.pptx

...

최종발표v5.pptx
```

**개선되었지만 버전에 따른 수정사항이 기억나지 않는다.**

## `git → 버전관리 해주는 감시카메라`



폴더 프로젝트로 만들어 모든 사항에 대하여 버전관리 할 수도 있다.



![](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1562632985842.png)

```
* git init을 치는 순간 master가 표시되며 git이 관리하겠다는 의미가 된다.
* cd(Change Directory) 기능
 - cd .. : 상위폴더로 이동
 - cd TIL: TIL폴더로 이동

* cd(경로 변경) touch(파일 만듬) mkdir(폴더 만듬) ~ ..(상위 폴더) ls(list)
* git status()
* untracked files(추적되지 않는 파일)
```



| ![1562633424149](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1562633424149.png) | ![](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1562633212190.png) |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
|                                                              |                                                              |

```
tab 사용방법
cd 디렉토리 파일 이름 타이핑 중간에 tab하면 비슷한 파일명을 바로 불러준다.
 # pratice_git을 전부 타이핑하기는 번거롭다
```



| ![1562634639288](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1562634639288.png) |      |
| ------------------------------------------------------------ | ---- |
|                                                              |      |

```
git commit -m
```

![1562634719039](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1562634719039.png)



![1562634859822](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1562634859822.png)

한번만 하면 되는 작업임

![1562634902767](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1562634902767.png)

방향키 눌러서 이전 명령어 불러옴

![1562634926596](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1562634926596.png)

commit 카메라 찰칵이라 생각하자

git add 

init 시작

add 관리할 파일 추가

commit  찰칵

-m 옵션이지만 반드시 붙여줘야하는 옵션

rm 파일명



`git init`

`git add <filename>`

`git commit -m '<message>'`

변경사항 저장

`git add <filename>`

`git commit -m '<message>'`

`git status` => 상태를 물어보는 명령어

`git log` => 사진(commit)들 로그를 보여줌

`pwd` => 내가 어디 폴더에 있는지 보여줌



### or create a new repository on the command line



```
echo "# practice_git" >> README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin https://github.com/simpsonyong/practice_git.git
git push -u origin master
```

### …or push an existing repository from the command line



```
git remote add origin https://github.com/simpsonyong/practice_git.git
git push -u origin master
```

```
git remote add origin https://github.com/simpsonyong/practice_git.git
```

origin 이 아니라도 다른 이름으로 명명가능

```
student@M703 MINGW64 ~/practice_git (master)
$ git remote -v
origin  https://github.com/simpsonyong/practice_git.git (fetch)
origin  https://github.com/simpsonyong/practice_git.git (push)

student@M703 MINGW64 ~/practice_git (master)
$ git push origin master

```

git은 사진기를 통해 사진을 계속 저장한다고 생각하자

```
git(카메라앱) is not github(드라이브)
```

특화정도 github(공개) gitlab(사내용) bitbucket(개인용)

```
student@M703 MINGW64 ~/practice_git (master)
$ git add .
```

지금 내가 있는 곳에서 모두 저장하겠다

```
student@M703 MINGW64 ~/practice_git (master)
$ git add -A
```

git add . 아무거나 다 찍겠다.



커밋 메세지가 나중에는 남과 프로젝트 같이할때 무엇으로 할 것인 가도 중요하다

![1562638911515](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1562638911515.png)

제대로 처음부터 쓰자 | 이용하여

```
$ git commit -m 'startcamp | learn git | 190709'
```

-u 기능

git push -u를 붙이면 아무말도 안해도 어디로 보낼지 정확하게 설정됨



```
student@M703 MINGW64 ~/TIL (master)
$ git add . ; git commit -m 'python | learn list | 190709'
On branch master
nothing to commit, working tree clean

student@M703 MINGW64 ~/TIL (master)
$ git push github master
Everything up-to-date
```



OS 운영체제 operating system

개발자 세상 UNIX 세상

일반인 세상 window 세상



맥북 UNIX에 기준에 맞춰서 개발되어 개발자에게 좋다



유닉스가 전통 -> 유료



오픈소스 형식이 리눅스가 공짜로 풀림 -> 더 커짐



 \백슬래시 -> 

한글판 윈도우면 



CLI종류

1. 유닋스 



코드블럭 ```



\```python

import random



numbers = range(1, 46) # 1부터 45까지



lucky_numbers = random.sample(numbers, 6)



print(lucky_numbers)

\```



파이썬 3.5 vs 파이썬 3.7 => 안정화된 버전이므로 3.7



```
import webbrowser



webbrowser.open()
```

앞에 () 가 없으므로 import할 때 webbrowser는 단순한 함수가 아닌 다양한 기능을 가진 패키지 덩어리 라 봐야함



open 안에 url www. 안치면 사회악 나옴





ctrl + / => 블록 설정 후 전체 주석처리(주석 해제도 가능)



함수 => 모르면 구글링 (존재하는지만 알면 된다)

웹 크롤러 -> 사이트 정보를 코딩으로 가져오는게 가능하다



웹 커뮤니케이션 방식 

1. 요청 request URL(주소)을 통해 보낸다
2. 응답 response 응답 문서(HTML XML 등)로 받는다





```
http://edu.ssafy.com/edu/board/mentoring/list.do

?searchBrdItmCdVal=3

&

brdItmSeq= #게시글 순번

&

regUserId=

&

searchMyItm=

&

searchWord= #가나다

&

_csrf=f84fcb10-adf4-4f5b-9f05-b90762f4a23e

&

pageIndex=1
```

```
위시위그 wysiwyg 한글오피스 등...

what you see is what you get
```





우리가 보는 네이버 사이트는 원본이 아니라서 우리가 받은 성적표처럼 우리가 직접 수정할 수 있다.. 

```
vs code: linter pep8 설치

* git에서 vscode 처럼 불필요한 폴더에 대한 트래킹을 방지하기 위해서 사용하는 코드
student@M703 MINGW64 ~/TIL (master)
$ touch .gitignore
```

![1562651329714](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1562651329714.png)touch .gitignore 로 파일 생성하고

안에 코드에 .vscode/ 하세요

```
student@M703 MINGW64 ~/TIL (master)
$ git add.
git: 'add.' is not a git command. See 'git --help'.
The most similar command is
        add

student@M703 MINGW64 ~/TIL (master)
$ git add .

student@M703 MINGW64 ~/TIL (master)
$ git commit -m 'startcamp | add gitig
nore | 190709'
[master 4fd2847] startcamp | add gitignore | 190709
 1 file changed, 1 insertion(+)
 create mode 100644 .gitignore

student@M703 MINGW64 ~/TIL (master)
$ " to include in what will be committed)
```

```
확장자 => 컴퓨터가 구분하기 위해서 있는 것이다.

pip 파이썬 세상에서 함수 구매할 수 있는 곳

예) pip install requests

```

![1562652587367](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1562652587367.png)

venv 가상환경 구축 후



f1 linter pep8 설치 후

![1562653057491](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1562653057491.png)

이걸로 실행시켜서

pip install requests



```
import requests

response = requests.get('https://naver.com').text

print(response)
```

[`venv`](https://docs.python.org/ko/3/library/venv.html#module-venv) 모듈은 자체 사이트 디렉터리를 갖는 경량 "가상 환경"을 만들고, 선택적으로 시스템 사이트 디렉터리에서 격리할 수 있도록 지원합니다. 각 가상 환경은 고유한 파이썬 바이너리(이 환경을 만드는 데 사용된 바이너리 버전과 일치함)를 가지며 자신의 사이트 디렉터리에 독립적으로 설치된 파이썬 패키지 집합을 가질 수 있습니다.

파이썬 가상 환경에 대한 자세한 내용은 [**PEP 405**](https://www.python.org/dev/peps/pep-0405)를 참조하십시오.

더 보기

 

[Python Packaging User Guide: Creating and using virtual environments](https://packaging.python.org/installing/#creating-virtual-environments)

참고

 

`pyvenv` 스크립트는 파이썬 3.6 에서 폐지되었고, 가상 환경이 어떤 파이썬 인터프리터를 기반으로 하는지에 대한 잠재적인 혼동을 방지하기 위해 `python3 -m venv`를 사용합니다.



`Setuptools` 나 `pip`과 같은 일반적인 설치 도구는 가상 환경에서 예상대로 작동합니다. 즉, 가상 환경이 활성화되면, 명시적으로 그렇게 지정하지 않아도 파이썬 패키지를 가상 환경에 설치합니다.



https -> 통신방식 브라우저에서는 작성 필요 없으나 코딩할때는 세밀하게 작성해야함

## 1. Python에서의 가상 환경이란?

- 파이썬에서는 한 라이브러리에 대해 하나의 버전만 설치가 가능합니다.
- 여러개의 프로젝트를 진행하게 되면 이는 문제가 됩니다. 작업을 바꿀때마다 다른 버전의 라이브러리를 설치해야합니다.
- 이를 방지하기 위한 격리된 독립적인 가상환경을 제공합니다.
- 일반적으로 프로젝트마다 다른 하나의 가상환경을 생성한 후 작업을 시작하게 됩니다.
- 가상환경의 대표적인 모듈은 3가지가 있습니다.
  - venv : Python 3.3 버전 이후 부터 기본모듈에 포함됨
  - virtualenv : Python 2 버전부터 사용해오던 가상환경 라이브러리, Python 3에서도 사용가능
  - conda : Anaconda Python을 설치했을 시 사용할 수있는 모듈
  - pyenv : pyenv의 경우 Python Version Manger임과 동시에 가상환경 기능을 플러그인 형태로 제공



```
뷰티풀 수프 4 설치 긴 텍스트를 좀더 편하게 가지고 놀 수 있게 하는 도구

pip install bs4

설치 후

import requests
import bs4

response = requests.get('https://naver.com').text
text = bs4.BeautifulSoup(response)

print(text)


import requests
import bs4

url = 'https://finance.naver.com/sise/'
response = requests.get(url).text
text = bs4.BeautifulSoup(response)

print(text)
```

ur1을 변수로 지정해야 나중에 url과 관련한 사항을 추가하거나 수정하기 용이하다

```


f12 => 원하는 값 찾기 => copy => copy selecter



import requests

import bs4



url = 'https://finance.naver.com/sise/'

response = requests.get(url).text

text = bs4.BeautifulSoup(response, 'html.parser') # 어떻게 예뻐지게 해주세요라는 함수

kospi = text.select_one('#KOSPI_now')



```



```
import requests

import bs4


url = 'https://finance.naver.com/sise/'

response = requests.get(url).text

text = bs4.BeautifulSoup(response, 'html.parser')

kospi = text.select_one('#KOSPI_now')

print(kospi.text)

출력

student@M703 MINGW64 ~/TIL/00_startcamp/day2 (master)
$ python scraping.py
2,052.03
(venv)
```



select_one 하나만 가져올때

select 다 가져올 떄



![1562655900625](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1562655900625.png)

tr = table row 가로우 세로 column

웹세상에서 response 200은 오케이의 세상

response 404는 없다의 세상 not found 

response 406 너의 요청을 받지 않겠다는 의미



멜론 아마존 등은 추가 검증이 필요함 우리가 보내는 User-agent 정보를 추가 기입해야함 (디도스등 방지용)

유저에이전트 키벨류를 넣어야함

멜론은 헤더가 있는지만 파악함 



```
import bs4

import requests



url = 'https://www.melon.com/chart/index.htm'



headers = {'User-Agent': ':)'}



response = requests.get(url, headers=headers)

print(response)

출력
student@M703 MINGW64 ~/TIL/00_startcamp/day2 (master)
$ python melon50.py
<Response [200]>
(venv)

웃어주면 통과한 격
```

못뚫는것은 없지만 url을 통해서 문서 한장을 가져오고 이것을 통해서 우리가 원하는 정보를 추출할 수 있다.



```
import bs4

import requests



url = 'https://www.melon.com/chart/index.htm'



headers = {'User-Agent': ':)'} # 헤더값 : :)



response = requests.get(url, headers=headers).text # header 값 입력을 통해 사이트 자료 가져옴

text = bs4.BeautifulSoup(response, 'html.parser') # parser를 통해서 예쁘게 꾸며준다

rows = text.select('.lst50') # lst50 하나하나 랭크를 가져온다





    rank = row.select_one('td:nth-child(2) > div > span.rank').text # 텍스트 안붙이면  span 등이 다 출력됨 엑기스만 뽑으려면 .text 넣을것

    title = row.select_one('td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a').text

    artist = row.select_one('td:nth-child(6) > div > div > div.ellipsis.rank02 > a').text

    print(rank, title, artist)

결과 output
student@M703 MINGW64 ~/TIL/00_startcamp/day2 (master)
$ python melon50.py
1 헤어져줘서 고마워 벤
2 술이 문제야 장혜진
3 We don`t talk together (Feat. 기리보이) (Prod. SUGA) 헤이즈 (Heize)
4 니 소식 송하예
5 Snapping 청하
6 솔직하게 말해서 나 김나영
7 사랑에 연습이 있었다면 (Prod. 2soo) 임재현
8 Speechless (Full) Naomi Scott
9 2002 Anne-Marie
10 bad guy Billie Eilish (빌리 아일리시)
11 포장마차 황인욱
12 너에게 못했던 내 마지막 말은 다비치
13 오늘도 빛나는 너에게 (To You My Light) (Feat.이라온) 마크툽 (MAKTUB)
14 작은 것들을 위한 시 (Boy With Luv) feat. Halsey 방탄소년단
15 괜찮아도 괜찮아 (That`s okay) 디오 (D.O.)
16 사랑이 식었다고 말해도 돼 먼데이 키즈 (Monday Kiz)
17 서울 밤 (feat. 빈지노) 어반자카파
18 FANCY TWICE (트와이스)
19 비가 내리는 날에는 윤하 (YOUNHA)
20 A Whole New World Mena Massoud
21 누구 없소 (NO ONE) (Feat. B.I of iKON) 이하이
22 주저하는 연인들을 위해 잔나비
23 U GOT IT 갓츄 (GOT U)
24 짐살라빔 (Zimzalabim) Red Velvet (레드벨벳)
25 노래방에서 장범준
26 Goodbye 박효신
27 사월이 지나면 우리 헤어져요 (Beautiful goodbye) 첸 (CHEN)
28 사계 (Four Seasons) 태연 (TAEYEON)
29 그때가 좋았어 케이시 (Kassy)
30 열대야 (Fever) 여자친구 (GFRIEND)
31 아퍼 (Feat. Kid Milli, Lil tachi, 김승민, NO:EL, C JAMM) 기리보이
32 모든 날, 모든 순간 (Every day, Every Moment) 폴킴
33 Uh-Oh (여자)아이들
34 나만, 봄 볼빨간사춘기
35 BIRTHDAY 전소미
36 Paris In The Rain Lauv
37 사계 (하루살이) 엠씨더맥스
38 너를 만나 폴킴
39 BAND 창모 (CHANGMO)
40 이뻐이뻐 (Pretty girl) 크레파스
41 움직여 (MOVE) (Prod. by ZICO) SIXC (6 crazy)
42 대충 입고 나와 우디 (Woody)
43 AH YEAH (아예) WINNER
44 달라달라 ITZY (있지)
45 소우주 (Mikrokosmos) 방탄소년단
46 벌써 12시 청하
47 봄날 방탄소년단
48 옥탑방 (Rooftop) 엔플라잉 (N.Flying)
49 Kill This Love BLACKPINK
50 비워 (Beer) (Prod. Way Ched) 창모 (CHANGMO)
(venv)
```

```
csv (seperated value : 분리된 데이터) 형식

1, 술이야, 바이브

2, 주저하는.., 잔나비
```

딕셔너리 키랑 키밸류 2개 동시에 꺼내려면  items() 이용

```
for name, phone in restaurants.items(): # 키, 키밸류

    print(name, phone)
    
출력
student@M703 MINGW64 ~/TIL/00_startcamp/day2 (master)
$ python file_control.py
양자강 02-557-4211
김밥카페 02-553-3181
순남시래기 02-508-0887
```

## 쓰기

```
restaurants = {

​    '양자강': '02-557-4211',

​    '김밥카페': '02-553-3181',

​    '순남시래기': '02-508-0887'

}



with open('restaurant.csv', 'w', encoding = 'utf-8') as f:# encoding='utf-8'는 안쓰면 한글이 깨진다.

​    for name, phone in restaurants.items():

​        f.write(f'{name}, {phone}\n')
```

## 읽기

```
import csv

with open('restaurant.csv', 'r', encoding='utf-8') as f:
    items = csv.reader(f)
    for item in items:
        print(item)
        
```



# 문자열 리터럴

양식 문자열 리터럴(formatted string literal, f-string)은 문자열 속의 식을 그 평가 결과로 치환하는 문자열이다. 이 기능은 파이썬 버전 3.6에서 새로 도입된 기능이어서 그보다 낮은 버전에서는 사용할 수 없다.

양식 문자열 리터럴을 작성할 때는 `f'문자열'`과 같이 문자열을 나타내는 따옴표 기호 앞에 `f`를 붙인다. 그리고 평가하려는 식을 중괄호 안에 삽입한다.

**코드 11-26** 양식 문자열 리터럴로 과목별 성적 양식화하기

```
>>> physics, chemistry, biology = 80, 90, 70
>>> f'물리학: {physics}, 화학: {chemistry}, 생물학: {biology}'
'물리학: 80, 화학: 90, 생물학: 70'
```

변수의 이름을 평가하는 것 뿐 아니라, 다른 식도 평가할 수 있다.

**코드 11-27** 양식 문자열 리터럴로 과목 점수 합계 평가하기

```
>>> f'총점: {physics + chemistry + biology}'
'총점: 240'
```

양식 문자열 리터럴에서도 자리 길이 지정 등 앞서 살펴본 다양한 양식 규칙을 적용할 수 있다. 다음 예는 for 문, `range()` 함수, 양식 문자열 리터럴을 이용해 제곱 곱셈표를 출력해 본 것이다.





```
import bs4

import requests

import csv # 멜론 정보들을 편집할 수 있게 csv 함수 불러옴



url = 'https://www.melon.com/chart/index.htm'



headers = {'User-Agent': ':)'} # 헤더값 : :)



response = requests.get(url, headers=headers).text # header 값 입력을 통해 사이트 자료 가져옴

text = bs4.BeautifulSoup(response, 'html.parser') # parser를 통해서 예쁘게 꾸며준다

rows = text.select('.lst50') # lst50 하나하나 랭크를 가져온다



writer = csv.writer(open('melon50.csv', 'w', encoding='utf-8' , newline='')) # writer함수 이용해서 new line'' 이유 : writer가 자동으로 띄어쓰기를 하므로 그것을 없앤다
writer.writerow(['순위', '제목', '가수']) # 엑셀이므로 미리 필터라인에 들어갈 제목을 작성한다



for row in rows:

​    rank = row.select_one('td:nth-child(2) > div > span.rank').text

​    title = row.select_one('td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a').text

​    artist = row.select_one('td:nth-child(6) > div > div > div.ellipsis.rank02 > a').text

​    \# print(rank, title, artist)

​    \# f.write(f'{rank},{title},{artist}\n')

​    \# f.write(r'' + ',' + r'' + ',' + r'' + '\n')

​    writer.writerow([rank, title, artist])
```

