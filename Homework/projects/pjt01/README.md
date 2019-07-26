## 1. 영화진흥위원회 오픈 API(주간/주말 박스오피스 데이터)

### 생성파일

- 01.py

```
import requests
import csv
from datetime import datetime, timedelta
from decouple import config

fieldnames = ['movieCd', 'movieNm', 'audiAcc']  # 영화 대표코드, 영화명, 해당일 누적관객수 필드네임
writer = csv.DictWriter(open('boxoffice.csv', 'w', encoding='utf-8', newline=''), fieldnames=fieldnames)  # boxoffice.csv 파일 작성, writer 변수로 저장
writer.writeheader()  # 헤더파일 입력

# boxoffice.csv라는 파일에 dict형식의 파일 작성
API_KEY = config('API_KEY')  # decouple을 이용한 보안키 획득
movie_codes = []  # 영화 대표코드 리스트 작성(하단의 for 구문 사용 시 최신 값 유지 및 중복 방지 목적)

for i in range(0, 50):  # 총 50주 기간

    d = datetime(2019, 7, 13) - timedelta(weeks=i)  # 최신 업데이트 일자(19.07.13)
    standard_time = d.strftime("%Y%m%d")
    URL = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?key={API_KEY}&weekGb=0&targetDt={standard_time}'
    data = requests.get(URL).json()

    result = {}  # 영화 대표코드 , 영화명 , 해당일 누적관객수 기록할 Dict 값
    for movie in data.get('boxOfficeResult').get('weeklyBoxOfficeList'):
        if movie.get('movieCd') not in movie_codes:  # API를 통한 값 vs 영화 대표코드 중복 방지
            movie_codes.append(movie.get('movieCd'))  # 영화 대표코드 리스트에 추가
            result['movieCd'] = movie.get('movieCd')
            result['movieNm'] = movie.get('movieNm')
            result['audiAcc'] = movie.get('audiAcc')
            writer.writerow(result)  # for구문을 돌면서 csv.DictWriter에 한 줄 씩 저장

```

### 결과 파일

- boxoffice.csv

## 2. 영화진흥위원회 오픈 API(영화 상세정보)

### 생성 파일

- 02.py

  ```
  import requests
  import csv
  from decouple import config
  
  with open('movie.csv', 'w', encoding='utf-8', newline='') as f:  # movie.csv 작성
      fieldnames = ['movieCd', 'movieNm', "movieNmEn", "movieNmOg", 'watchGradeNm', 'showTm', 'prdtYear', 'genres', 'directors']
      # 영화 대표코드 , 영화명(국문) , 영화명(영문) , 영화명(원문) , 관람등급 , 개봉연도 , 상영시간 , 장르 , 감독명
      writer = csv.DictWriter(f, fieldnames=fieldnames)
      writer.writeheader()
      API_KEY = config('API_KEY')
      movie_codes = []
  
      with open('boxoffice.csv', 'r', encoding='utf-8') as f:  # boxoffice.csv를 불러옴
          for row in csv.DictReader(f):
              movie_codes.append(row['movieCd'])  # movieCd열을 movie_codes의 리스트에 저장
  
      for movie_code in movie_codes:
          URL = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json?key={API_KEY}&movieCd={movie_code}'
          source = requests.get(URL).json()["movieInfoResult"]['movieInfo']
          result = {}  # CSV로 저장할 최종 딕셔너리 자료
          result['movieCd'] = source['movieCd']  # 대표코드
          result['movieNm'] = source['movieNm']  # 영화명(국문)
          result['movieNmEn'] = source['movieNmEn']  # 영화명(영문)
          if source['movieNmOg']:
              result['movieNmOg'] = source['movieNmOg']  # 영화명(원문)
          if source['audits']:  # 관람등급
              result['watchGradeNm'] = source['audits'][0]['watchGradeNm']
          result['showTm'] = source['showTm']  # 상영시간
          result['prdtYear'] = source['prdtYear']  # 개봉연도
          if source['genres']:  # 장르
              result['genres'] = source['genres'][0]['genreNm']
          if source['directors']:  # 감독명
              result['directors'] = source['directors'][0]['peopleNm']
          writer.writerow(result)
  
  ```

### 결과 파일

- movie.csv

## 3. 영화진흥위원회 오픈 API(영화인 정보)

### 생성 파일

- 03.py

  ```
  import requests
  from datetime import datetime, timedelta
  from decouple import config
  import csv
  
  director_reader = csv.DictReader(open('movie.csv', 'r', encoding='utf-8'))
  director_names = []  # movie.csv에서 불러온 감독이름을 저장하기 위한 빈 리스트
  for row in director_reader:
      director_names.append(row['directors'])
  
  
  with open('director.csv', 'w', encoding='utf-8', newline='') as f:  # director.csv 생성
      fieldnames = ['peopleCd', 'peopleNm', 'filmoNames', 'repRoleNm']
      # 영화인 코드 , 영화인명 , 분야 , 필모리스트
      writer = csv.DictWriter(f, fieldnames=fieldnames)
      writer.writeheader()
  
      API_KEY = config('API_KEY')
      URL = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/people/searchPeopleList.json?key={API_KEY}&peopleNm='
  
      for name in director_names:  # 감독명을 통한 조회
          result = {}
          if requests.get(URL + name).json()['peopleListResult']:
              director_data = requests.get(URL + name).json()['peopleListResult']['peopleList'][0]  # 감독명을 통한 주소로 director_data를 받음
              result['peopleCd'] = director_data['peopleCd']
              result['peopleNm'] = director_data['peopleNm']
              if director_data['filmoNames']:  # filmoNames이 없는 경우 오류 방지
                  result['filmoNames'] = director_data['filmoNames']
              if director_data['repRoleNm']:   # repRoleNm이 없는 경우 오류 방지
                  result['repRoleNm'] = director_data['repRoleNm']
              writer.writerow(result)
  
  ```

### 결과 파일

- director.csv