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
